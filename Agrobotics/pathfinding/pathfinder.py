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
sqrt3 = math.sqrt(3)
apothem_length = 700.0 / 30.0
side_length = (2 / sqrt3) * apothem_length


def hexToRect(Coord: tuple) -> tuple:
    r = Coord[0]
    q = Coord[1]

    x = 46 - (q - r)
    y = 82 - (r + q)
    x = x * round(3 * sqrt3)
    y = y * 3

    return (x, y)  # Coordinates are in terms of half radii; x is approximated to nearest half radius


def angle_between_hexes(delta_hex) -> int:
    if delta_hex[0] == 0:
        if delta_hex[1] > 0:
            return 330
        return 150
    if delta_hex[1] == 0:
        if delta_hex[0] > 0:
            return 30
        return 210
    if abs(delta_hex[0]) == abs(delta_hex[1]):
        if delta_hex[0] == delta_hex[1]:
            if delta_hex[0] > 0:
                return 0
            return 180
        else:
            if delta_hex[0] > 0:
                return 90
            return 270
    if delta_hex[0] % 2 == 0 and abs(delta_hex[1]) * 2 == abs(delta_hex[0]):
        if delta_hex[0] > 1:
            return 60
        return 240
    if delta_hex[1] % 2 == 0 and abs(delta_hex[0]) * 2 == abs(delta_hex[1]):
        if delta_hex[1] > 1:
            return 300
        return 120


def shortest_angle(given_angle: int, desired_angle: int) -> int:
    diff = desired_angle - given_angle
    if diff > 180:
        diff -= 360
    elif diff < -180:
        diff += 360
    return diff


def distance_between_hexes(delta_hex: tuple[int, int], angle: int) -> float | None:
    delta = delta_hex[0] if delta_hex[0] != 0 else delta_hex[1]
    if angle in [30, 90, 150, 210, 270, 330]:
        return apothem_length * delta * 2
    elif angle in [0, 60, 120, 180, 240, 300]:
        result = 1.6 * abs(delta * (apothem_length + side_length))
        return result
    return None


@dataclass
class movement_node:
    move_node: tuple[int, int] | None  # Hexagon to move to
    start_node: tuple[int, int] | tuple[int, ...]  # Hexagon moved from
    angle: float  # Angle to move at
    distance: int  # Distance to move


def pathfind(path_ref) -> list[
    movement_node]:  # "pathfinding/paths" is relative to the "scripter.py" file (the main code)
    """
    Will take the path to a .txt containing the path, then generate the robot code necessary to do that path
    Returns an array, where the rows are the lines to write
    """
    logger.info("Generating path from path file...")

    out: list[movement_node] = []
    current_angle = None

    try:
        with open(path_ref, "r") as path_file:
            path: list[tuple[int, ...]] = []
            lines = path_file.readlines()
            try:
                if len(lines[0].split(" ")) == 1:
                    current_angle = int(lines[0].split(" ")[0])
                else:
                    path.append(tuple(int(coord) for coord in lines[0].split(" ")))
            except IndexError:
                pass
            finally:
                for line in lines[1:]:
                    split = line.split(" ")
                    if len(split) != 1:
                        path.append(tuple(int(coord) for coord in split))
                    else:
                        path.append((int(split[0]), -100000))
    except FileNotFoundError:
        logger.critical(f"Path file not found! Path: '{path_ref}'")
        return []

    if current_angle is None:
        current_angle = 0
    for cur_index, cur_node in enumerate(path[:-1]):
        if cur_node[1] == -100000:
            angle = cur_node[0]
            turn_angle = shortest_angle(current_angle, angle)
            current_angle = turn_angle
            out.append(movement_node(
                move_node=None,
                start_node=None,
                angle=turn_angle,
                distance=0
            )
            )
            continue
        next_node = path[cur_index + 1]
        if next_node[1] == -100000:
            continue
        try:
            hex_difference = (next_node[0] - cur_node[0], next_node[1] - cur_node[1])
        except TypeError:  # This error occurs when the next hexagon is an angle
            continue

        desired_angle = angle_between_hexes(delta_hex=hex_difference)
        turn_angle = shortest_angle(current_angle, desired_angle)
        current_angle = turn_angle

        distance = distance_between_hexes(delta_hex=hex_difference, angle=desired_angle)
        if distance is None:
            logger.critical(
                f"[{path_ref}]: PATH NOT VALID FROM '{cur_node}' -> '{next_node}' (Angle: '{desired_angle}') (delta_hex: '{hex_difference}')")
            raise Exception("PATH IS NOT VALID!")

        out.append(movement_node(
            move_node=next_node,
            start_node=cur_node,
            angle=turn_angle,
            distance=int(distance)
            )
        )
        logger.debug(
            f"Current node: '{str(cur_node)}', Next node: '{str(next_node)}', Desired Angle: '{desired_angle}', Distance: '{str(distance)}'")

    try:
        end_element = path[-1]
        if end_element[1] == -100000:
            turn_angle = shortest_angle(current_angle, end_element[0])
            out.append(movement_node(
                move_node=None,
                start_node=None,
                angle=turn_angle,
                distance=0
                )
            )
    except IndexError:
        return out

    return out


if __name__ == "__main__":
    pathfind("paths/testing/example.txt")
