# this file is an example of how to use the controller module to read the controller values and process them for further use.
# use this as a base for your own control logic of the tracked vehicle.

from control_modules import joystick_module
import time

# Initialize Xbox controller
controller = joystick_module.XboxController()

# Controller mapping - defines which channels we want to use and in which order
controller_mapping = {
    'LeftJoystickX': 0,
    'LeftJoystickY': 1,
    'RightJoystickX': 2,
    'RightJoystickY': 3,
    'LeftTrigger': 4,
    'RightTrigger': 5,
    'LeftBumper': 6,
    'RightBumper': 7,
    'A': 8,
    'B': 9,
    'X': 10,
    'Y': 11,
    # please see the joystick_module.py file for the full list of available channels
}


def read_controller():
    """
    Read, map and return controller values
    """
    controller_values = controller.read()
    mapped_values = [controller_values[channel] for channel in controller_mapping]
    return mapped_values


def _process_joystick(value, deadzone=0.20): # 20% deadzone
    """
    Process joystick input with deadzone

    process_all_inputs calls this function for each joystick.
    """
    if abs(value) < deadzone:
        return 0.0  # set stick value to 0 if within deadzone
    return value


def _process_pedal(trigger_value, bumper_value, deadzone=0.05):
    """
    Process trigger input with deadzone. Flip the value if corresponding bumper is held.
    Idea is to be able to drive tracked vehicles with triggers acting as pedals, and with possibility to reverse.

    Typically, the Xbox controller trigger values are in the range -1..1, where -1 is fully pressed and 1 is fully released.
    This function converts the trigger value to a 0..1 range and applies a deadzone.

    process_all_inputs calls this function for each trigger.
    """
    # Add deadzone to triggers
    if abs(trigger_value) < deadzone:
        return 0.0

    # Convert trigger value to 0..1 range. Midpoint is moved to the start of the trigger
    pedal_value = (trigger_value + 0.5) / 2

    # Flip the trigger value if bumper is held
    if bumper_value:
        pedal_value = -pedal_value

    return pedal_value


def process_all_inputs(raw_values):
    """
    Process all controller inputs with appropriate processing functions.
    This function calls the appropriate processing function for each input channel.
    """
    processed_values = []

    # go through all the raw values and process them
    for i, value in enumerate(raw_values):
        channel_name = list(controller_mapping.keys())[i]

        # Apply appropriate processing based on input type

        # Check if the channel name has the word 'Trigger' in it
        if 'Trigger' in channel_name: # this gets us the trigger value from the raw_values list

            # Find corresponding 'Bumper' value, by replacing 'Trigger' with 'Bumper' in the channel name.
            # this way we can match left and right trigger with left and right bumper
            bumper_index = controller_mapping[channel_name.replace('Trigger', 'Bumper')] # this gets us the right bumper index

            # Process the trigger value with matched bumper value, and add it to the processed_values list
            processed_value = _process_pedal(value, raw_values[bumper_index])

        # check if the channel name has the word 'Joystick' in it
        elif 'Joystick' in channel_name:
            # Process joystick value, and add it to the processed_values list
            processed_value = _process_joystick(value)

        # check if the channel name has other words than 'Trigger' or 'Joystick' in it (basically buttons in this case)
        else:
            # Buttons output 0 or 1, so no processing needed. Add them to the list as they are.
            processed_value = value

        # Add the processed value to the list
        processed_values.append(processed_value)

    # Return the processed values for further use
    return processed_values

#example function
def calculate_multiplier(processed_values):


    #set the multiplier to 2.0 if A button is held
    if processed_values[8]: # button A from the list
        multiplier = 2.0

    #set the multiplier to 10 if B button is held
    elif processed_values[9]: # button B from the list
        multiplier = 10.0

    #set the multiplier to 1.0 if no buttons are held
    else:
        multiplier = 1.0

    return multiplier

# example function
def spin_wheel(processed_value, multiplier):
    # simple example function to spin a wheel at a certain speed
    rpm = 360 * multiplier * processed_value  # we use controller value for the speed control
    print(f"Wheel is spinning at RPM: {rpm}")



# main loop
def main():
    running = True   # Main loop running flag. For example
    try:
        while running:
            # for safety, you could check if the controller is connected here. Skipping that for simplicity now.


            # Read controller to get the mapped values
            raw_values = read_controller()

            #print(f"raw mapped values: {raw_values}")

            # Process inputs
            processed_values = process_all_inputs(raw_values) # you can skip this if you don't need any processing
            # looks like this: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 0, 0, 0]. The indexing matches the controller_mapping!



            # Now you could use the processed values for your control logic

            # example, change speed multiplier with button presses:
            speed_multiplier = calculate_multiplier(processed_values) # call example function


            # example, use the RightTrigger value to spin imaginary wheel:
            spin_wheel(processed_values[5], speed_multiplier) # call example function


            # example, quit the loop if button Y is pressed
            if processed_values[11]:
                running = False
                print("Button Y pressed, stopping the loop")


            # Print values for debugging
            #print(f"Processed values: {processed_values}")


            time.sleep(0.1)  # 10Hz update rate

    except KeyboardInterrupt:
        print("Program terminated by user")
    finally:
        # stop the controller monitoring thread
        controller.stop_monitoring()
    print("Program terminated.")


if __name__ == "__main__":
    main()