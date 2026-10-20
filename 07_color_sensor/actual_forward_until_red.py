
"""
Forward Until Red - Actual LEGO SPIKE Prime

The robot moves forward until its Color Sensor detects red.

Place a red strip of paper or tape across the robot's path.

Hardware:
    Left Motor: Port A
    Right Motor: Port B
    Color Sensor: Port C
"""

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Port, Color
from pybricks.robotics import DriveBase
from pybricks.tools import wait


WHEEL_DIAMETER = 56  # Wheel diameter in millimeters.
AXLE_TRACK = 152  # Distance between wheels in millimeters.
DRIVE_SPEED = 200  # Forward speed in millimeters per second.

hub = PrimeHub()  # Initialize the SPIKE Prime Hub.
left_motor = Motor(Port.A)  # Initialize the left motor.
right_motor = Motor(Port.B)  # Initialize the right motor.
color_sensor = ColorSensor(Port.C)  # Initialize the Color Sensor.

robot = DriveBase(
    left_motor,
    right_motor,
    wheel_diameter=WHEEL_DIAMETER,
    axle_track=AXLE_TRACK,
)

print("Mission: Forward Until Red")
print("Searching for the red stopping zone.")

hub.light.on(Color.GREEN)  # Green indicates forward movement.
robot.drive(DRIVE_SPEED, 0)  # Drive forward continuously.

while color_sensor.color() != Color.RED:
    wait(20)  # Keep checking the Color Sensor.

robot.stop()  # Stop when red is detected.
hub.light.on(Color.RED)  # Red indicates mission completion.

print("Red detected!")
print("Mission completed.")
