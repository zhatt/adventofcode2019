import unittest

import aoc
import day04


class TestDay04(unittest.TestCase):

    def test_is_valid_password1(self):
        self.assertFalse(day04.is_valid_password(101010, exclude_triples=True))
        self.assertTrue(day04.is_valid_password(112345, exclude_triples=True))
        self.assertTrue(day04.is_valid_password(123455, exclude_triples=True))
        self.assertFalse(day04.is_valid_password(623455, exclude_triples=True))

        # Examples from description.
        self.assertTrue(day04.is_valid_password(111111, exclude_triples=True))
        self.assertFalse(day04.is_valid_password(223450, exclude_triples=True))
        self.assertFalse(day04.is_valid_password(123789, exclude_triples=True))

    def test_part1_input(self):
        result = day04.part1(aoc.read_input('day04.input'))
        self.assertEqual(1099, result)

    def test_is_valid_password2(self):
        self.assertFalse(day04.is_valid_password(101010))
        self.assertTrue(day04.is_valid_password(112345))
        self.assertTrue(day04.is_valid_password(123455))
        self.assertFalse(day04.is_valid_password(623455))

        # Examples from description.
        self.assertTrue(day04.is_valid_password(112233))
        self.assertFalse(day04.is_valid_password(123444))
        self.assertTrue(day04.is_valid_password(111122))

    def test_part2_input(self):
        result = day04.part2(aoc.read_input('day04.input'))
        self.assertEqual(710, result)


if __name__ == '__main__':
    unittest.main()
