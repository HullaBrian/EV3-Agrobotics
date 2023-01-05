# DO NOT RUN ON EV3
# For generating the shortest path between two nodes

# Builtin modules
import math
import sys
import time
from queue import PriorityQueue
from itertools import count
from threading import Thread

# 3rd party modules
from loguru import logger

# Internal modules
from pathfinding.objects import Hexagon
from pathfinding.objects import getObstacles
from pathfinding.objects import convertToSmallGrid
from pathfinding.objects import smallHexDistTo
from pathfinding.objects import movement_node
from pathfinding.objects import vector_to

from pathfinding.directional_movement import convert_to_directional_path

unique = count()
previous_vector = None


class Grid(object):
    def __init__(self, width: int, height: int, start: tuple):
        # Initiating map as 2-D array with all values set to "None"
        self.grid = [[None] * width for i in range(height)]
        self.start = start

        self.axial_vectors_cost = math.sqrt(3)
        self.weighted_vectors_cost = 3
        self.angle_cost = 5

        logger.info("Initialized initial grid")

        self.axial_direction_vectors = [
            (0, -1), (-1, 0), (-1, +1),
            (0, +1), (+1, 0), (+1, -1)
        ]
        self.weighted_axial_direction_vectors = [
            (-1, -1), (-2, +1), (-1, +2),
            (+1, +1), (+2, -1), (+1, -2)
        ]
        self.vectors = []
        self.vectors.extend(self.axial_direction_vectors)
        self.vectors.extend(self.weighted_axial_direction_vectors)

    def getNeighborsOf(self, hexagon: Hexagon) -> list[str]:
        neighbors: list[tuple] = []

        for vector in self.vectors:
            try:
                neighbor = self.grid[hexagon.q + vector[0]][hexagon.r + vector[1]]

                if neighbor is not None:
                    neighbors.append(neighbor)
                    # logger.debug(f"Generated neighbor for Hexagon ({hexagon.q},{hexagon.r}) -> ({neighbor.q},{neighbor.r})")
            except AttributeError:
                continue
            except IndexError:
                continue

        return neighbors

    def moveCost(self, hex1: Hexagon, hex2: Hexagon) -> int:
        vector = (hex2.r - hex1.r, hex2.q - hex1.q)

        if vector in self.weighted_axial_direction_vectors:
            logger.debug(f"Move cost between {hex1} and {hex2} is weighted and has cost {self.weighted_vectors_cost}")
            return self.weighted_vectors_cost
        elif vector in self.axial_direction_vectors:
            logger.debug(f"Move cost between {hex1} and {hex2} is axial and has {self.axial_vectors_cost}")
            return self.axial_vectors_cost
        else:
            logger.error(f"Attempted to find cost of vector {vector} but {vector} not in vector lists")

    def pathFind(self, start: tuple, end: tuple) -> list[movement_node]:
        global previous_vector

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

            for next_hex in current.neighbors:
                new_cost = cost_so_far[current] + self.moveCost(current, next_hex)

                if next_hex.obstacle:
                    logger.debug(f"Avoided obstacle at {str(next_hex)}")
                    continue

                if next_hex not in cost_so_far or new_cost < cost_so_far[next_hex]:
                    logger.debug(f"Adding hex to queue at {next_hex.r}, {next_hex.q} with total cost of {new_cost}")
                    cost_so_far[next_hex] = new_cost

                    priority = new_cost + (smallHexDistTo((next_hex.r, next_hex.q), (end_hexagon.r, end_hexagon.q)) / 3.9)
                    if vector_to(came_from[current], current) != vector_to(current, next_hex):
                        priority += self.angle_cost

                    logger.debug(f"Hex at {next_hex.r}, {next_hex.q} has a priority of {priority}")
                    frontier.put((priority, next(unique), next_hex))
                    came_from[next_hex] = current
        else:
            logger.error(f"No path from {start} to {end} found")

        path: list[Hexagon] = [current]  # This list will be the shortest path between the two hexes

        while current != start_hexagon:
            current = came_from[current]
            path.append(current)
        
        path.reverse()

        logger.info("Shortest path found is: ")
        for node in path:
            logger.info(f'{str(node)} {cost_so_far[node]}')
        
        return convert_to_directional_path(path)


