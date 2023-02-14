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
right_motor = Motor(Port.D, Direction.COUNTERCLOCKWISE)
try:
    robo_gun = Motor(Port.C, positive_direction=Direction.CLOCKWISE)
except Exception:
    print("robo gun error!")
    robo_gun = None
robot = DriveBase(left_motor, right_motor, wheel_diameter=83, axle_track=100)
robot.settings(straight_speed=300)


def run_robo_gun(speed: int, rotations: int):
    for i in range(rotations):
        robo_gun.run_until_stalled(speed, duty_limit=80)
        speed *= -1


touch_sensor = TouchSensor(Port.S4)
touch_sensor2 = TouchSensor(Port.S1)
while not touch_sensor.pressed() and not touch_sensor2.pressed():
    pass
time.sleep(0.5)


# ----PATHFINDING---- #

# Moving straight from (31, 31) -> (31, 31)
robot.straight(-160)

# Moving to (27, 39)
robot.turn(-60)
time.sleep(0.5)
robot.straight(-321)

# ----INSTRUCTIONS---- #
run_robo_gun(200, 1)