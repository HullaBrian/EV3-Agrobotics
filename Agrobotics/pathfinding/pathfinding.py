# DO NOT RUN ON EV3
# For generating the shortest path between two nodes

# https://www.pythonpool.com/a-star-algorithm-python/
import math
import sys
import time
from queue import Queue
from queue import PriorityQueue
from itertools import count
from loguru import logger
import os
from threading import Thread

logger.info("Program Start")

unique = count()


obstaclesFile: str = ""
sqrt3 = math.sqrt(3)


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
            coord = line.split(",") # stores all coords as lists of strings e.g. ["1", "8"]
            for i in range(len(coord)): coord[i] = int(coord[i]) # converts all strings in coord to ints
            coord = tuple(coord) # converts the list coord into a tuple

            obstacles.append(coord) # adds current coord to obstacles
            line = file.readline().removesuffix("\n") # iterates on to next line to repeat while loop

    return obstacles


def hexToRect(Coord: tuple, isLarge: bool = False) -> tuple:
    r = Coord[0]
    q = Coord[1]

    if isLarge:
        x = r * 2
        y = 26 - ((2 * q) + r)
    else:
        x = 46 - (q - r)
        y = 82 - (r + q)
        x = round(3 * sqrt3)
        y = y * 3

    return (x, y) # Coordinates are in terms of half radii; x is approximated to nearest half radius


def smallHexDistTo(start: tuple, end: tuple) -> int:
    """
    Takes two small hex coordinates and returns the linear distance (squared) between the two in terms of half
    radii to nearest half radius
    """

    # TODO: Fix diagonal paths being preferred over straight ones due to rounding apothems down to nearest half raidus

    start_rect_coord = hexToRect(start, False)
    start_x = start_rect_coord[0]
    start_y = start_rect_coord[1]

    end_rect_coord = hexToRect(end, False)
    end_x = end_rect_coord[0]
    end_y = end_rect_coord[1]

    dist = (end_x - start_x)**2 + (end_y - start_y)**2  # Pythagorean theorum without square root
    #Square root is unnecessary because for all non-negative values of a and b where a > b,  a*a > b*b

    return dist


class Grid(object):
    def __init__(self, width: int, height: int, start: tuple):
        # Initiating map as 2-D array with all values set to "None"
        self.grid = [[None] * width for i in range(height)]
        self.start = start
        self.axial_vectors_cost = 2
        self.weighted_vectors_cost = 3
        logger.info("Initialized initial grid")

        self.axial_direction_vectors = [
            (0, -1), (-1, 0), (-1, +1),
            (0, +1), (+1, 0), (+1, -1)
        ]
        self.weighted_axial_direction_vectors = [
            (-1, -1), (-2, +1), (-1, +2),
            (+1, +1), (+2, -1), (+1, -2)
        ]

    def getNeighborsOf(self, hexagon: Hexagon) -> list[str]:
        neighbors: list[tuple] = []

        vectors = self.axial_direction_vectors
        vectors.extend(self.weighted_axial_direction_vectors)

        for vector in vectors:
            try:
                neighbor = self.grid[hexagon.q + vector[0]][hexagon.r + vector[1]]
                
                if neighbor is not None:
                    neighbors.append(neighbor)
                    logger.debug(f"Generated neighbor for Hexagon ({hexagon.q},{hexagon.r}) -> ({neighbor.q},{neighbor.r})")
            except AttributeError:
                continue
            except IndexError:
                continue
        logger.debug(f"Hexagon {hexagon} has neighbors list {neighbors}")
        return neighbors


    def moveCost(self, hex1: Hexagon, hex2: Hexagon) -> int:
        vector = (hex2.r - hex1.r, hex2.q - hex1.q)
        if vector in self.axial_direction_vectors:
            return self.axial_vectors_cost
        elif vector in self.weighted_axial_direction_vectors:
            return self.weighted_vectors_cost
        else:
            logger.error(f"Attempted to find cost of vector {vector} but {vector} not in vector lists")
            
    
    def newPathFind(self, start: tuple, end: tuple) -> list:
        start_hexagon = self.grid[start[0]][start[1]]
        end_hexagon = self.grid[end[0]][end[1]]

        logger.info(f"Pathfinding from {start_hexagon} to {end_hexagon}")

        frontier = PriorityQueue()
        frontier.put((0, next(unique), start_hexagon))

        logger.debug(f"Frontier contains {frontier.queue}")

        came_from = {start_hexagon: None}
        cost_so_far = {start_hexagon: 0}

        while not frontier.empty():
            current = frontier.get()
            current = current[2]

            if current == end_hexagon:
                break

            for next_hex in self.getNeighborsOf(current):
                new_cost = cost_so_far[current] + self.moveCost(current, next_hex)
                if next_hex not in cost_so_far or new_cost < cost_so_far[next_hex]:
                    logger.debug(f"Adding hex to queue at {next_hex.r}, {next_hex.q}")
                    cost_so_far[next_hex] = new_cost
                    priority = new_cost + smallHexDistTo((next_hex.r, next_hex.q), (end_hexagon.r, end_hexagon.q))
                    frontier.put((priority, next(unique), next_hex))
                    came_from[next_hex] = current
        else:
            logger.error(f"No path from {start} to {end} found")

        path = [current] #This list will be the shortest path between the two hexes

        while current != start_hexagon:
            current = came_from[current]
            path.append(current)
        
        path.reverse()

        logger.info("Shortest path found is: ")
        for node in path:
            logger.info(str(node))
        
        return path
    

    # Pathfind function is made largely obsolete by newPathfind consider removing once newPathfind is known to be fully functioning
    def pathfind(self, end: tuple) -> list:
        start_hexagon = self.grid[self.start[0]][self.start[1]]
        end_hexagon = self.grid[end[0]][end[1]]

        #TODO: Implement weighting for pathfinding and allow for travel along vectors (-1,-1), (-2, +1), (-1, +2), (+1, +1), (+2, -1), and (+1, -2)

        frontier = Queue()
        frontier.put(start_hexagon)
        came_from = dict()  # path A->B is stored as came_from[B] == A
        came_from[start_hexagon] = None

        while not frontier.empty():
            current = frontier.get()

            if (current.q, current.r) == end:
                break

            for next in self.__getNeighborsOf(current):
                if next not in came_from and not next.obstacle:
                    frontier.put(next)
                    came_from[next] = current

        path = [end_hexagon]
        try:
            current = came_from[end_hexagon]
        except KeyError:
            logger.critical(f"Could not find path from {start_hexagon} to {end_hexagon}")
            return []
        while current is not start_hexagon:
            path.append(current)
            current = came_from[current]

        return path[::-1]

    def __str__(self):
        out: str = ""

        for row in list(zip(*self.grid[::1])):
            for hex in row:
                out += str(hex) + " "
            out += "\n"
        
        return out


