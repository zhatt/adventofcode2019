import unittest
from fractions import Fraction

import aoc


class TestAoc(unittest.TestCase):
    coord1 = aoc.Coord(1, 3)
    coord2 = aoc.Coord(21, 2)
    coord3 = aoc.Coord(1, 43)

    def test_add_coord(self):
        self.assertEqual(aoc.Coord(22, 5), aoc.add_coords(self.coord1, self.coord2))
        self.assertEqual(aoc.Coord(23, 48), aoc.add_coords(self.coord1, self.coord2, self.coord3))

    def test_distance_manhattan(self):
        self.assertEqual(20 + 1, aoc.distance_manhattan_coords(self.coord1, self.coord2))

    def test_min_bound_coord(self):
        self.assertEqual(aoc.Coord(1, 2), aoc.min_bound_coord(self.coord1, self.coord2))
        self.assertEqual(aoc.Coord(1, 2), aoc.min_bound_coord(self.coord1, self.coord2, \
                                                              self.coord3))

    def test_max_bound_coord(self):
        self.assertEqual(aoc.Coord(1, 43), aoc.max_bound_coord(self.coord1, self.coord3))
        self.assertEqual(aoc.Coord(21, 43), aoc.max_bound_coord(self.coord1, self.coord2, \
                                                                self.coord3))

    def test_slope(self):
        self.assertEqual(Fraction(2, -1), aoc.slope_negy(aoc.Coord(0, 0), aoc.Coord(4, 8)))
        self.assertEqual(Fraction(8, 3), aoc.slope_negy(aoc.Coord(0, 0), aoc.Coord(3, -8)))

    def test_coord_relation(self):
        self.assertEqual(0, aoc.coord_relation_negy(aoc.Coord(1, 2), aoc.Coord(1, 2)))
        self.assertEqual(1, aoc.coord_relation_negy(aoc.Coord(1, 2), aoc.Coord(2, 2)))
        self.assertEqual(-1, aoc.coord_relation_negy(aoc.Coord(10, 2), aoc.Coord(2, 2)))
        self.assertEqual(1, aoc.coord_relation_negy(aoc.Coord(-10, -10), aoc.Coord(-2, -2)))


if __name__ == '__main__':
    unittest.main()
