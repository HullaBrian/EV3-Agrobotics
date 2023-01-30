import unittest

from Agrobotics.pathfinding.pathfinder import angle_between_hexes
from Agrobotics.pathfinding.pathfinder import distance_between_hexes
from Agrobotics.pathfinding.pathfinder import hexToRect


class pathfinding_tests(unittest.TestCase):
    def test_coordinate_conversions(self):
        self.assertEqual("EE", "EEe")

    def test_distance_resolution(self):
        self.assertEqual(858, distance_between_hexes((11, 11)))

    def test_angle_resolution(self):
        self.assertEqual(22, 2)


if __name__ == "__main__":
    unittest.main()