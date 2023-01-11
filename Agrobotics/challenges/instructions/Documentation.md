# Documentation for Programming Challenges
## Changing Variables
- To change a motor port, wheel diameter, or axle track length, edit config.json in the challenges directory.

## Programing
- Forwards: ```robot.straight(*distance in mm*)```
  - Changing robot DriveBase settings:
    - ```robot.settings(straight_speed, straight_acceleration, turn_rate, turn_acceleration)```
      - ``straight_speed`` is in mm/s
      - ```straight_acceleration``` is in mm/s<sup>2</sup>
      - ```turn_rate``` is in deg/s
      - ```turn_acceleration``` is in deg/s<sup>2</sup>
- Stop movement: ```robot.stop()```

## Ev3 MicroPython Documentation
- [DriveBase](https://pybricks.com/ev3-micropython/robotics.html#pybricks.robotics.DriveBase)
