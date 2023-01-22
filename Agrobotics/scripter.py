# 3rd party
from loguru import logger

# Builtins
import os
import sys
import json
import time
from threading import Thread

# Internal
from challenges import load_challenges
from pathfinding.pathfinder import pathfind


logger.remove()
logger.add(sys.stderr, level="DEBUG")


logger.debug("Loading config...")
config_file = open("pathfinding/config.json", "r")
config = json.load(config_file)
config_file.close()
del config_file
logger.info("Loaded config!")

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
logger.success("Applied config!")

logger.info("Scanning for path files...")
paths = []
for path in os.listdir(f"pathfinding{os.sep}paths"):
    if path.endswith(".txt"):
        paths.append(f"pathfinding{os.sep}paths{os.sep}{path}")
        logger.debug(f"Found path '{path}'")
logger.success("Retrieved list of all paths!")


def pathfind_thread(path_location: str):
    global paths_dict
    paths_dict[path_location] = pathfind(path_location)


logger.info("Starting worker threads...")
paths_dict: dict = {}
threads = []
for path in paths:
    t = Thread(target=pathfind_thread, args=(path,))
    t.start()
    threads.append(t)
    logger.debug(f"Started thread for '{path}'")

logger.success("Started all worker threads!")
logger.info("Waiting for threads to finish...")
while True:
    num = 0
    for thread in threads:
        if not thread.is_alive():
            num += 1
    if num == len(threads):
        break
logger.success("All threads have finished!")
logger.info("Writing all instructions to out files...")


def write_instructions(lst: list, file_obj):
    straight_accumulation: int = 0  # Used to simplify straight movements for robot
    straight_path = []
    try:
        for index, movement in enumerate(lst):
            if movement.angle != 0:
                if straight_accumulation != 0:
                    file_obj.write(f"\n# Moving straight from {straight_path[0]} -> {straight_path[-1]}\n")
                    file_obj.write(f"robot.straight({straight_accumulation})\n")
                    straight_accumulation = 0
                    straight_path.clear()

                file_obj.write(f"\n# Moving to {str(movement.move_node)}\n")
                file_obj.write(f"robot.turn({movement.angle})\ntime.sleep(0.5)\n")
                file_obj.write(f"robot.straight({round(movement.distance * 11.68)})\n")
            else:
                straight_accumulation += round(movement.distance * 11.68)
                straight_path.append(str(movement.move_node))

                if len(lst) == 1:
                    file_obj.write(f"robot.straight({round(movement.distance * 11.68)})\n")
    except TypeError:
        if lst is None:
            logger.error(file_obj.name + " does not instructions to write!")


for file_name in paths_dict:
    logger.info(f"Writing instructions for '{file_name}'")
    with open(os.path.join("out", file_name.split(os.sep)[-1].replace(".txt", ".py")), "w") as path_file:
        path_file.write(base + "\n\n# ----MAIN---- #\n\n")
        logger.debug("Wrote base code.")
        write_instructions(paths_dict[file_name], path_file)
        logger.debug("Wrote instructions")
    logger.success(f"Wrote instructions for '{file_name}'")
logger.success("Successfully wrote all instructions to out files!")
