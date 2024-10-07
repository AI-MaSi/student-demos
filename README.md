# Masi Control System for Students

This is a simplified example of a Masi control system, designed for students to learn how to use Masi-project systems. It's built around a simplified Raspberry Pi stack for control and sensor reading.

## Files:

1. `main.py`: The main script that ties everything together. It initializes the PWM controller, ADC sensors, and Xbox controller, and runs the main control loop.

2. `PWM_controller.py`: Handles PWM outputs for servos and other devices. It can work with real hardware or in simulation mode.

3. `ADC_sensors.py`: Manages analog sensor readings. It supports various filtering options and can also run in simulation mode.

4. `joystick_module.py`: Provides support for Xbox controller input.

5. `channel_configs.yaml`: Configuration file for PWM channels. It defines servo settings, input/output mappings, and other PWM-related parameters.

6. `sensor_configs.yaml`: Configuration file for ADC sensors. It includes ADC settings, filter configurations, and sensor calibration values.

## Configuration:

- `channel_configs.yaml`: Use this file to set up your PWM channels. You can define servo properties, input/output mappings, and control parameters.

- `sensor_configs.yaml`: This file configures your ADC sensors and filter settings. It includes ADC board setup, filter types, and sensor-specific calibrations.

These YAML files allow you to easily customize the system without changing the main code, making it great for experimentation and learning.

## Usage:

1. Make sure you have the required libraries installed (see `main.py` for details).
2. Customize `channel_configs.yaml` and `sensor_configs.yaml` to match your setup.
3. Run `main.py` to start the system.

Note: This system can run in simulation mode, allowing you to test without actual hardware connected to your Raspberry Pi.

Have fun experimenting with your Masi control system and learning about control systems and sensor integration!
