from loguru import logger
import os
import sys


from pathfinding.directional_movement import convert_to_directional_path
from pathfinding.pathfinding import SmallGrid


logger.remove()
logger.add(sys.stderr, level="DEBUG")


grid = SmallGrid()
path = grid.pathFind((19, 45), (32, 43))


# Get output script path
logger.debug(f"Current working directory is: {os.getcwd()}")
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
import time

ev3 = EV3Brick()

left_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.D, Direction.COUNTERCLOCKWISE)
robot = DriveBase(left_motor, right_motor, wheel_diameter=82, axle_track=101)

forklift_vertical = Motor(Port.A, positive_direction=Direction.CLOCKWISE)  # Positive is up
forklift_horizontal = Motor(Port.C, positive_direction=Direction.CLOCKWISE)  # Positive is out

ev3.speaker.beep()
""")

    for index, movement in enumerate(path):
        file.write(f"\n# Moving to {str(movement.move_node)}\n")

        try:
            move_angle = movement.angle - path[index - 1].angle
        except IndexError:
            move_angle = movement.angle
        if move_angle != 0:
            file.write(f"robot.turn({move_angle})\n")
        file.write(f"robot.straight({-1 * round(movement.distance * 23.5)})\n")
        if move_angle != 0:
            file.write("time.sleep(0.5)\n")
