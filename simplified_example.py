# this is a very simple example of how to use the modules

# before usage, remember to install the needed libraries
# and configure the configuration files correctly!


# import modules from the control_modules folder
from control_modules import PWM_controller  # for PWM (servo) control

from control_modules import joystick_module # for Xbox (or any other generic) controller

from time import sleep  # for sleeping

import random   # for generating random values


# Initialize the PWM controller
pwm = PWM_controller.PWM_hat(config_file='configuration_files/example_PWM_config_file.yaml',  # Load the config file from the configuration_files folder
                             input_rate_threshold=0,  # Set the safety stop threshold to 0 for testing (= disabled)
                             deadzone=0)                                                         # Set the deadzone to 0 for testing (= disabled)
                            # you could also give more arguments:
                            # simulation_mode=True, this is deprecating as the simulation mode is automatically enabled if the hardware is not found
                            # pump_variable=True,   makes the pump speed change based on the system load
                            # tracks_disabled=True  disables track control

# initializing the PWM controller will also initialize the servos to their default positions!
# if safety rate threshold is set to more than 0, safety monitoring systems will also start up!


# before you start the loop, you might want to check if the channels are right
# this shows what input (from controller or other source) is mapped to what PWM board output.
pwm.print_input_mappings() # this prints out the input mappings

# sleep a bit before starting the loop (so you have time to read the console output)
sleep(5)


# Initialize the Xbox controller
controller = joystick_module.XboxController()


# endless loop
while True:

    # generate random value between -1 and 1
    #value1 = random.uniform(-1, 1)
    #value2 = random.uniform(-1, 1)

    #random_value_list = [value1, value2]


    # read all the values from the controller (if you have one)
    values = controller.read()

    # check the values for debugging
    #print(values)

    # take the value we want to use
    the_value_we_want_to_give1 = values['LeftJoystickY']
    the_value_we_want_to_give2 = values['RightJoystickY']


    # create a list from the wanted values
    value_list = [the_value_we_want_to_give1, the_value_we_want_to_give2]

    # update the PWM controller with the list.
    pwm.update_values(value_list)


    sleep(1.0)