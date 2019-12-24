import unittest

import aoc
import day12


class TestDay12(unittest.TestCase):
    example_input1 = [
        "<x=-1, y=0, z=2>",
        "<x=2, y=-10, z=-7>",
        "<x=4, y=-8, z=8>",
        "<x=3, y=5, z=-1>",
    ]

    example_input2 = [
        "<x=-8, y=-10, z=0>",
        "<x=5, y=5, z=10>",
        "<x=2, y=-7, z=3>",
        "<x=9, y=-8, z=-3>",
    ]

    def test_parse_input(self):
        moon_data = day12.parse_input(self.example_input1)

        expected = (
            [
                # x data
                day12.MoonData(-1, 0),
                day12.MoonData(2, 0),
                day12.MoonData(4, 0),
                day12.MoonData(3, 0),
            ],
            [
                # y data
                day12.MoonData(0, 0),
                day12.MoonData(-10, 0),
                day12.MoonData(-8, 0),
                day12.MoonData(5, 0),
            ],
            [
                # z data
                day12.MoonData(2, 0),
                day12.MoonData(-7, 0),
                day12.MoonData(8, 0),
                day12.MoonData(-1, 0),
            ],
        )

        self.assertEqual(expected, moon_data)

    def test_part1_example1_movement(self):
        moon_data = day12.parse_input(self.example_input1)

        expected1 = (
            [
                # x data
                day12.MoonData(2, 3),
                day12.MoonData(3, 1),
                day12.MoonData(1, -3),
                day12.MoonData(2, -1),
            ],
            [
                # y data
                day12.MoonData(-1, -1),
                day12.MoonData(-7, 3),
                day12.MoonData(-7, 1),
                day12.MoonData(2, -3),
            ],
            [
                # z data
                day12.MoonData(1, -1),
                day12.MoonData(-4, 3),
                day12.MoonData(5, -3),
                day12.MoonData(0, 1),
            ],
        )

        expected10 = (
            [
                # x data
                day12.MoonData(2, -3),
                day12.MoonData(1, -1),
                day12.MoonData(3, 3),
                day12.MoonData(2, 1),
            ],
            [
                # y data
                day12.MoonData(1, -2),
                day12.MoonData(-8, 1),
                day12.MoonData(-6, 2),
                day12.MoonData(0, -1),
            ],
            [
                # z data
                day12.MoonData(-3, 1),
                day12.MoonData(0, 3),
                day12.MoonData(1, -3),
                day12.MoonData(4, -1),
            ],
        )

        day12.simulate_one_step(moon_data)
        self.assertEqual(expected1, moon_data)

        for _ in range(9):
            day12.simulate_one_step(moon_data)
        self.assertEqual(expected10, moon_data)

    def test_part1_example1_energy(self):
        moon_data = day12.parse_input(self.example_input1)
        for _ in range(10):
            day12.simulate_one_step(moon_data)

        energy = day12.calculate_energy(moon_data)
        self.assertEqual(179, energy)

    def test_part2_example2_energy(self):
        moon_data = day12.parse_input(self.example_input2)
        for _ in range(100):
            day12.simulate_one_step(moon_data)

        energy = day12.calculate_energy(moon_data)
        self.assertEqual(1940, energy)

    def test_part1_input(self):
        result = day12.part1(aoc.read_input('day12.input'))
        self.assertEqual(12351, result)

    def test_part2_example1(self):
        result = day12.part2(self.example_input1)
        self.assertEqual(2772, result)

    def test_part2_example2(self):
        result = day12.part2(self.example_input2)
        self.assertEqual(4686774924, result)

    def test_part2_input(self):
        result = day12.part2(aoc.read_input('day12.input'))
        self.assertEqual(380635029877596, result)


if __name__ == '__main__':
    unittest.main()
