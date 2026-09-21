# 🔁 Lesson 4: Loops

This lesson introduces loops as a way to repeat robot actions without writing the same commands multiple times.

The activities focus on `for` loops and show how repetition can be used for movement patterns and simple robot behaviors.

## 📁 Files

* `simulator_repeat_forward.py` — repeats the same forward movement
* `actual_repeat_forward.py` — physical SPIKE Prime version
* `simulator_square.py` — moves the robot in a square
* `actual_square.py` — physical SPIKE Prime version
* `simulator_zigzag.py` — creates an alternating zigzag path
* `actual_zigzag.py` — physical SPIKE Prime version
* `simulator_increasing_distance.py` — increases the movement distance each repetition
* `actual_increasing_distance.py` — physical SPIKE Prime version
* `simulator_patrol.py` — repeatedly moves forward and backward
* `actual_patrol.py` — physical SPIKE Prime version

## 🧠 Concepts Introduced

* `for` loops
* `range()`
* Repeating robot actions
* Loop variables
* Using loop variables in calculations
* Repeating multiple commands as one pattern
* Alternating behavior inside a loop
* Applying loops to practical robot behaviors

## ▶️ Running the Simulator Programs

1. Open the [GearsBot Simulator](https://gears.aposteriori.com.sg/).
2. Select a suitable two-wheel robot.
3. Open the Python editor.
4. Copy and paste one of the `simulator_*.py` scripts.
5. Run the program.
6. Observe how the loop changes the robot's movement.

## 🧱 Running the Actual Programs

1. Connect the drive motors to the SPIKE Prime hub.
2. Check that the motor ports in the selected `actual_*.py` script match the physical robot.
3. Open [Pybricks Code](https://code.pybricks.com/).
4. Connect the SPIKE Prime hub.
5. Copy and paste the selected actual script.
6. Place the robot in an open testing area.
7. Run the program.

> The actual robot may require different wheel diameter, axle track, turn angle, or motor-direction values.

## 🧪 Demo Progression

### 1. Repeat Forward

Introduces the basic structure of a `for` loop by repeating the same movement several times.

```python
for repetition in range(REPETITIONS):
    robot.straight(MOVE_DISTANCE)
```

### 2. Square

Repeats a forward movement and turn to trace a square.

```python
for side in range(NUMBER_OF_SIDES):
    robot.straight(SIDE_LENGTH)
    robot.turn(TURN_ANGLE)
```

### 3. Zigzag

Uses the loop number to alternate between left and right turns.

This demo also provides an early example of conditional behavior inside a loop.

### 4. Increasing Distance

Uses the loop variable in a calculation so that the robot moves farther during every repetition.

```python
move_distance = BASE_DISTANCE * repetition
```

### 5. Patrol

Uses a loop to create a simple practical robot behavior by repeatedly moving forward and backward along the same path.

## 💡 Physical Robot Feedback

The `actual_*.py` programs use the SPIKE Prime light matrix to provide simple visual feedback.

Depending on the demo, the hub may display:

* the current repetition number
* the current side or segment number
* turning indicators
* a start icon
* a completion icon

This makes it easier to observe which part of the loop is currently running.

## 🧪 Try It Yourself

Modify the programs to:

* Change the number of repetitions
* Make a larger or smaller square
* Create a sharper or wider zigzag
* Change how quickly the movement distance increases
* Increase the number of patrol rounds
* Change the LED indicators
* Create your own repeating movement pattern
