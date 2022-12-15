#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time

# This program requires LEGO EV3 MicroPython v2.0 or higher.

# Create your objects here.
ev3 = EV3Brick()

left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
forklift = Motor(Port.C, positive_direction=Direction.CLOCKWISE)
robot = DriveBase(left_motor, right_motor, wheel_diameter=82, axle_track=101)

# Moving to (7,49)
robot.turn(60)
time.sleep(0.5)
robot.straight(70)

# Moving to (9,48)
robot.straight(70)

# Moving to (10,47)
robot.turn(30)
time.sleep(0.5)
robot.straight(41)

# Moving to (11,46)
robot.straight(41)

# Moving to (12,45)
robot.straight(41)

# Moving to (13,44)
robot.straight(41)

# Moving to (14,43)
robot.straight(41)

# Moving to (15,42)
robot.straight(41)

# Moving to (16,41)
robot.straight(41)

# Moving to (18,40)
robot.turn(-150)
time.sleep(0.5)
robot.straight(70)

# Moving to (20,39)
robot.straight(70)

# Moving to (22,38)
robot.straight(70)

# Moving to (24,37)
robot.straight(70)

# Moving to (26,36)
robot.straight(70)

# Moving to (28,35)
robot.straight(70)

# Moving to (30,34)
robot.straight(70)

# Moving to (32,33)
robot.straight(70)

# Moving to (33,32)
robot.turn(30)
time.sleep(0.5)
robot.straight(41)

# Moving to (35,31)
robot.turn(-150)
time.sleep(0.5)
robot.straight(70)

# Moving to (37,30)
robot.straight(70)

# Moving to (39,29)
robot.straight(70)

# Moving to (41,28)
robot.straight(70)

# Moving to (43,27)
robot.straight(70)

# Moving to (44,26)
robot.turn(30)
time.sleep(0.5)
robot.straight(41)

# Moving to (45,24)
robot.turn(30)
time.sleep(0.5)
robot.straight(70)

# Moving to (45,23)
robot.turn(30)
time.sleep(0.5)
robot.straight(41)

# Moving to (46,21)
robot.turn(-150)
time.sleep(0.5)
robot.straight(70)

# Moving to (48,20)
robot.turn(-120)
time.sleep(0.5)
robot.straight(70)

# Moving to (50,19)
robot.straight(70)

# Moving to (52,18)
robot.straight(70)

# Moving to (54,17)
robot.straight(70)

# Moving to (56,16)
robot.straight(70)

# Moving to (58,15)
robot.straight(70)

# Moving to (60,14)
robot.straight(70)

# Moving to (61,14)
robot.turn(-150)
time.sleep(0.5)
robot.straight(41)

# Moving to (62,14)
robot.straight(41)

# Moving to (63,14)
robot.straight(41)

# Moving to (64,14)
robot.straight(41)

# Moving to (65,14)
robot.straight(41)

# Moving to (66,14)
robot.straight(41)

# Moving to (67,15)
robot.turn(-150)
time.sleep(0.5)
robot.straight(70)
