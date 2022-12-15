from loguru import logger
import os
import sys
import math


from pathfinding.directional_movement import convert_to_directional_path
from pathfinding.pathfinding import SmallGrid


logger.remove()
logger.add(sys.stderr, level="DEBUG")


grid = SmallGrid()
path = grid.pathFind((5, 50), (67, 15))


# Get output script path
logger.debug(f"Current working directory is: {os.getcwd()}")
file_path = ""
for root, dirs, files in os.walk(os.getcwd(), topdown=False):
    for name in files:
        if name == "main.py":
            file_path = os.path.abspath(os.path.join(root, name))
            logger.success("Path found: " + file_path)
            break
if file_path == "":
    logger.error("Obstacles file not found")
    raise Exception("Obstacles file not found")


with open(file_path, "w+") as file:
    file.write("""#!/usr/bin/env pybricks-micropython
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
""")

    for index, movement in enumerate(path):
        file.write("\n")

        try:
            move_angle = movement.angle - path[index - 1].angle
        except IndexError:
            move_angle = movement.angle
        move_angle = move_angle % 360
        if abs(move_angle) > 180:
            move_angle = (move_angle * -1)
            if move_angle > 0:
                move_angle -= 180
            else:
                move_angle += 180

        if move_angle != 0:
            file.write(f"robot.turn({move_angle})\n")

        file.write(f"robot.straight({round(movement.distance * 23.5)})\n")
