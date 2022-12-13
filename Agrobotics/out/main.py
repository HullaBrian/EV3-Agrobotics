#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time

ev3 = EV3Brick()

left_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.D, Direction.COUNTERCLOCKWISE)
robot = DriveBase(left_motor, right_motor, wheel_diameter=82, axle_track=101)

forklift_vertical = Motor(Port.A, positive_direction=Direction.CLOCKWISE)  # Positive is up
forklift_horizontal = Motor(Port.C, positive_direction=Direction.CLOCKWISE)  # Positive is out

ev3.speaker.beep()

# Moving to (20,45)
robot.straight(-41)

# Moving to (21,46)
robot.turn(-30)
robot.straight(-70)
time.sleep(0.5)

# Moving to (22,46)
robot.turn(30)
robot.straight(-41)
time.sleep(0.5)

# Moving to (23,46)
robot.straight(-41)

# Moving to (24,46)
robot.straight(-41)

# Moving to (26,45)
robot.turn(30)
robot.straight(-70)
time.sleep(0.5)

# Moving to (28,44)
robot.straight(-70)

# Moving to (30,43)
robot.straight(-70)

# Moving to (31,43)
robot.turn(-30)
robot.straight(-41)
time.sleep(0.5)

# Moving to (32,43)
robot.straight(-41)
