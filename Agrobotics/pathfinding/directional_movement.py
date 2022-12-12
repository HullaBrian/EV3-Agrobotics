# Directional movement script that takes the path generated in pathfinding.py and gets the rotations needed
# to execute the path on the robot

from objects import Hexagon
from objects import movement_node
from objects import moveCost
from pathfinding import SmallGrid  # For pathfinding


def convert_to_directional_path(path: list[Hexagon]) -> list[movement_node]:
        path = path
        direction_path: list = []

        directional_vectors = {
            (+1, -1): 0,
            (+1, -2): 30,
            (0, -1): 60,
            (-1, -1): 90,
            (-1, 0): 120,
            (-2, +1): 150,
            (-1, +1): 180,
            (-1, +2): 210,
            (0, +1): 240,
            (+1, +1): 270,
            (+1, 0): 300,
            (+2, -1): 330
        }

        for index, start_node in enumerate(path[:-1]):
            move_to = path[index + 1]

            final_r = move_to.r - start_node.r
            final_q = move_to.q - start_node.q
            angle = directional_vectors[(final_q, final_r)]

            distance = moveCost(start_node, move_to)

            direction_path.append(movement_node(
                move_to,
                start_node,
                angle,
                distance
            ))

        return direction_path


if __name__ == "__main__":
    grid = SmallGrid()
    path = grid.pathFind((37, 31), (41, 35))
    dpath = convert_to_directional_path(path)
    for node in dpath:
        print(node.move_node, node.distance)
