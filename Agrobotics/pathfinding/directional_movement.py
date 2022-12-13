# Directional movement script that takes the path generated in pathfinding.py and gets the rotations needed
# to execute the path on the robot
from Agrobotics.pathfinding.objects import Hexagon
from Agrobotics.pathfinding.objects import movement_node


def convert_to_directional_path(path: list[Hexagon]) -> list[movement_node]:
        from Agrobotics.pathfinding.objects import movement_node
        from Agrobotics.pathfinding.objects import moveCost
        from Agrobotics.pathfinding.pathfinding import SmallGrid  # For pathfinding
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
