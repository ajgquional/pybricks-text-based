"""
DriveBase Movement in the GearsBot Simulator

This program demonstrates how to create a two-wheel DriveBase
and control the robot's basic movement. The robot moves forward,
turns, moves backward, and then stops.
"""

from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait


WHEEL_DIAMETER = 56  # Diameter of each wheel in millimeters.
AXLE_TRACK = 152  # Distance between the two wheels in millimeters.
MOVE_DISTANCE = 500  # Distance traveled in millimeters.
TURN_ANGLE = 90  # Turning angle in degrees.
PAUSE_TIME = 500  # Pause between actions in milliseconds.

left_motor = Motor(Port.A)  # Create the left drive motor.
right_motor = Motor(Port.B)  # Create the right drive motor.

robot = DriveBase(
    left_motor,
    right_motor,
    wheel_diameter=WHEEL_DIAMETER,
    axle_track=AXLE_TRACK,
)  # Create the two-wheel robot drive base.

print("DriveBase demonstration started.")

robot.straight(MOVE_DISTANCE)  # Move forward by 500 millimeters.
wait(PAUSE_TIME)  # Pause before the next movement.

robot.turn(TURN_ANGLE)  # Turn the robot 90 degrees.
wait(PAUSE_TIME)  # Pause before the next movement.

robot.straight(-MOVE_DISTANCE)  # Move backward by 500 millimeters.
wait(PAUSE_TIME)  # Pause before finishing.

robot.stop()  # Make sure the drive base is stopped.

print("DriveBase demonstration finished.")