class LargeGrid(Grid):
    """
    LargeGrid is solely for inputting data
    """
    def __init__(self, width: int = 14, height: int = 16, start: tuple = (7,7)):
        super().__init__(width, height, start)

        self.obstacles = getObstacles()
        logger.info("Registered obstacles at: " + ", ".join(str(content) for content in self.obstacles))

        # Defining all existing hexes
        for q in range(16):
            for i in range(6):
                r = i + (8 - math.ceil(q / 2))

                # Ignore hexes that are not printed on the moon base
                if q >= 6 or q <= 8:
                    if f"{q},{r}" in ["6,10", "7,9", "8,9"]:
                        break

                # Set as obstacle if in obstacles list
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

        # Begin multi-threaded neighbor generation
        logger.info("Generating neighbors...")
        thread_count = 4  # There are 68 rows, leaving each thread (assuming 4) 17 rows to do
        start = time.time()

        threads: list[Thread] = []
        row_counter = 0
        iterator = int(len(self.grid) / thread_count)

        # Initialize threads
        for _ in range(thread_count):
            threads.append(
                Thread(target=self.__generate_neighbors, args=(self.grid[row_counter:row_counter + iterator])))
            row_counter += iterator

        # Start threads
        for thread in threads:
            thread.start()

        # Wait for threads to stop
        while True in [thread.is_alive() for thread in threads]:
            for thread in threads:
                thread.join()

        end = time.time()
        logger.success(f"Finished generating neighbors in {(end - start)} seconds.")

        # Code to add small obstacles
        # Convert obstacles to correct format
        for obstacle in large_obstacles:
            self.obstacles.append(convertToSmallGrid(obstacle))

        self.obstacle_vectors = [
            (-1, 0), (0, -1), (+1, -1), (+1, 0), (0, +1), (-1, -1),  # Inner neighbors
            (-1, -1), (0, -2), (+1, -2), (+2, -2), (+2, -1), (+2, 0), (+1, +1), (0, +2), (-1, +2), (-2, +2), (-2, -1), (-2, -2),  # Outer neighbors
            (0, -3), (+1, -3), (+2, -3), (+3, -3), (+3, -2), (+3, -1), (+3, 0), (+2, +1), (+1, +2), (0, +3), (-1, +3), (-2, +3), (-3, +3), (-3, +2), (-3, +1), (-3, 0), (-2, -1), (-1, -2)
        ]
        for obstacle in self.obstacles:
            hexagon = self.grid[obstacle[0]][obstacle[1]]

            hexagon.obstacle = True
            for vector in self.obstacle_vectors:
                try:
                    self.grid[obstacle[0] + vector[0]][obstacle[1] + vector[1]].obstacle = True
                except AttributeError:
                    continue

    def __generate_neighbors(self, *map: list[list]):
        rows = []
        for row in map[1:]:
            rows.append(row)

        for row in rows:
            for hexagon in row:
                if hexagon is None:
                    continue
                neighbors = self.getNeighborsOf(hexagon)
                # logger.debug(f"neighbors of {str(hexagon)}: {str(neighbors)}")
                hexagon.neighbors = neighbors


if __name__ == "__main__":
    # Remove debug messages for faster execution
    start_time = time.time()
    logger.remove()
    logger.add(sys.stderr, level="DEBUG")
    logger.info("Program start")
    logger.info("Creating grid")
    start = (7, 4)
    grid = LargeGrid(start=start)
    small_grid = SmallGrid()

    logger.info("Running basic grid check...")
    try:
        assert small_grid.moveCost(small_grid.grid[62][20], small_grid.grid[63][18]) == 3
        assert small_grid.moveCost(small_grid.grid[45][30], small_grid.grid[47][29]) == 3
        assert small_grid.moveCost(small_grid.grid[45][30], small_grid.grid[46][29]) == 1.7320508075688772
        assert small_grid.moveCost(small_grid.grid[5][50], small_grid.grid[7][49]) == 3
    except AssertionError as error:
        logger.critical("Grid did not pass safety checks! Printing traceback:")
        print(error)
        exit()
    logger.success("Completed checks!")

    small_grid.pathFind((19, 45), (32, 43))

    end_time = time.time()
    logger.success(f"Program finished in {end_time - start_time} seconds")
