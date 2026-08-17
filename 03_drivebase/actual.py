"""
DriveBase Movement on an Actual SPIKE Prime Robot

This program demonstrates how to create a two-wheel DriveBase
and control the robot's basic movement. The robot moves forward,
turns, moves backward, and then stops.

The SPIKE Prime light matrix displays a simple indicator for each
movement so that the robot's current action is easy to observe.
"""

from pybricks.hubs import PrimeHub
from pybricks.parameters import Icon, Port
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.tools import wait


WHEEL_DIAMETER = 56  # Diameter of each wheel in millimeters.
AXLE_TRACK = 152  # Distance between the two wheels in millimeters.
MOVE_DISTANCE = 500  # Distance traveled in millimeters.
TURN_ANGLE = 90  # Turning angle in degrees.
PAUSE_TIME = 500  # Pause between actions in milliseconds.

hub = PrimeHub()  # Create an object representing the SPIKE Prime hub.

left_motor = Motor(Port.A)  # Create the left drive motor.
right_motor = Motor(Port.B)  # Create the right drive motor.

robot = DriveBase(
    left_motor,
    right_motor,
    wheel_diameter=WHEEL_DIAMETER,
    axle_track=AXLE_TRACK,
)  # Create the two-wheel robot drive base.

print("DriveBase demonstration started.")
hub.display.icon(Icon.PLAY)  # Show that the program is starting.
wait(PAUSE_TIME)

print("Moving forward.")
hub.display.icon(Icon.UP)  # Show the forward movement indicator.
robot.straight(MOVE_DISTANCE)  # Move forward by 500 millimeters.

hub.display.off()  # Clear the display during the pause.
wait(PAUSE_TIME)

print("Turning.")
hub.display.char("R")  # Display R to indicate a right turn.
robot.turn(TURN_ANGLE)  # Turn the robot 90 degrees.

hub.display.off()  # Clear the display during the pause.
wait(PAUSE_TIME)

print("Moving backward.")
hub.display.icon(Icon.DOWN)  # Show the backward movement indicator.
robot.straight(-MOVE_DISTANCE)  # Move backward by 500 millimeters.

hub.display.off()  # Clear the display during the pause.
wait(PAUSE_TIME)

robot.stop()  # Make sure the drive base is stopped.

print("DriveBase demonstration finished.")
hub.display.icon(Icon.HAPPY)  # Show that the program is complete.
wait(1000)
hub.display.off()  # Clear the light matrix.