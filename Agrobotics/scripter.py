from loguru import logger
import os
import sys
import json

# from pathfinding.objects import convertToSmallGrid
# from pathfinding.objects import shortest_angle
# from pathfinding.pathfinding import SmallGrid
from challenges import load_challenges


logger.remove()
logger.add(sys.stderr, level="INFO")


config_file = open("config.json", "r")
config = json.load(config_file)
config_file.close()
del config_file
base = f"""#!/usr/bin/env pybricks-micropython
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

left_motor = Motor(Port.{config["left wheel"]}, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.{config["right wheel"]}, Direction.COUNTERCLOCKWISE)
robo_gun = Motor(Port.{config["robo gun"]}, positive_direction=Direction.CLOCKWISE)
robot = DriveBase(left_motor, right_motor, wheel_diameter={config["wheel diameter"]}, axle_track={config["axle track"]})
"""