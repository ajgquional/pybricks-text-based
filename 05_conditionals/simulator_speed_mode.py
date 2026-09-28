"""
Speed Mode in the GearsBot Simulator

This program demonstrates how conditionals can select different
local drive speeds. The selected speed is passed directly to
robot.drive().
"""

from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait


WHEEL_DIAMETER = 56  # Diameter of each wheel in millimeters.
AXLE_TRACK = 152  # Distance between the wheels in millimeters.
DRIVE_TIME = 2000  # Driving time in milliseconds.

SPEED_MODE = "medium"  # Change to "slow", "medium", or "fast".

left_motor = Motor(Port.A)  # Create the left drive motor.
right_motor = Motor(Port.B)  # Create the right drive motor.

robot = DriveBase(
    left_motor,
    right_motor,
    wheel_diameter=WHEEL_DIAMETER,
    axle_track=AXLE_TRACK,
)  # Create the robot drive base.

if SPEED_MODE == "slow":
    drive_speed = 100  # Slow speed in millimeters per second.
elif SPEED_MODE == "medium":
    drive_speed = 250  # Medium speed in millimeters per second.
elif SPEED_MODE == "fast":
    drive_speed = 400  # Fast speed in millimeters per second.
else:
    drive_speed = 150  # Use a safe default speed.
    print("Unknown speed mode. Using default speed.")

print("Selected mode:", SPEED_MODE)
print("Drive speed:", drive_speed, "mm/s")

robot.drive(drive_speed, 0)  # Drive straight at the selected speed.
wait(DRIVE_TIME)  # Continue driving for the selected amount of time.
robot.stop()  # Stop the robot.