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

left_motor = Motor(Port.D, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
forklift = Motor(Port.C, positive_direction=Direction.CLOCKWISE)
robot = DriveBase(left_motor, right_motor, wheel_diameter=82, axle_track=101)


# GOING TO THE CHALLENGE


# Moving to (28,31)
robot.turn(-60)
time.sleep(0.5)
robot.straight(-70)

# Moving straight from (27,33) -> (25,37)
robot.straight(-210)

# Moving to (24,38)
robot.turn(-30)
time.sleep(0.5)
robot.straight(-41)

# Moving to (23,40)
robot.turn(30)
time.sleep(0.5)
robot.straight(-70)

# Moving straight from (22,42) -> (21,44)
robot.straight(-140)

# Moving to (21,45)
robot.turn(30)
time.sleep(0.5)
robot.straight(-41)

# Moving straight from (21,46) -> (21,54)
robot.straight(-369)

# Moving to (20,56)
robot.turn(-30)
time.sleep(0.5)
robot.straight(-70)

# Moving straight from (19,58) -> (18,60)
robot.straight(-140)

# Moving to (18,61)
robot.turn(30)
time.sleep(0.5)
robot.straight(-41)

# Moving to (17,63)
robot.turn(-30)
time.sleep(0.5)
robot.straight(-70)

# DOING THE CHALLENGE



# RETURNING

robot.turn(60)  # Orienting to 90 degrees!

# Moving to (43,14)
robot.turn(-120)
time.sleep(0.5)
robot.straight(-70)

# Moving straight from (41,15) -> (39,16)
robot.straight(-140)

# Moving to (38,18)
robot.turn(60)
time.sleep(0.5)
robot.straight(-70)

# Moving straight from (37,20) -> (35,24)
robot.straight(-210)

# Moving to (33,25)
robot.turn(-60)
time.sleep(0.5)
robot.straight(-70)

# Moving straight from (31,26) -> (31,26)
robot.straight(-70)

# Moving to (30,28)
robot.turn(60)
time.sleep(0.5)
robot.straight(-70)

# Moving to (29,29)
robot.turn(-30)
time.sleep(0.5)
robot.straight(-41)
