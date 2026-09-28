# 🔀 Lesson 5: Conditionals

This lesson introduces Python conditionals as a way for the robot to make decisions based on values in the program.

The activities focus on `if`, `elif`, and `else` statements without using sensors yet.

## 📁 Files

- `simulator_speed_mode.py` — selects a driving speed based on the chosen mode
- `simulator_competition_time_strategy.py` — changes behavior based on simulated time remaining
- `simulator_even_odd_turns.py` — combines loops and conditionals to alternate turning behavior
- `simulator_route_choice.py` — selects a movement route based on a programmed condition

## 🧠 Concepts Introduced

- `if`
- `elif`
- `else`
- Comparison operators
- Boolean conditions
- Decision-making in robot programs
- Combining conditionals with loops
- Selecting different movement behaviors
- Changing `robot.drive()` speed and turn rate locally

## ▶️ Running the Simulator Programs

1. Open the [GearsBot Simulator](https://gears.aposteriori.com.sg/).
2. Select a suitable two-wheel robot.
3. Open the Python editor.
4. Copy and paste one of the `simulator_*.py` scripts.
5. Run the program.
6. Change the condition values and observe how the robot's behavior changes.

## 🧪 Demo Progression

### 1. Speed Mode

Uses `if`, `elif`, and `else` to select a local driving speed.

```python
if SPEED_MODE == "slow":
    drive_speed = 100
elif SPEED_MODE == "medium":
    drive_speed = 250
else:
    drive_speed = 400
```

### 2. Competition Time Strategy

Uses a simulated `TIME_REMAINING` value to select different robot behavior.

This demonstrates how a robot program can change its strategy depending on its current state.

### 3. Even/Odd Turns

Combines a loop with a conditional.

The robot checks whether the current repetition is even or odd and changes its turn direction.

```python
if repetition % 2 == 0:
    turn_rate = TURN_RATE
else:
    turn_rate = -TURN_RATE
```

### 4. Route Choice

Uses conditionals to choose between different movement routes.

This demonstrates how a condition can control an entire sequence of robot actions.

## 🤖 Decision-Making Without Sensors

In this lesson, the conditions are based on values already stored in the program.

For example:

```python
SPEED_MODE = "medium"
TIME_REMAINING = 35
ROUTE = "left"
```

The robot is making decisions, but it is not yet sensing its environment.

Later lessons will replace some of these programmed values with real sensor readings.

The same basic structure will remain:

```text
Get information
→ Check a condition
→ Choose an action
```

## 🧪 Try It Yourself

Modify the programs to:

- Add a new speed mode
- Change the time thresholds
- Reverse the even and odd turning directions
- Add another possible route
- Combine two conditions using `and` or `or`
- Create your own conditional robot behavior