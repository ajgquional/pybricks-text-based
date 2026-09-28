"""
Maze Map Challenge from green to yellow (seed 93)

This program allows the robot to move from the green base up to the 
yellow base in the Maze Map World (seed 93). This Maze Map seed 
facilitates a good environment for practicing the use of for loops 
to aid in forming complex robot behaviors.
"""

from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait
import time # optional, for counting elapsed time

# configuration
WHEEL_DIAMETER = 56  # Diameter of each wheel in millimeters.
AXLE_TRACK = 152  # Distance between the wheels in millimeters.
MOVE_DISTANCE = 400  # Distance traveled per repetition in millimeters.
TURN_ANGLE = 90 # Angle by which the robot has to turn
PAUSE_TIME = 300  # Pause between movements in milliseconds.

left_motor = Motor(Port.A)  # Create the left drive motor.
right_motor = Motor(Port.B)  # Create the right drive motor.

robot = DriveBase(
    left_motor,
    right_motor,
    wheel_diameter=WHEEL_DIAMETER,
    axle_track=AXLE_TRACK,
)  # Create the robot drive base.

# controlling the settings of the robot for better controllability
robot.settings(straight_speed=200, straight_acceleration=500, turn_rate=100, turn_acceleration=200)

# straight_speed: Measured in millimeters per second (mm/s)
# straight_acceleration: Measured in mm/s²
# turn_rate: Measured in degrees per second (deg/s)
# turn_acceleration: Measured in deg/s²

print("Motion start.")
start_time = time.time() # optional, for counting elapsed time

for _ in range(2):
    robot.straight(MOVE_DISTANCE)
    robot.turn(TURN_ANGLE)
    robot.straight(410)
    robot.turn(-TURN_ANGLE)
    
wait(PAUSE_TIME) # pause before traversing next part of the maze

for _ in range(2):
    robot.straight(-MOVE_DISTANCE)
    robot.turn(TURN_ANGLE)
    robot.straight(MOVE_DISTANCE)
    robot.turn(-TURN_ANGLE)
    
wait(PAUSE_TIME) # pause before traversing next part of the maze

for _ in range(3):
    robot.straight(320) # reduced move distance
    robot.turn(TURN_ANGLE)
    
robot.straight(-50) # moving backward before turning
robot.turn(185) # adjusted 180-degree rotation
wait(PAUSE_TIME) # pause before traversing next part of the maze

robot.straight(MOVE_DISTANCE)
robot.turn(-TURN_ANGLE)

for _ in range(3):
    robot.straight(350) # adjusted straight movement
    robot.turn(TURN_ANGLE)
    
robot.stop()

end_time = time.time()
execution_time = end_time - start_time
print(f"Goal reached. Time elapsed: {execution_time:.6f} s")