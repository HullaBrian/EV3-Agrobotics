import unittest

import random

from Agrobotics.pathfinding.pathfinder import angle_between_hexes
from Agrobotics.pathfinding.pathfinder import distance_between_hexes
from Agrobotics.pathfinding.pathfinder import hexToRect


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
ACCURACY = 40


def is_about(value1, value2) -> bool:
    return value1 - ACCURACY <= value2 <= value1 + ACCURACY


class pathfinding_tests(unittest.TestCase):
    def test_coordinate_conversions(self):
        pass  # self.assertEqual("EE", "EEe")

    def test_docking_station_distance(self):
        print(distance_between_hexes((40 - 29, 40 - 29), 0))
        self.assertTrue(is_about(distance_between_hexes((40 - 29, 40 - 29), 0), 900))

    def test_farming_module_distance(self):
        self.assertTrue(is_about(distance_between_hexes((44 - 29, 14 - 29), 90), 700))  # Farming Module

    def test_growing_medium_by_docking_station(self):
        self.assertEqual(None, distance_between_hexes((39 - 29, 29 - 33), 17))

    def test_arbitrary_distance(self):
        self.assertTrue(is_about(distance_between_hexes((27 - 29, 33 - 29), 300), 175))  # Arbitrary distance

    def test_docking_station_angle(self):
        self.assertEqual(0, angle_between_hexes((40 - 29, 40 - 29)))  # Docking station

    def test_farming_module_angle(self):
        self.assertEqual(90, angle_between_hexes((44 - 29, 14 - 29)))  # Farming Module

    def test_growing_medium_angle(self):
        self.assertEqual(300, angle_between_hexes((17 - 29, 53 - 29)))

    def test_arbitrary_angles(self):
        for test_case in range(0, 100):
            for vector in directional_vectors:
                multiplier = random.randint(2, 8)
                new_vector = (vector[0] * multiplier, vector[1] * multiplier)
                self.assertEqual(directional_vectors[vector], angle_between_hexes(new_vector))

    def test_angle_vectors(self):
        for vector in directional_vectors:
            self.assertEqual(directional_vectors[vector], angle_between_hexes(vector))


if __name__ == "__main__":
    unittest.main()
