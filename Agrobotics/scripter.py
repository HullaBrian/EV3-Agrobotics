from loguru import logger
import os
import sys

from pathfinding.objects import convertToSmallGrid
from pathfinding.pathfinding import SmallGrid
from challenges import load_challenges


logger.remove()
logger.add(sys.stderr, level="DEBUG")


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


def write_instructions(lst, file_obj):
    straight_accumulation: int = 0  # Used to simplify straight movements for robot
    straight_path = []
    for index, movement in enumerate(path):
        if movement.angle != 0:
            if straight_accumulation != 0:
                file.write(f"\n# Moving straight from {straight_path[0]} -> {straight_path[-1]}\n")
                file.write(f"robot.straight({straight_accumulation})\n")
                straight_accumulation = 0
                straight_path.clear()

            file.write(f"\n# Moving to {str(movement.move_node)}\n")
            file.write(f"robot.turn({movement.angle})\ntime.sleep(0.5)\n")
            file.write(f"robot.straight({round(movement.distance * 23.5) * -1})\n")
        else:
            straight_accumulation += round(movement.distance * 23.5) * -1
            straight_path.append(str(movement.move_node))


START = convertToSmallGrid((7, 4))
for challenge in load_challenges():
    with open(f"out/{challenge.name}", "w") as file:
        file.write("""#!/usr/bin/env pybricks-micropython
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
""")
    grid = SmallGrid()
    path = grid.pathFind(START, challenge.target)

    file.write("\n\nGOING TO THE CHALLENGE\n\n")
    write_instructions(path, file)
    file.write("\nDOING THE CHALLENGE\n\n")
    file.write(challenge.instructions + "\n")
    file.write("\nRETURNING\n\n")
    path = grid.pathFind(path[-1].move_node, START)  # TODO: INITIAL ANGLE IS NOT TAKEN INTO ACCOUNT WHEN RETURNING
    write_instructions(path, file)
