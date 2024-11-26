# this file contains various example scripts that help you understand how to use the joystick_module.py file

# import modules
from control_modules import joystick_module
from time import sleep

# init the controller
controller = joystick_module.XboxController()


# basic read function
def read_joystick():
    # read the controller values
    # this contains channel name and the corresponding value
    controller_values = controller.read()
    print(f"raw values: {controller_values}")

# read only the values, and not the channel names
def read_joystick_values_only():
    # this contains channel name and the corresponding value
    controller_values = controller.read()

    # get the values only
    values = list(controller_values.values())
    print(f"raw values, naming removed: {values}")

# example of mapping the values to a list
# this is a simple way, but may not be usable in all cases
def place_joystick_values():
    # read the controller values with names
    controller_values = controller.read()

    # place the values directly into the right places. Note that the order is important (fixed index).
    mapped_values = [
        controller_values['LeftJoystickY'],     # first in index, so 0
        controller_values['LeftJoystickX'],     # 1
        controller_values['RightJoystickY'],    # 2
        controller_values['RightJoystickX'],    # 3
        controller_values['LeftTrigger'],       # 4
        controller_values['RightTrigger'],      # 5
        controller_values['A']                  # 6
        # You can see all the available channels in the joystick_module.py file
    ]

    print(f"mapped values (fixed index): {mapped_values}")

# a more flexible way to map the values
# create a mapping to reorder values as needed
def read_and_map_joystick():
    # create a mapping to reorder values as needed
    # the numbers represent the position in the final list where you want each value. You can also change the order as you like.
    mapping_dict = {
        'LeftJoystickY': 0,
        'LeftJoystickX': 1,
        'RightJoystickY': 2,
        'RightJoystickX': 3,
        'LeftTrigger': 4,
        'RightTrigger': 5,
        'A': 7, # indexes flipped here for example
        'B': 6, # indexes flipped here for example

        # add more mappings as needed. You can see all the available channels in the joystick_module.py file
    }

    # read the controller values
    controller_values = controller.read()

    # create a list with the correct size
    mapped_values = [0] * len(mapping_dict)

    # map each value to its desired position
    for control_name, desired_index in mapping_dict.items():
        mapped_values[desired_index] = controller_values[control_name]

    print(f"mapped values (dict_mapping): {mapped_values}")


# example of how to apply a deadzone to a list of values
# this would usually be applied to the analog joystick values
def apply_deadzone():

    deadzone = 0.20 # 20% deadzone from center

    # read the controller values with names
    controller_values = controller.read()

    # place the values directly into the right places. Note that the order is important (fixed index).
    mapped_values = [
        controller_values['LeftJoystickY'],   # first in index, so 0
        controller_values['LeftJoystickX'],   # 1
        controller_values['RightJoystickY'],  # 2
        controller_values['RightJoystickX'],  # 3
        # You can see all the available channels in the joystick_module.py file
    ]

    # apply the deadzone to the mapped values
    for i, value in enumerate(mapped_values):
        if abs(value) < deadzone:
            mapped_values[i] = 0 # set current reading to 0 if it is within the deadzone

    print(f"mapped values with deadzone: {mapped_values}")



if __name__ == '__main__':
    # uncomment the function you want to test here!
    while True:

        # read_joystick()
        # read_joystick_values_only()
        place_joystick_values()
        # read_and_map_joystick()
        sleep(0.2)