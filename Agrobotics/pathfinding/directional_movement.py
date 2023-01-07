# Directional movement script that takes the path generated in pathfinding.py and gets the rotations needed
# to execute the path on the robot
from pathfinding.objects import Hexagon
from pathfinding.objects import movement_node


def convert_to_directional_path(path: list[Hexagon]) -> list[movement_node]:
        from pathfinding.objects import moveCost
        from pathfinding.pathfinding import SmallGrid  # For pathfinding

        direction_path: list = []

        # Wrong angles
        directional_vectors = {
            (+1, -1): 0,  # 90
            (+1, -2): 30,  # 120
            (0, -1): 60,  # 150
            (-1, -1): 90,  # 180
            (-1, 0): 120,  # -150
            (-2, +1): 150,  # -120
            (-1, +1): 180,  # -90
            (-1, +2): 210,  # -60
            (0, +1): 240,  # -30
            (+1, +1): 270,  # 0
            (+1, 0): 300,  # 30
            (+2, -1): 330  # 60
        }

        current_angle = 90
        for index, start_node in enumerate(path[:-1]):
            move_to = path[index + 1]

            final_r = move_to.r - start_node.r
            final_q = move_to.q - start_node.q
            desired_angle = directional_vectors[(final_q, final_r)]
            angle = 180 - (desired_angle - current_angle)
            current_angle = desired_angle

            distance = moveCost(start_node, move_to)

            direction_path.append(movement_node(
                move_to,
                start_node,
                angle,
                distance
            ))

        return direction_path
