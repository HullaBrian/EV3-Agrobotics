# Objects module that contains helper objects and methods

# Builtin modules
import math
import os
from dataclasses import dataclass

# 3rd party modules
from loguru import logger


class Hexagon(object):
    def __init__(self, coords: tuple, obstacle: bool = False):
        self.q = coords[0]  # Coordinate corresponding to column
        self.r = coords[1]  # Coordinate corresponding to negative diagonal

        # s coordinate is calculated from r and q and is used for some calculations
        self.s = -1 * (self.r + self.q)  # Coordinate corresponding to positive diagonal

        self.neighbors = []

        self.obstacle: bool = obstacle

        logger.debug(f"Created new Hexagon at ({self.q},{self.r})")

    def __str__(self):
        return f"({self.q},{self.r})"


@dataclass
class movement_node:
    move_node: Hexagon  # Hexagon to move to
    start_node: Hexagon  # Hexagon moved from
    angle: int  # Angle to move at
    distance: int  # Distance to move


"""
------Helper Methods------
"""


def vector_to(hex1: Hexagon, hex2: Hexagon) -> tuple:
    try:
        return (hex2.r - hex1.r, hex2.q - hex1.q)
    except AttributeError:
        return (0, 0)


def convertToSmallGrid(largeCoord: tuple) -> tuple:
    r = largeCoord[0]
    q = largeCoord[1]
    small_r = 35 + (4 * (r - 7)) + (2 * (q - 7))  # I don't know why these are the formulas to convert all I know is that they work
    small_q = 35 - (2 * (r - 7)) + (2 * (q - 7))

    return (small_r, small_q)


def findObstaclesFile() -> str:
    global obstaclesFile
    if obstaclesFile == "":
        logger.debug(f"Current working directory is: {os.getcwd()}")
        for root, dirs, files in os.walk(os.getcwd(), topdown=False):
            for name in files:
                logger.debug(f"ACK file '{name}'")
                if name == "obstacles.txt":
                    filePath = os.path.abspath(os.path.join(root, name))
                    obstaclesFile = filePath
                    logger.success("Obstacles file found at path " + filePath)
                    break
    if obstaclesFile == "":
        logger.error("Obstacles file not found")
        raise Exception("Obstacles file not found")
    return obstaclesFile


def getObstacles() -> list[tuple]:
    obstacles = []

    with open(findObstaclesFile(), "r") as file:
        line = file.readline().removesuffix("\n") # Stores the first line for upcoming while loop
        while line != "":
            coord = line.split(",")  # stores all coords as lists of strings e.g. ["1", "8"]
            for i in range(len(coord)): coord[i] = int(coord[i])  # converts all strings in coord to ints
            coord = tuple(coord)  # converts the list coord into a tuple

            obstacles.append(coord) # adds current coord to obstacles
            line = file.readline().removesuffix("\n") # iterates on to next line to repeat while loop

    return obstacles


obstaclesFile: str = ""
sqrt3 = math.sqrt(3)


def hexToRect(Coord: tuple, isLarge: bool = False) -> tuple:
    r = Coord[0]
    q = Coord[1]

    if isLarge:
        x = r * 2
        y = 26 - ((2 * q) + r)

    else:
        x = 46 - (q - r)
        y = 82 - (r + q)
        x = x * round(3 * sqrt3)
        y = y * 3

    return (x, y)  # Coordinates are in terms of half radii; x is approximated to nearest half radius


def smallHexDistTo(start: tuple, end: tuple) -> int:
    """
    Takes two small hex coordinates and returns the linear distance between the two in terms of half
    radii to nearest half radius
    """

    # TODO: Fix diagonal paths being preferred over straight ones due to rounding apothems down to nearest half raidus

    start_rect_coord = hexToRect(start, False)
    start_x = start_rect_coord[0]
    start_y = start_rect_coord[1]

    end_rect_coord = hexToRect(end, False)
    end_x = end_rect_coord[0]
    end_y = end_rect_coord[1]

    dist = math.sqrt((end_x - start_x)**2 + (end_y - start_y)**2)  # Pythagorean theorem
    # Square root is necessary because program breaks without it

    return dist


def moveCost(hex1: Hexagon, hex2: Hexagon) -> int:
    axial_direction_vectors = [
        (0, -1), (-1, 0), (-1, +1),
        (0, +1), (+1, 0), (+1, -1)
    ]
    weighted_axial_direction_vectors = [
        (-1, -1), (-2, +1), (-1, +2),
        (+1, +1), (+2, -1), (+1, -2)
    ]
    axial_vectors_cost = sqrt3
    weighted_vectors_cost = 3

    vector = (hex2.r - hex1.r, hex2.q - hex1.q)

    if vector in weighted_axial_direction_vectors:
        logger.debug(f"Move cost between {hex1} and {hex2} is weighted and has cost {weighted_vectors_cost}")
        return weighted_vectors_cost
    elif vector in axial_direction_vectors:
        logger.debug(f"Move cost between {hex1} and {hex2} is axial and has {axial_vectors_cost}")
        return axial_vectors_cost
    else:
        logger.error(f"Attempted to find cost of vector {vector} but {vector} not in vector lists")
