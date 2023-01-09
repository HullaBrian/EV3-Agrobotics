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


# Moving to (29,30)
robot.turn(-30)
time.sleep(0.5)
robot.straight(-41)

# Moving to (30,31)
robot.turn(30)
time.sleep(0.5)
robot.straight(-70)

# Moving to (30,32)
robot.turn(-30)
time.sleep(0.5)
robot.straight(-41)

# Moving straight from (30,33) -> (30,34)
robot.straight(-82)

# Moving to (31,35)
robot.turn(30)
time.sleep(0.5)
robot.straight(-70)

# Moving straight from (32,36) -> (33,37)
robot.straight(-140)

# Moving to (35,36)
robot.turn(60)
time.sleep(0.5)
robot.straight(-70)

# Moving to (36,37)
robot.turn(-60)
time.sleep(0.5)
robot.straight(-70)

# DOING THE CHALLENGE



# RETURNING

robot.turn(0)  # Orienting to 90 degrees!

# Moving to (39,40)
robot.turn(180)
time.sleep(0.5)
robot.straight(-70)

# Moving straight from (38,39) -> (35,36)
robot.straight(-280)

# Moving to (35,35)
robot.turn(-30)
time.sleep(0.5)
robot.straight(-41)

# Moving straight from (35,34) -> (35,32)
robot.straight(-123)

# Moving to (33,33)
robot.turn(90)
time.sleep(0.5)
robot.straight(-70)

# Moving to (32,32)
robot.turn(-60)
time.sleep(0.5)
robot.straight(-70)