"""
Repeat Forward Movement on an Actual SPIKE Prime Robot

This program demonstrates a basic for loop by moving the robot
forward the same distance several times.
"""

from pybricks.hubs import PrimeHub
from pybricks.parameters import Icon, Port
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.tools import wait


WHEEL_DIAMETER = 56  # Diameter of each wheel in millimeters.
AXLE_TRACK = 152  # Distance between the wheels in millimeters.
MOVE_DISTANCE = 200  # Distance traveled per repetition in millimeters.
REPETITIONS = 4  # Number of times the movement is repeated.
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

print("Repeat forward demonstration started.")
hub.display.icon(Icon.PLAY)  # Show that the program is starting.
wait(PAUSE_TIME)

for repetition in range(REPETITIONS):
    print("Repetition:", repetition + 1)
    hub.display.char(str(repetition + 1))  # Show the current repetition.
    robot.straight(MOVE_DISTANCE)  # Move forward once.
    wait(PAUSE_TIME)  # Pause before repeating.

robot.stop()  # Make sure the robot is stopped.

print("Repeat forward demonstration finished.")
hub.display.icon(Icon.HAPPY)  # Show that the program is complete.
wait(1000)
hub.display.off()  # Clear the light matrix.