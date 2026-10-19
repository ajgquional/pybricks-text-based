# 🎨 Lesson 7: Color Sensor

This lesson introduces the SPIKE Prime Color Sensor and its use in detecting colors and reflected light intensity.

Before starting the activities, we will test a custom GearsBot world to verify that the simulated color sensor can detect colored surfaces.

## 📁 Files

```text
07_color_sensor/
├── worlds/
│   └── color_test.png
├── simulator_test_color_sensor.py
└── README.md
```

The ground image is generated using `generate_world.py`, located in the repository's root directory.

## 🌍 Generating the Test World

From the repository's root directory, run:

```bash
python generate_world.py --preset color-test --width 1200 --height 800 --output 07_color_sensor/worlds/color_test.png
```

The resulting image contains three colored patches:

- 🔴 Red
- 🟢 Green
- 🔵 Blue

The surrounding white area serves as the background.

## 🚀 Loading the World in GearsBot

1. Open the [GearsBot Simulator](https://gears.aposteriori.com.sg/).
2. Open **Worlds → World Builder**.
3. Select the ground and locate its image URL setting (`imageURL`).
4. Enter the raw GitHub URL of the generated PNG:

   ```text
   https://raw.githubusercontent.com/ajgquional/pybricks-text-based/main/07_color_sensor/worlds/color_test.png
   ```

5. Adjust the ground dimensions and robot's starting position as needed.
6. Select a robot equipped with a downward-facing color sensor.

## 🧪 Testing the Color Sensor

1. Open `simulator_test_color_sensor.py`.
2. Check that the sensor port in the script matches the robot's color sensor port.
3. Copy the script into GearsBot's Python editor.
4. Position the robot so that its color sensor is over the white background.
5. Run the script and observe the console output.
6. Repeat the test over the red, green, and blue patches.

The script continuously prints the detected color and reflected light intensity.

### Expected Behavior

| Surface | Expected detected color |
|---|---|
| White background | White |
| Red patch | Red |
| Green patch | Green |
| Blue patch | Blue |

Exact readings may vary depending on the simulator's sensor implementation and world configuration.

## 📌 Notes

- Ensure that the color sensor faces the ground.
- The sensor must be positioned over the colored patch, not merely the robot's center.
- The PNG dimensions are measured in pixels, while robot movements use physical distance units.
- This initial test verifies the custom world before proceeding to more advanced sensor challenges.

## 🔜 Upcoming Activities

After the world has been verified, this lesson will introduce color-based actions, stopping at a red marker, color-controlled navigation, and basic line following.

Each activity will include scripts for both **GearsBot** and the **actual SPIKE Prime robot**.