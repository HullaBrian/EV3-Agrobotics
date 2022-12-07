# DO NOT RUN ON EV3
# For generating the shortest path between two nodes

# https://www.pythonpool.com/a-star-algorithm-python/
import math
import sys
from queue import Queue
from loguru import logger
import os

obstaclesFile: str = ""


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


def convertToSmallGrid(largeCoord: tuple) -> tuple:
        r = largeCoord[0]
        q = largeCoord[1]
        small_r = 35 - (4 * (r - 7)) + (2 * (q - 7)) #I don't know why these are the formulas to convert all I know is that they work
        small_q = 35 + (2 * (r - 7)) + (2 * (q - 7))
        return (small_r, small_q)

def findObstaclesFile() -> str:
    global obstaclesFile
    if obstaclesFile == "":
        for root, dirs, files in os.walk(os.getcwd()):
            for name in files:
                if name == "obstacles.txt":
                    filePath = os.path.abspath(os.path.join(root, name))
                    obstaclesFile = filePath
                    logger.success("Obstacles file found at path " + filePath)
                    break
    if obstaclesFile == "":
        logger.error("Obstacles file not found")
        raise Exception("Obstacles file not found")
    return obstaclesFile
    

class Grid(object):
    def __init__(self, width: int, height: int, start: tuple):
        # Initiating map as 2-D array with all values set to "None"
        self.grid = [[None] * width for i in range(height)]
        self.start = start
        logger.info("Initialized initial grid")

        self.axial_direction_vectors = [
            (0, -1), (-1, 0), (-1, +1),
            (0, +1), (+1, 0), (+1, -1)
        ]
        self.weighted_axial_direction_vectors = [
            (-1, -1), (-2, +1), (-1, +2),
            (+1, +1), (+2, -1), (+1, -2)
        ]

    def __getNeighborsOf(self, hexagon: Hexagon) -> list[str]:
        neighbors: list[Hexagon] = []

        for vector in list(self.axial_direction_vectors).extend(self.weighted_axial_direction_vectors):
            try:
                neighbor = self.grid[hexagon.q + vector[0]][hexagon.r + vector[1]]
                
                if neighbor is not None:
                    neighbors.append((neighbor, 3 if vector in self.weighted_axial_direction_vectors else 2))
                    logger.debug(f"Generated neighbor for Hexagon ({hexagon.q},{hexagon.r}) -> ({neighbor.q},{neighbor.r}) with weight {3 if vector in self.weighted_axial_direction_vectors else 2}")
            except AttributeError:
                continue
            except IndexError:
                continue

        return neighbors
    
    def pathfind(self, end: tuple) -> list:
        start_hexagon = self.grid[self.start[0]][self.start[1]]
        end_hexagon = self.grid[end[0]][end[1]]

        #TODO: Implement weighting for pathfinding and allow for travel along vectors (-1,-1), (-2, +1), (-1, +2), (+1, +1), (+2, -1), and (+1, -2)

        frontier = Queue()
        frontier.put(start_hexagon)
        came_from = dict() # path A->B is stored as came_from[B] == A
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

        with open(findObstaclesFile(), "r") as file:
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

        self.obstacles: list[tuple] = []
        with open(findObstaclesFile(), "r") as file: # Read Obstacles from obstacle list
            large_obstacles = [tuple([int(coord.removesuffix("\n")) for coord in line.split(",")]) for line in file.readlines()]

        #Convert obstacles to correct format
        for obstacle in large_obstacles:
            self.obstacles.append(convertToSmallGrid(obstacle))

        #Define Hexagons in grid using funky algebraic properties of the grid
        for i in range(63):
            r = i + 5
            if(r < 54):
                q = 55 - r
            else:
                q = r - 52
            if(r < 19):
                while(q - r < 47):
                    self.grid[r][q] = Hexagon((r,q))
                    q += 1
            else:
                while(q + r <= 82):
                    self.grid[r][q] = Hexagon((r,q))
                    q += 1

        #TODO: Add code for small grid obstacles


if __name__ == "__main__":
    # Remove debug messages for faster execution
    logger.remove()
    logger.add(sys.stderr, level="INFO")
    
    logger.info("Creating grid")
    start = (7, 4)
    grid = LargeGrid(start=start)
    small_grid = SmallGrid()
    
    #for node in grid.pathfind((11, 3)):
    #    print(node)
