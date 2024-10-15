# This is a simplified example of a Masi control system.

# First, we import the modules we want to use
from control_modules import PWM_controller   # for servo, motor or any PWM device control
from control_modules import  ADC_sensors      # for analog sensor (voltage) readings

import time             # for sleeping
import random           # for random placeholder values


# Optional: Xbox controller
# you can also import modules like this
import control_modules.joystick_module as joystick_module


# remember to have every needed libraries installed!
# pip3 install PyYAML
# pip3 install inputs (for Xbox controller)

# if running with real hardware, you also need these:
# pip3 install adafruit-circuitpython-servokit
# ADCPi libraries: https://github.com/abelectronicsuk/ABElectronics_Python_Libraries/blob/master/ADCPi/README.md


def main(adc,pwm, controller):
    step = 0    # To make the prints more readable

    # Main example loop
    while True:


        if step % 10 == 0:  # print every 10th step
            # Read raw analog voltage from all configured sensors
            raw_sensor_values = adc.read_raw()
            print(f"Raw values: {raw_sensor_values}")

        if step % 10 == 0:  # print every 10th step
            # Read voltage from all configured sensors, with scaling and filtering
            sensor_values = adc.read_filtered()
            print(f"Filtered values: {sensor_values}")



        # typically the "control_values" would be a list containing every channel value for the control.
        # e.g. control_values = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] for 8 channels
        # the mapping of the list would need to match the configuration of the PWM controller!


        # for this example, we give the randomly generated values to the servos
        # if the controller is connected, we use the joystick value instead


        # tip: controller.is_connected() gives boolean variable, you can print it etc.
        if not controller.is_connected():   # check if controller is NOT connected

            # update the servo angle to be a random joystick value between -1..1
            control_values = random.uniform(-1, 1)  # some value between these numbers
            pwm.update_values(control_values)

            # wait a bit with the random values, as the servos might not like the constant rapid changes
            #time.sleep(1.0)
        else:
            # controller is connected, use the joystick value
            joy_values = controller.read()

            pwm.update_values(joy_values['LeftJoystickY'])

        # you can see the servo angles like this:
        print(pwm.servo_angles)

        # to get the value without naming (for processing etc., you can use for example:
        #example_servo_angle = pwm.servo_angles['ExampleServo1 angle']
        #print(f"Example servo direct value: {example_servo_angle}")

        step += 1
        # Sleep time
        time.sleep(0.5)



if __name__ == '__main__':

    # Initialize PWM controller
    pwm = PWM_controller.PWM_hat(
        config_file='configuration_files/PWM_config.yaml',  # use the config file to set up the PWM controller
        simulation_mode=True,
        # with simulation mode enabled, you can mess around with the system without the correct hardware
        input_rate_threshold=1,
        # set the safety threshold (how many updates required per second to be able to control the servos). Set to 0 to disable
        deadzone= 0.5  # set the input deadzone (how much input is required to start moving the servos).
    )

    # Initialize ADC sensors
    adc = ADC_sensors.ADC_hat(
        config_file='configuration_files/ADC_config.yaml',  # use the config file to set up the ADC sensors
        decimals=2,  # output decimal points
        simulation_mode=True
    )


    # Initialize Xbox controller
    controller = joystick_module.XboxController()


    # Run the main loop
    try:
        main(adc,pwm, controller)
    except KeyboardInterrupt:
        # Good practice is to reset the system when quitting. "finally" call also works well for this
        print("Exiting...")
        pwm.reset()
