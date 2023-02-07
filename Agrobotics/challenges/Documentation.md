# Documentation for Programming Challenges
## Changing Variables
- To change a motor port, wheel diameter, or axle track length, edit config.json

## Programing
### Robot driving/settings:
- Forwards: ```robot.straight(*distance in mm*)```
- Turn: ```robot.turn(angle_in_degrees)```
- Changing robot DriveBase settings:
  - ```robot.settings(straight_speed, straight_acceleration, turn_rate, turn_acceleration)```
    - ``straight_speed`` is in mm/s
    - ```straight_acceleration``` is in mm/s<sup>2</sup>
    - ```turn_rate``` is in deg/s
    - ```turn_acceleration``` is in deg/s<sup>2</sup>
- Stop movement: ```robot.stop()```
### The Robo-Gun
- Use `run_robo_gun(speed_degrees_per_second, #_of_rotations)` to run the robo-gun for a specified number of rotations

## Ev3 MicroPython Documentation
- [DriveBase](https://pybricks.com/ev3-micropython/robotics.html#pybricks.robotics.DriveBase)
- [Motor](https://pybricks.com/ev3-micropython/ev3devices.html?highlight=motor#motors)