class LargeGrid(Grid):
    """
    LargeGrid is solely for inputting data
    """
    def __init__(self, width: int = 14, height: int = 16, start: tuple = (7,7)):
        super().__init__(width, height, start)

        self.obstacles = getObstacles()
        logger.info("Registered obstacles at: " + ", ".join(str(content) for content in self.obstacles))

        #Defining all existing hexes
        for q in range(16):
            for i in range(6):
                r = i + (8 - math.ceil(q / 2))

                #Ignore hexes that are not printed on the moon base
                if q >= 6 or q <= 8:
                    if f"{q},{r}" in ["6,10", "7,9", "8,9"]:
                        break

                #Set as obstacle if in obstacles list
                self.grid[q][r] = Hexagon((q, r), obstacle=True if (q, r) in self.obstacles else False)
        
        logger.info("Populated Grid")

        for row in self.grid:
            for hexagon in row:
                try:
                    hexagon.neighbors = self.__getNeighborsOf(hexagon)
                except AttributeError:
                    continue

        # Add buffers around the ACTUAL obstacles
        for obstacle in self.obstacles:
            for neighbor in self.grid[obstacle[0]][obstacle[1]].neighbors:
                neighbor.obstacle = True

        logger.success("Initialized large grid!")


class SmallGrid(Grid):
    """
    SmallGrid is used for pathfinding
    """
    def __init__(self, width: int = 65, height: int = 68, start: tuple = (35, 35)):
        super().__init__(width, height, start)

        large_obstacles: list[tuple] = getObstacles()
        self.obstacles: list[tuple] = []

        # Convert obstacles to correct format
        for obstacle in large_obstacles:
            self.obstacles.append(convertToSmallGrid(obstacle))
        
        logger.info("Registered small obstacles at: " + ", ".join(str(content) for content in self.obstacles))

        # Define Hexagons in grid using funky algebraic properties of the grid
        for i in range(63):
            r = i + 5
            if r < 54:
                q = 55 - r
            else:
                q = r - 52
            if r < 19:
                while q - r < 47:
                    self.grid[r][q] = Hexagon((r, q))
                    q += 1
            else:
                while q + r <= 82:
                    self.grid[r][q] = Hexagon((r, q))
                    q += 1

        # TODO: Add code for small grid obstacles


        #Begin multi-threaded neighbor generation
        logger.info("Generating neighbors...")
        thread_count = 4  # There are 68 rows, leaving each thread (assuming 4) 17 rows to do
        start = time.time()

        threads: list[Thread] = []
        row_counter = 0
        iterator = int(len(self.grid) / thread_count)

        # Initialize threads
        for _ in range(thread_count):
            threads.append(Thread(target=self.__generate_neighbors, args=(self.grid[row_counter:row_counter + iterator])))
            row_counter += iterator

        # Start threads
        for thread in threads:
            thread.start()

        # Wait for threads to stop
        while True in [thread.is_alive() for thread in threads]:
            pass

        end = time.time()
        logger.success(f"Finished generating neighbors in {(end - start)} seconds.")

    def __generate_neighbors(*map: list[list]):
        rows = []
        for row in map[1:]:
            rows.append(row)
        #print(rows)
        for row in rows:
            for hexagon in row:
                try:
                    hexagon.neighbors = super.getNeighborsOf(hexagon)
                except AttributeError:
                    continue


if __name__ == "__main__":
    # Remove debug messages for faster execution
    logger.remove()
    logger.add(sys.stderr, level="INFO")
    logger.info("Creating grid")
    start = (7, 4)
    grid = LargeGrid(start=start)
    small_grid = SmallGrid()
    small_grid.newPathFind((5, 50), (67, 15))

    """
    for row in small_grid.grid:
        for hexagon in row:
            try:
                if hexagon.neighbors is not None and hexagon.neighbors is not []:
                    print(f"Hexagon at {hexagon} has neighbors!")
            except AttributeError:
                pass
    """