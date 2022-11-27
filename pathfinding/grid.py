# DO NOT RUN ON EV3
# For generating the shortest path between two nodes
import math
import sys
from queue import Queue
from loguru import logger


# Remove debug messages for faster execution
logger.remove()
logger.add(sys.stderr, level="INFO")


class Hexagon(object):
    def __init__(self, coords: tuple, obstacle: bool = False):
        self.q = coords[0] # Coordinate corresponding to column
        self.r = coords[1] # Coordinate corresponding to negative diagonal

        #s coordinate is calculated from r and q and is used for some calculations
        self.s = -1 * (self.r + self.q) # Coordinate corresponding to positive diagonal
    
        self.neighbors = []

        self.obstacle: bool = obstacle

        logger.debug(f"Created new Hexagon at ({self.q},{self.r})")

    def __str__(self):
        return f"({self.q},{self.r})"


class Grid(object):
    def __init__(self, width: int = 14, height: int = 16, start: tuple = (7, 7)):
        # Initiating map as 2-D array with all values set to "None"
        self.grid = [[None] * width for i in range(height)]
        self.start = start
        logger.info("Initialized initial grid")

        with open("obstacles.txt", "r") as file:
            self.obstacles = [tuple([int(coord.removesuffix("\n")) for coord in line.split(",")]) for line in file.readlines()]
        logger.info("Registered obstacles at: " + ", ".join(str(content) for content in self.obstacles))

        #Defining all existing hexes
        for q in range(16):
            for i in range(6):
                r = i + (8 - math.ceil(q / 2))

                #Ignore hexes that are not printed on the moon base
                if q >= 6 or q <= 8:
                    if f"{q},{r}" in ["6,10", "7,9", "8,9"]:
                        break

                self.grid[q][r] = Hexagon((q, r), obstacle=True if (q, r) in self.obstacles else False)

        logger.info("Populated grid")

        self.axial_direction_vectors = [
            (0, -1), (-1, 0), (-1, +1),
            (0, +1), (+1, 0), (+1, -1)
        ]

        # Add buffers around the ACTUAL obstacles
        for obstacle in self.obstacles:
            for neighbor in self.grid[obstacle[0]][obstacle[1]].neighbors:
                neighbor.obstacle = True

        logger.success("Initialized grid!")

    def __str__(self):
        out: str = ""

        for row in list(zip(*self.grid[::1])):
            for hex in row:
                out += str(hex) + " "
            out += "\n"
        
        return out
