# Directional movement script that takes the path generated in pathfinding.py and gets the rotations needed
# to execute the path on the robot
from Agrobotics.pathfinding.archive.pathfinding import Hexagon
from Agrobotics.pathfinding.archive.pathfinding import movement_node
from Agrobotics.pathfinding.archive.pathfinding import shortest_angle


def convert_to_directional_path(path: list[Hexagon]) -> tuple[list[movement_node], int]:
        from Agrobotics.pathfinding.archive.pathfinding import moveCost

        direction_path: list = []

        # All vector-angle mappings are relative to the robot facing South
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

        current_angle = 0  # Facing south
        for index, start_node in enumerate(path[:-1]):
            move_to = path[index + 1]

            final_r = move_to.r - start_node.r
            final_q = move_to.q - start_node.q
            desired_angle = directional_vectors[(final_q, final_r)]
            angle = shortest_angle(given_angle=current_angle, desired_angle=desired_angle)
            current_angle = desired_angle

            distance = moveCost(start_node, move_to)

            direction_path.append(movement_node(
                move_to,
                start_node,
                angle,
                distance
            ))

        return direction_path, current_angle
