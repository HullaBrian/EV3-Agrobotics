# pathfinder.py: used to pathfind using a hybrid pathfinding system

# Builtins
import math
from dataclasses import dataclass

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

axial_direction_vectors = [
    (0, -1), (-1, 0), (-1, +1),
    (0, +1), (+1, 0), (+1, -1)
]
weighted_axial_direction_vectors = [
    (-1, -1), (-2, +1), (-1, +2),
    (+1, +1), (+2, -1), (+1, -2)
]
logger.debug("Loaded vectors!")

sqrt3 = math.sqrt(3)


def angle_between_hexes(delta_hex: tuple[int, int]) -> float:
    try:
        desired_angle = directional_vectors[delta_hex]
    except KeyError:
        try:
            desired_angle = math.degrees(-1 * math.atan((delta_hex[0]) / delta_hex[1]))  # Round it up
        except ZeroDivisionError:
            if delta_hex[0] == 0:
                if delta_hex[1] > 0:
                    desired_angle = 30.0
                else:
                    desired_angle = 210.0
            else:
                if delta_hex[0] > 0:
                    desired_angle = 90.0
                else:
                    desired_angle = 270.0

    return float(desired_angle)


def shortest_angle(given_angle: int, desired_angle: int) -> int:
    diff = desired_angle - given_angle
    if diff > 180:
        diff -= 360
    elif diff < -180:
        diff += 360
    return diff


def distance_between_hexes(angle, delta_hex: tuple[int, int]) -> int:
    flat_sided_distance = sqrt3
    angle_distance = 1

    if angle % 90 == 90:
        diff = delta_hex[0] if delta_hex[0] != 0 else delta_hex[1]
        return int(diff * flat_sided_distance)
    else:
        return int(math.sqrt(delta_hex[0] ** 2 + delta_hex[1] ** 2) * angle_distance)


@dataclass
class movement_node:
    move_node: tuple[int, int]  # Hexagon to move to
    start_node: tuple[int, int]  # Hexagon moved from
    angle: float  # Angle to move at
    distance: int  # Distance to move


def pathfind(path_ref, start_tile=(-1, -1)) -> list[str]:  # "pathfinding/paths" is relative to the "scripter.py" file (the main code)
    """
    Will take the path to a .txt containing the path, then generate the robot code necessary to do that path
    Returns an array, where the rows are the lines to write
    """
    logger.info("Generating path from path file...")

    out: list[movement_node] = []

    try:
        with open(path_ref, "r") as path_file:
            path: list[tuple[int, int]] = []
            for line in path_file.readlines():
                path.append(tuple(int(coord) for coord in line.split(" ")))
    except FileNotFoundError:
        logger.critical(f"Path file not found! Path: '{path_ref}'")
        return []

    if start_tile != (-1, -1):
        path.insert(0, start_tile)

    current_angle = 330
    for cur_index, cur_node in enumerate(path[:-1]):
        next_node = path[cur_index + 1]

        difference = (next_node[0] - cur_node[0], next_node[1] - cur_node[1])

        desired_angle = angle_between_hexes(delta_hex=difference)
        turn_angle = shortest_angle(current_angle, desired_angle)
        current_angle = turn_angle

        distance = distance_between_hexes(angle=desired_angle, delta_hex=difference)
        out.append(movement_node(
            move_node=next_node,
            start_node=cur_node,
            angle=turn_angle,
            distance=distance * 2.5
        ))
        logger.debug(f"Current node: '{str(cur_node)}', Next node: '{str(next_node)}', Desired Angle: '{desired_angle}', Distance: '{str(distance * 2.5)}'")

        return out


if __name__ == "__main__":
    pathfind("paths/testing/example.txt")
