#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# This program requires LEGO EV3 MicroPython v2.0 or higher.

# Create your objects here.
ev3 = EV3Brick()

left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
forklift = Motor(Port.C, positive_direction=Direction.CLOCKWISE)
robot = DriveBase(left_motor, right_motor, wheel_diameter=82, axle_track=101)

robot.turn(60)
robot.straight(70)

robot.straight(70)

robot.turn(30)
robot.straight(41)

robot.straight(41)

robot.straight(41)

robot.straight(41)

robot.straight(41)

robot.straight(41)

robot.straight(41)

robot.turn(-150)
robot.straight(70)

robot.straight(70)

robot.straight(70)

robot.straight(70)

robot.straight(70)

robot.straight(70)

robot.straight(70)

robot.straight(70)

robot.turn(30)
robot.straight(41)

robot.turn(-150)
robot.straight(70)

robot.straight(70)

robot.straight(70)

robot.straight(70)

robot.straight(70)

robot.turn(30)
robot.straight(41)

robot.turn(30)
robot.straight(70)

robot.turn(30)
robot.straight(41)

robot.turn(-150)
robot.straight(70)

robot.turn(-120)
robot.straight(70)

robot.straight(70)

robot.straight(70)

robot.straight(70)

robot.straight(70)

robot.straight(70)

robot.straight(70)

robot.turn(-150)
robot.straight(41)

robot.straight(41)

robot.straight(41)

robot.straight(41)

robot.straight(41)

robot.straight(41)

robot.turn(-150)
robot.straight(70)
