"""
Increasing Distance Movement on an Actual SPIKE Prime Robot

This program demonstrates how the loop variable can be used
in a calculation. The robot moves farther during each repetition.
"""

from pybricks.hubs import PrimeHub
from pybricks.parameters import Icon, Port
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.tools import wait


WHEEL_DIAMETER = 56  # Diameter of each wheel in millimeters.
AXLE_TRACK = 152  # Distance between the wheels in millimeters.
BASE_DISTANCE = 100  # Starting movement distance in millimeters.
REPETITIONS = 5  # Number of movements.
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

print("Increasing distance demonstration started.")
hub.display.icon(Icon.PLAY)  # Show that the program is starting.
wait(PAUSE_TIME)

for repetition in range(1, REPETITIONS + 1):
    move_distance = BASE_DISTANCE * repetition  # Increase each movement.

    print("Repetition:", repetition)
    print("Distance:", move_distance, "mm")

    hub.display.char(str(repetition))  # Show the current repetition.
    robot.straight(move_distance)  # Move using the calculated distance.
    wait(PAUSE_TIME)

robot.stop()  # Make sure the robot is stopped.

print("Increasing distance demonstration finished.")
hub.display.icon(Icon.HAPPY)  # Show that the program is complete.
wait(1000)
hub.display.off()  # Clear the light matrix.