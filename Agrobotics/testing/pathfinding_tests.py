import unittest

from Agrobotics.pathfinding.pathfinder import angle_between_hexes
from Agrobotics.pathfinding.pathfinder import distance_between_hexes
from Agrobotics.pathfinding.pathfinder import hexToRect


ACCURACY = 0.10


def is_about(value1, value2) -> bool:
    return abs((value1 - value2) / float(value1)) <= ACCURACY


class pathfinding_tests(unittest.TestCase):
    def test_coordinate_conversions(self):
        pass  # self.assertEqual("EE", "EEe")

    def test_docking_station_distance(self):
        EXPECTED = 900
        ACTUAL = distance_between_hexes((40 - 29, 40 - 29))
        self.assertTrue(is_about(ACTUAL, EXPECTED))

    def test_farming_module_distance(self):
        EXPECTED = 700
        ACTUAL = distance_between_hexes((44 - 29, 14 - 29))
        self.assertTrue(is_about(ACTUAL, EXPECTED))  # Farming Module

    def test_growing_medium_by_docking_station(self):
        EXPECTED = 580
        ACTUAL = distance_between_hexes((39 - 29, 29 - 33))
        self.assertTrue(is_about(ACTUAL, EXPECTED))

    def test_arbitrary_distance(self):
        EXPECTED = 175
        ACTUAL = distance_between_hexes((27 - 29, 33 - 29))
        self.assertTrue(is_about(ACTUAL, EXPECTED))  # Arbitrary distance

    def test_docking_station_angle(self):
        self.assertEqual(0, angle_between_hexes((40 - 29, 40 - 29)))  # Docking station

    def test_farming_module_angle(self):
        self.assertEqual(90, angle_between_hexes((44 - 29, 14 - 29)))  # Farming Module

    def test_growing_medium_angle(self):
        self.assertEqual(300, angle_between_hexes((17 - 29, 53 - 29)))

    def test_arbitrary_angle(self):
        self.assertEqual(30, angle_between_hexes((32 - 29, 29 - 29)))


if __name__ == "__main__":
    unittest.main()
