"""
Square Movement on an Actual SPIKE Prime Robot

This program demonstrates how a for loop can repeat a sequence
of movements. The robot moves forward and turns four times
to trace a square.
"""

from pybricks.hubs import PrimeHub
from pybricks.parameters import Icon, Port
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.tools import wait


WHEEL_DIAMETER = 56  # Diameter of each wheel in millimeters.
AXLE_TRACK = 152  # Distance between the wheels in millimeters.
SIDE_LENGTH = 300  # Length of each side of the square in millimeters.
TURN_ANGLE = 90  # Turning angle at each corner in degrees.
NUMBER_OF_SIDES = 4  # Number of sides in a square.
PAUSE_TIME = 300  # Pause between movements in milliseconds.

hub = PrimeHub()  # Create an object representing the SPIKE Prime hub.

left_motor = Motor(Port.A)  # Create the left drive motor.
right_motor = Motor(Port.B)  # Create the right drive motor.

robot = DriveBase(
    left_motor,
    right_motor,
    wheel_diameter=WHEEL_DIAMETER,
    axle_track=AXLE_TRACK,
)  # Create the robot drive base.

print("Square demonstration started.")
hub.display.icon(Icon.PLAY)  # Show that the program is starting.
wait(PAUSE_TIME)

for side in range(NUMBER_OF_SIDES):
    print("Side:", side + 1)
    hub.display.char(str(side + 1))  # Show the current side number.

    robot.straight(SIDE_LENGTH)  # Move along one side.
    wait(PAUSE_TIME)

    hub.display.char("R")  # Show that the robot is about to turn.
    robot.turn(TURN_ANGLE)  # Turn toward the next side.
    wait(PAUSE_TIME)

robot.stop()  # Make sure the robot is stopped.

print("Square demonstration finished.")
hub.display.icon(Icon.HAPPY)  # Show that the program is complete.
wait(1000)
hub.display.off()  # Clear the light matrix.