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
upper_deck = Motor(Port.A, positive_direction=Direction.CLOCKWISE)
lower_deck = Motor(Port.C, positive_direction=Direction.CLOCKWISE)
robot = DriveBase(left_motor, right_motor, wheel_diameter=82, axle_track=101)


# GOING TO THE CHALLENGE


# Moving to (30,28)
robot.turn(90)
time.sleep(0.5)
robot.straight(-41)

# Moving straight from (31,27) -> (33,25)
robot.straight(-123)

# Moving to (35,24)
robot.turn(-30)
time.sleep(0.5)
robot.straight(-70)

# Moving to (36,23)
robot.turn(30)
time.sleep(0.5)
robot.straight(-41)

# Moving straight from (37,22) -> (42,17)
robot.straight(-246)

# Moving to (44,16)
robot.turn(-30)
time.sleep(0.5)
robot.straight(-70)

# Moving straight from (46,15) -> (48,14)
robot.straight(-140)

# Moving to (49,13)
robot.turn(30)
time.sleep(0.5)
robot.straight(-41)

# Moving straight from (50,12) -> (50,12)
robot.straight(-41)

# Moving to (52,11)
robot.turn(-30)
time.sleep(0.5)
robot.straight(-70)

# Moving straight from (54,10) -> (56,9)
robot.straight(-140)

# Moving to (57,9)
robot.turn(-30)
time.sleep(0.5)
robot.straight(-41)

# Moving straight from (58,9) -> (58,9)
robot.straight(-41)

# Moving to (59,10)
robot.turn(-30)
time.sleep(0.5)
robot.straight(-70)

# Moving straight from (60,11) -> (60,11)
robot.straight(-70)

# Moving to (61,11)
robot.turn(30)
time.sleep(0.5)
robot.straight(-41)

# Moving straight from (62,11) -> (63,11)
robot.straight(-82)

# Moving to (64,12)
robot.turn(-30)
time.sleep(0.5)
robot.straight(-70)

# DOING THE CHALLENGE



# RETURNING

robot.turn(0)  # Orienting to 90 degrees!

# Moving to (25,51)
robot.turn(-120)
time.sleep(0.5)
robot.straight(-70)

# Moving to (24,50)
robot.turn(-60)
time.sleep(0.5)
robot.straight(-70)

# Moving to (25,48)
robot.turn(-60)
time.sleep(0.5)
robot.straight(-70)

# Moving straight from (26,46) -> (26,46)
robot.straight(-70)

# Moving to (27,45)
robot.turn(-30)
time.sleep(0.5)
robot.straight(-41)

# Moving straight from (28,44) -> (28,44)
robot.straight(-41)

# Moving to (29,42)
robot.turn(30)
time.sleep(0.5)
robot.straight(-70)

# Moving to (29,41)
robot.turn(30)
time.sleep(0.5)
robot.straight(-41)
