"""
Competition Time Strategy in the GearsBot Simulator

This program changes the robot's local drive speed depending on
the simulated amount of time remaining in a competition match.
"""

from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait


WHEEL_DIAMETER = 56  # Diameter of each wheel in millimeters.
AXLE_TRACK = 152  # Distance between the wheels in millimeters.
DRIVE_TIME = 1500  # Driving time in milliseconds.

TIME_REMAINING = 35  # Simulated remaining match time in seconds.

left_motor = Motor(Port.A)  # Create the left drive motor.
right_motor = Motor(Port.B)  # Create the right drive motor.

robot = DriveBase(
    left_motor,
    right_motor,
    wheel_diameter=WHEEL_DIAMETER,
    axle_track=AXLE_TRACK,
)  # Create the robot drive base.

if TIME_REMAINING > 60:
    drive_speed = 200  # Use a controlled speed early in the match.
    strategy = "Normal"
elif TIME_REMAINING > 20:
    drive_speed = 300  # Increase speed during the middle phase.
    strategy = "Fast"
else:
    drive_speed = 400  # Use maximum speed near the end.
    strategy = "Final Push"

print("Time remaining:", TIME_REMAINING, "seconds")
print("Strategy:", strategy)
print("Drive speed:", drive_speed, "mm/s")

robot.drive(drive_speed, 0)  # Drive using the selected strategy speed.
wait(DRIVE_TIME)  # Continue for a fixed amount of time.
robot.stop()  # Stop the robot.