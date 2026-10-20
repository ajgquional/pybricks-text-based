
"""
Forward Until Red - GearsBot Simulator

The robot drives forward until its color sensor detects red.

World:
    color_stop_world.json

Concepts:
    Color Sensor, while loop, conditionals, continuous movement.
"""

from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Color
from pybricks.robotics import DriveBase
from pybricks.tools import wait


WHEEL_DIAMETER = 56  # Wheel diameter in millimeters.
AXLE_TRACK = 152  # Distance between wheels in millimeters.
DRIVE_SPEED = 200  # Forward speed in millimeters per second.

left_motor = Motor(Port.A)  # Initialize the left motor.
right_motor = Motor(Port.B)  # Initialize the right motor.
color_sensor = ColorSensor(Port.S1)  # Initialize the color sensor.

robot = DriveBase(
    left_motor,
    right_motor,
    wheel_diameter=WHEEL_DIAMETER,
    axle_track=AXLE_TRACK,
)

print("Mission: Forward Until Red")
print("Searching for the red stopping zone...")

robot.drive(DRIVE_SPEED, 0)  # Drive forward continuously.

while color_sensor.color() != Color.RED:
    wait(20)  # Check the sensor every 20 milliseconds.

robot.stop()  # Stop when red is detected.

print("Red detected!")
print("Mission completed.")
