import unittest

from Agrobotics.pathfinding.pathfinder import angle_between_hexes
from Agrobotics.pathfinding.pathfinder import distance_between_hexes
from Agrobotics.pathfinding.pathfinder import hexToRect


class pathfinding_tests(unittest.TestCase):
    def test_coordinate_conversions(self):
        pass # self.assertEqual("EE", "EEe")

    def test_docking_station_distance(self):
        self.assertEqual(900, distance_between_hexes((40 - 29, 40 - 29)))  # Docking station

    def test_farming_module_distance(self):
        self.assertEqual(700, distance_between_hexes((44 - 29, 14 - 29)))  # Farming Module

    def test_growing_medium_by_docking_station(self):
        self.assertEqual(580, distance_between_hexes((39 - 29, 29 - 33)))

    def test_arbitrary_distance(self):
        self.assertEqual(175, distance_between_hexes((27 - 29, 33 - 29)))  # Arbitrary distance

    def test_docking_station_angle(self):
        self.assertEqual(0, angle_between_hexes((40 - 29, 40 - 29)))  # Docking station

    def test_farming_module_angle(self):
        self.assertEqual(90, angle_between_hexes((44 - 29, 14 - 29)))  # Farming Module

    def test_growing_medium_angle(self):
        self.assertEqual(330, angle_between_hexes((19 - 29, 49 - 29)))

    def test_arbitrary_angle(self):
        self.assertEqual(30, angle_between_hexes((32 - 29, 29 - 29)))


if __name__ == "__main__":
    unittest.main()
