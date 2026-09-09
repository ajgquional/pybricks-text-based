"""
Square Movement in the GearsBot Simulator

This program demonstrates how a for loop can repeat a sequence
of movements. The robot moves forward and turns four times
to trace a square.
"""

from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait


WHEEL_DIAMETER = 56  # Diameter of each wheel in millimeters.
AXLE_TRACK = 152  # Distance between the wheels in millimeters.
SIDE_LENGTH = 400  # Length of each side of the square in millimeters.
TURN_ANGLE = 95  # Turning angle at each corner in degrees.
NUMBER_OF_SIDES = 4  # Number of sides in a square.
PAUSE_TIME = 300  # Pause between movements in milliseconds.

left_motor = Motor(Port.A)  # Create the left drive motor.
right_motor = Motor(Port.B)  # Create the right drive motor.

robot = DriveBase(
    left_motor,
    right_motor,
    wheel_diameter=WHEEL_DIAMETER,
    axle_track=AXLE_TRACK,
)  # Create the robot drive base.

print("Square demonstration started.")

for side in range(NUMBER_OF_SIDES):
    print("Side:", side + 1)
    robot.straight(SIDE_LENGTH)  # Move along one side.
    wait(PAUSE_TIME)
    robot.turn(TURN_ANGLE)  # Turn toward the next side.
    wait(PAUSE_TIME)

robot.stop()  # Make sure the robot is stopped.

print("Square demonstration finished.")