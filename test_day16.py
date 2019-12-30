import itertools
import unittest

import aoc
import day16


class TestDay16(unittest.TestCase):

    def test_pattern_generator(self):
        expected1 = [1, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1, 0]
        result1 = list(itertools.islice(day16.generate_pattern(1), 12))
        self.assertEqual(expected1, result1)

        expected2 = [0, 1, 1, 0, 0, -1, -1, 0, 0, 1, 1, 0]
        result2 = list(itertools.islice(day16.generate_pattern(2), 12))
        self.assertEqual(expected2, result2)

        expected3 = [0, 0, 1, 1, 1, 0, 0, 0, -1, -1, -1, 0]
        result3 = list(itertools.islice(day16.generate_pattern(3), 12))
        self.assertEqual(expected3, result3)

    def test_part1_example1(self):
        signal = "12345678"
        signal = day16.do_phase(signal)
        self.assertEqual("48226158", signal)
        signal = day16.do_phase(signal)
        self.assertEqual("34040438", signal)
        signal = day16.do_phase(signal)
        self.assertEqual("03415518", signal)
        signal = day16.do_phase(signal)
        self.assertEqual("01029498", signal)

    def test_part1_example2(self):
        signal = "80871224585914546619083218645595"
        signal = day16.do_phase(signal, 100)
        self.assertEqual("24176176", signal[0:8])

        signal = "19617804207202209144916044189917"
        signal = day16.do_phase(signal, 100)
        self.assertEqual("73745418", signal[0:8])

        signal = "69317163492948606335995924319873"
        signal = day16.do_phase(signal, 100)
        self.assertEqual("52432133", signal[0:8])

    def test_part1_input(self):
        result = day16.part1(aoc.read_input('day16.input'))
        self.assertEqual("74369033", result)

    def test_part2_example1(self):
        result = day16.part2(["03036732577212944063491565474664"])
        self.assertEqual("84462026", result)

    def test_part2_example2(self):
        result = day16.part2(["02935109699940807407585447034323"])
        self.assertEqual("78725270", result)

    def test_part2_example3(self):
        result = day16.part2(["03081770884921959731165446850517"])
        self.assertEqual("53553731", result)

    def test_part2_input(self):
        result = day16.part2(aoc.read_input('day16.input'))
        self.assertEqual('19903864', result)


if __name__ == '__main__':
    unittest.main()
