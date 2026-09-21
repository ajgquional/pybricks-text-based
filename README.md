# 🤖 Pybricks Text-Based Programming

Custom beginner-friendly Python scripts for learning **text-based Pybricks programming** using LEGO® Education SPIKE™ Prime.

Each lesson folder contains two script versions:

* `simulator.py` — for the online simulator
* `actual.py` — for an actual SPIKE Prime robot running Pybricks

The tutorial begins with basic motor control and gradually progresses toward sensors, autonomous robot behavior, RoboSports Double Tennis, and advanced device integration such as HuskyLens.

## 📁 Proposed Outline

* 01: First Program
* 02: Motor Control
* 03: Drivebase Movement
* 04: Loops
* 05: Conditions and Decisions (coming soon)
* 06: Functions (coming soon)
* 07: Color Sensor (coming soon)
* 08: Distance Sensor (coming soon)
* 09: Gyro and Orientation (coming soon)
* 10: Search and React (coming soon)
* 11: Timers and Match Logic (coming soon)
* 12: Double Tennis (coming soon)
* 13: HuskyLens Integration (coming soon)

> The structure may be adjusted as the tutorial progresses.

## 🌐 Simulator

The simulator activities use **GearsBot**, a free browser-based robotics simulator.

* [GearsBot Simulator](https://gears.aposteriori.com.sg/)
* [GearsBot Pybricks Tutorials](https://tutorials.aposteriori.com.sg/110-Pybricks-Basics/10-Introduction/10-Intro.html)

GearsBot commonly uses the older EV3-style Pybricks API, while an actual SPIKE Prime uses the current Powered Up API. Separate scripts are therefore provided for each platform.

## 🔗 References

### Pybricks

* [Pybricks Website](https://pybricks.com/)
* [Pybricks Code](https://code.pybricks.com/)
* [Pybricks Learning Resources](https://pybricks.com/learn/)
* [Pybricks Documentation](https://docs.pybricks.com/en/latest/)
* [SPIKE Prime Hub Documentation](https://docs.pybricks.com/en/latest/hubs/primehub.html)
* [Motor Documentation](https://docs.pybricks.com/en/latest/pupdevices/motor.html)
* [DriveBase Documentation](https://docs.pybricks.com/en/latest/robotics.html)
* [Pybricks Runner for VS Code](https://open-vsx.org/extension/AnandSingh/pybricks-runner)

### Relevant Competitions

* [Philippine Robot Olympiad](https://felta.ph/pro/download.html)
* [PRO 2025 RoboSports Double Tennis General Rules](https://felta.ph/pro/files/2025/PRO-2025-RoboSports-Double-Tennis-General-Rules.pdf)
* [IDE Series 2026 Singapore](https://ideseries.org/ide2026/)
* [First Lego League 2026-2027 (Bioglow) Philippines](https://felta.ph/pdf/fll/16th_FLL_Philippines_2026-2027_BIOGLOW_Season_Calendar.pdf)

### HuskyLens

* [HuskyLens Wiki](https://wiki.dfrobot.com/HUSKYLENS_V1.0_SKU_SEN0305_SEN0336)
* [PyHuskyLens Documentation](https://docs.antonsmindstorms.com/en/latest/Software/PyHuskyLens/docs/index.html)

## 📝 Notes

* Simulator programs are stored in `simulator.py` or `simulator_*.py`.
* Physical SPIKE Prime programs are stored in `actual.py` or `actual_*.py`.
* Motor and sensor ports may need to be changed based on the selected simulator robot or physical robot configuration.
* Wheel diameter, axle track, speed, and sensor thresholds may require calibration on the actual robot.
* The simulator is primarily used to test program logic, while the physical robot is used to test hardware behavior and calibration.
