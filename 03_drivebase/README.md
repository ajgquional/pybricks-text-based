# 🚗 Lesson 3: DriveBase Movement

This lesson introduces the `DriveBase` class, which allows two motors to work together as a mobile robot.

The program demonstrates:

- Creating left and right drive motors
- Creating a `DriveBase`
- Moving forward and backward
- Turning the robot
- Using wheel diameter and axle track
- Displaying movement indicators on the SPIKE Prime LED matrix

## 📁 Files

- `simulator.py` — runs in the GearsBot simulator
- `actual.py` — runs on an actual SPIKE Prime robot

## 🧠 Concepts Introduced

- `DriveBase`
- `robot.straight()`
- `robot.turn()`
- `robot.stop()`
- Wheel diameter
- Axle track
- Positive and negative movement distances
- Turning angles
- Coordinating two motors

## ▶️ Running the Simulator Version

1. Open the [GearsBot Simulator](https://gears.aposteriori.com.sg/).
2. Select a robot with two drive motors.
3. Open the Python editor.
4. Copy and paste the contents of `simulator.py`.
5. Run the program.
6. Observe the robot's movement.

## 🧱 Running the Actual Version

1. Connect the left and right drive motors to the SPIKE Prime hub.
2. Check that the motor ports in `actual.py` match the physical robot.
3. Open [Pybricks Code](https://code.pybricks.com/).
4. Connect the SPIKE Prime hub.
5. Copy and paste the contents of `actual.py`.
6. Place the robot in an open testing area.
7. Run the program.

> The physical robot may require different values for wheel diameter, axle track, and motor direction.

## 🧪 Try It Yourself

Modify the program to:

- Move a shorter or longer distance
- Turn 45°, 180°, or 360°
- Make the robot move in a square
- Change the order of the movements
- Experiment with different wheel diameter or axle track values
- Change the LED indicators shown during each movement