# 🧩 Lesson 6: Functions

This lesson introduces functions as a way to organize robot behaviors into reusable skills and complete missions.

The main activity uses a **Mission Selector** program where different functions are called depending on the selected mission.

## 📁 Files

- `simulator_mission_selector.py` — demonstrates reusable robot functions and mission selection in GearsBot

## 🧠 Concepts Introduced

- Defining functions with `def`
- Calling functions
- Function parameters
- Reusing functions
- Combining functions with loops
- Combining functions with conditionals
- Returning values with `return`
- Building complex robot behaviors from simpler skills

## ▶️ Running the Simulator Program

1. Open the [GearsBot Simulator](https://gears.aposteriori.com.sg/).
2. Select a suitable two-wheel robot.
3. Open the Python editor.
4. Copy and paste `simulator_mission_selector.py`.
5. Change the `MISSION` variable.
6. Run the program.
7. Observe which function is executed.

## 🤖 Available Missions

### Forward

Uses a simple function with one parameter:

```python
move_forward(500)
```

### Square

Uses a function that combines:

- another function
- a parameter
- a loop

```python
drive_square(300)
```

### Patrol

Uses multiple parameters and repeated movement:

```python
patrol(400, 3)
```

The program also calculates the planned patrol distance using a function with a `return` value.

### Zigzag

Combines:

- parameters
- loops
- conditionals
- reusable movement functions

```python
zigzag(
    distance=250,
    turn_angle=45,
    segments=6,
)
```

## 🪜 Function Progression

The functions are arranged from simpler to more advanced examples:

```text
move_forward()
→ turn_robot()
→ drive_square()
→ patrol()
→ zigzag()
→ calculate_patrol_distance()
```

This demonstrates how larger robot behaviors can be built from smaller reusable skills.

## 🧪 Try It Yourself

Modify the program to:

- Change the mission parameters
- Add a new movement function
- Create a triangle mission
- Create a rectangle mission
- Add another patrol pattern
- Add a new option to the mission selector
- Create a function that returns another calculated value