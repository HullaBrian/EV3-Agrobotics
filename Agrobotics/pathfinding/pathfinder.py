# pathfinder.py: used to pathfind using a hybrid pathfinding system

# Builtins
import os
import json

# 3rd party
from loguru import logger

# Internal
#


directional_vectors = {
            (+1, -1): 90,
            (+1, -2): 120,
            (0, -1): 150,
            (-1, -1): 180,
            (-1, 0): 210,
            (-2, +1): 240,
            (-1, +1): 270,
            (-1, +2): 300,
            (0, +1): 330,
            (+1, +1): 0,
            (+1, 0): 30,
            (+2, -1): 60
}
logger.debug("Loaded directional vectors!")


def angle_between_hexes(hex1: tuple[int, int], hex2: tuple[int, int]) -> int:
    pass


def distance_between_hexes(hex1: tuple[int, int], hex2: tuple[int, int]) -> int:
    pass


def pathfind(path_ref, start_tile=(-1, -1)) -> list[str]:  # "pathfinding/paths" is relative to the "scripter.py" file (the main code)
    """
    Will take the path to a .txt containing the path, then generate the robot code necessary to do that path
    Returns an array, where the rows are the lines to write
    """
    logger.info("Generating path from path file...")

    out: list[str] = []

    with open(path_ref, "r") as path_file:
        path = path_file.readlines()

    if start_tile == (-1, -1):
        start_tile = tuple(int(i) for i in path[0].split(" "))

    current_angle = 0
    for cur_index, cur_node in enumerate(path[:-1]):
        next_node = path[cur_index]


if __name__ == "__main__":
    pathfind("paths", (7, 7))
