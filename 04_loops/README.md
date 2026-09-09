# 🔁 Lesson 4: Loops

This lesson introduces loops as a way to repeat robot actions without writing the same commands multiple times.

The activities focus on `for` loops and show how repetition can be used for movement patterns and simple robot behaviors.

## 📁 Files

* `simulator_repeat_forward.py` — repeats the same forward movement
* `simulator_square.py` — moves the robot in a square
* `simulator_zigzag.py` — creates an alternating zigzag path
* `simulator_increasing_distance.py` — increases the movement distance each repetition
* `simulator_patrol.py` — repeatedly moves forward and backward

## 🧠 Concepts Introduced

* `for` loops
* `range()`
* Repeating robot actions
* Loop variables
* Using loop variables in calculations
* Repeating multiple commands as one pattern
* Applying loops to practical robot behaviors

## ▶️ Running the Simulator Programs

1. Open the [GearsBot Simulator](https://gears.aposteriori.com.sg/).
2. Select a suitable two-wheel robot.
3. Open the Python editor.
4. Copy and paste one of the simulator scripts.
5. Run the program.
6. Observe how the loop changes the robot's movement.

## 🧪 Demo Progression

### 1. Repeat Forward

Introduces the basic structure of a `for` loop by repeating the same forward movement several times.

### 2. Square

Repeats a sequence of two commands:

```python
robot.straight(SIDE_LENGTH)
robot.turn(TURN_ANGLE)
```

This allows the robot to trace a square.

### 3. Zigzag

Alternates between left and right turns to create a zigzag pattern.

This demo also provides an early example of changing behavior during different loop iterations.

### 4. Increasing Distance

Uses the loop variable to calculate a different movement distance for every repetition.

Example:

```python
move_distance = BASE_DISTANCE * repetition
```

### 5. Patrol

Uses a loop to create a simple practical robot behavior by repeatedly moving forward and backward along the same path.

## 🧪 Try It Yourself

Modify the programs to:

* Change the number of repetitions
* Make a larger or smaller square
* Create a sharper or wider zigzag
* Change how quickly the movement distance increases
* Increase the number of patrol rounds
* Create your own repeating movement pattern
