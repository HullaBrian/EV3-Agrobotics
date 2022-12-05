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
ev3.speaker.beep() # Sanity Check

left_motor = Motor(Port.B)
right_motor = Motor(Port.D)

forklift = Motor(Port.C, positive_direction=Direction.CLOCKWISE)

time.sleep(1.0)
ev3.speaker.beep() # Sanity Check

# Measurements are innacurate
robot = DriveBase(left_motor, right_motor, wheel_diameter=82, axle_track=101)

ev3.speaker.beep() # Sanity Check

robot.straight(100)
robot.turn(90)

time.sleep(2.0)
ev3.speaker.beep()
time.sleep(2.0)
forklift.run_time(-1000, 1000)
time.sleep(2.0)
ev3.speaker.beep()
