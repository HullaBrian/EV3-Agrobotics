# pathfinder.py: used to pathfind using a hybrid pathfinding system

# Builtins
import os
import json
import math

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
sqrt3 = math.sqrt(3)


def angle_between_hexes(hex1: tuple[int, int], hex2: tuple[int, int]) -> int:
    pass


def distance_between_hexes(hex1: tuple[int, int], hex2: tuple[int, int]) -> int:
    pass


def hexToRect(Coord: tuple) -> tuple:
    r = Coord[0]
    q = Coord[1]

    x = 46 - (q - r)
    y = 82 - (r + q)
    x *= round(3 * sqrt3)
    y *= 3

    return (x, y)  # Coordinates are in terms of half radii; x is approximated to nearest half radius


def pathfind(path_ref, start_tile=(-1, -1)) -> list[str]:  # "pathfinding/paths" is relative to the "scripter.py" file (the main code)
    """
    Will take the path to a .txt containing the path, then generate the robot code necessary to do that path
    Returns an array, where the rows are the lines to write
    """
    logger.info("Generating path from path file...")

    out: list[str] = []

    with open(path_ref, "r") as path_file:
        path: list[tuple[int, int]] = []
        for line in path_file.readlines():
            path.append(tuple(int(coord) for coord in line.split(" ")))

    if start_tile != (-1, -1):
        path.insert(0, start_tile)

    current_angle = 0
    for cur_index, cur_node in enumerate(path[:-1]):
        next_node = path[cur_index + 1]

        diff = (next_node[0] - cur_node[0], next_node[1] - cur_node[1])
        try:
            desired_angle = directional_vectors[diff]
        except KeyError:
            diff = (hexToRect((next_node[0] - cur_node[0], next_node[1] - cur_node[1])))
            desired_angle = -1 * math.atan((diff[0]) / diff[1])

        logger.debug(f"Angle between '{cur_node}' and '{next_node}' is '{desired_angle}'")


if __name__ == "__main__":
    pathfind("paths/testing/vectors.txt")
