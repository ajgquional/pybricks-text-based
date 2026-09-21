"""
Zigzag Movement on an Actual SPIKE Prime Robot

This program demonstrates how a loop can produce alternating
behavior. The robot moves forward and alternates between
left and right turns to create a zigzag path.
"""

from pybricks.hubs import PrimeHub
from pybricks.parameters import Icon, Port
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.tools import wait


WHEEL_DIAMETER = 56  # Diameter of each wheel in millimeters.
AXLE_TRACK = 152  # Distance between the wheels in millimeters.
MOVE_DISTANCE = 250  # Distance traveled per zigzag segment.
TURN_ANGLE = 45  # Angle used for each zigzag turn.
SEGMENTS = 6  # Number of zigzag segments.
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

print("Zigzag demonstration started.")
hub.display.icon(Icon.PLAY)  # Show that the program is starting.
wait(PAUSE_TIME)

for segment in range(SEGMENTS):
    print("Segment:", segment + 1)
    hub.display.char(str(segment + 1))  # Show the segment number.

    robot.straight(MOVE_DISTANCE)  # Move forward before each turn.
    wait(PAUSE_TIME)

    if segment % 2 == 0:
        hub.display.char("R")  # Show a right-turn indicator.
        robot.turn(TURN_ANGLE)  # Turn one direction on even segments.
    else:
        hub.display.char("L")  # Show a left-turn indicator.
        robot.turn(-TURN_ANGLE)  # Turn the opposite direction.

    wait(PAUSE_TIME)

robot.stop()  # Make sure the robot is stopped.

print("Zigzag demonstration finished.")
hub.display.icon(Icon.HAPPY)  # Show that the program is complete.
wait(1000)
hub.display.off()  # Clear the light matrix.