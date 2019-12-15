import unittest

import aoc
import day08


class TestDay08(unittest.TestCase):

    def test_part1_example1(self):
        image = "123456789012"

        result = day08.find_fewest_zero_layer(image, 3, 2)
        self.assertEqual(1, result)

    def test_part1_input(self):
        result = day08.part1(aoc.read_input('day08.input'))
        self.assertEqual(2760, result)

    def test_part2_example1(self):
        image = "0222112222120000"

        result = day08.render_image(image, 2, 2)
        self.assertEqual(" X\nX \n", result)

    def test_part2_input(self):
        # When viewed, my answer is 'AGUEB'
        expected_result = \
            " XX   XX  X  X XXXX XXX  \n" \
            "X  X X  X X  X X    X  X \n" \
            "X  X X    X  X XXX  XXX  \n" \
            "XXXX X XX X  X X    X  X \n" \
            "X  X X  X X  X X    X  X \n" \
            "X  X  XXX  XX  XXXX XXX  \n"

        result = day08.part2(aoc.read_input('day08.input'))
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
