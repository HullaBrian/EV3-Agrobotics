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


# Moving to (31,28)
robot.turn(60)
time.sleep(0.5)
robot.straight(-70)

# Moving straight from (33,27) -> (43,22)
robot.straight(-420)

# Moving to (44,21)
robot.turn(30)
time.sleep(0.5)
robot.straight(-41)

# Moving straight from (45,20) -> (46,19)
robot.straight(-82)

# Moving to (47,17)
robot.turn(30)
time.sleep(0.5)
robot.straight(-70)

# Moving straight from (48,15) -> (48,15)
robot.straight(-70)

# Moving to (49,14)
robot.turn(-30)
time.sleep(0.5)
robot.straight(-41)

# Moving straight from (50,13) -> (50,13)
robot.straight(-41)

# Moving to (52,12)
robot.turn(-30)
time.sleep(0.5)
robot.straight(-70)

# Moving to (53,13)
robot.turn(-60)
time.sleep(0.5)
robot.straight(-70)

# DOING THE CHALLENGE



# RETURNING

robot.turn(0)  # Orienting to 90 degrees!

# Moving to (53,13)
robot.turn(180)
time.sleep(0.5)
robot.straight(-70)

# Moving straight from (52,12) -> (52,12)
robot.straight(-70)

# Moving to (50,13)
robot.turn(60)
time.sleep(0.5)
robot.straight(-70)

# Moving straight from (48,14) -> (36,20)
robot.straight(-490)

# Moving to (35,22)
robot.turn(60)
time.sleep(0.5)
robot.straight(-70)

# Moving to (33,23)
robot.turn(-60)
time.sleep(0.5)
robot.straight(-70)

# Moving straight from (31,24) -> (31,24)
robot.straight(-70)

# Moving to (30,26)
robot.turn(60)
time.sleep(0.5)
robot.straight(-70)

# Moving straight from (29,28) -> (29,28)
robot.straight(-70)

# Moving to (29,29)
robot.turn(30)
time.sleep(0.5)
robot.straight(-41)
