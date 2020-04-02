import unittest

import aoc
import day25


class TestDay17(unittest.TestCase):

    def test_part1_input(self):
        result = day25.part1(aoc.read_input('day25.input'))
        self.assertEqual('229384', result)

if __name__ == '__main__':
    unittest.main()
