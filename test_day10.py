import unittest

import aoc
import day10


class TestDay10(unittest.TestCase):

    def test_parse_input(self):
        input_list = [
            ".#.",
            "...",
            "# #",
        ]

        expected_map = {
            aoc.Coord(1, 0), aoc.Coord(0, 2), aoc.Coord(2, 2)
        }

        asteroid_map = day10.parse_input(input_list)
        self.assertEqual(expected_map, asteroid_map)

    def test_part1_example1(self):
        input_list = [
            ".#..#",
            ".....",
            "#####",
            "....#",
            "...##",
        ]

        result = day10.part1(input_list)
        self.assertEqual(8, result)

    def test_part1_example2(self):
        input_list = [
            "......#.#.",
            "#..#.#....",
            "..#######.",
            ".#.#.###..",
            ".#..#.....",
            "..#....#.#",
            "#..#....#.",
            ".##.#..###",
            "##...#..#.",
            ".#....####",
        ]

        result = day10.part1(input_list)
        self.assertEqual(33, result)

    def test_part1_example3(self):
        input_list = [
            "#.#...#.#.",
            ".###....#.",
            ".#....#...",
            "##.#.#.#.#",
            "....#.#.#.",
            ".##..###.#",
            "..#...##..",
            "..##....##",
            "......#...",
            ".####.###.",
        ]

        result = day10.part1(input_list)
        self.assertEqual(35, result)

    def test_part1_example4(self):
        input_list = [
            ".#..#..###",
            "####.###.#",
            "....###.#.",
            "..###.##.#",
            "##.##.#.#.",
            "....###..#",
            "..#.#..#.#",
            "#..#.#.###",
            ".##...##.#",
            ".....#.#..",
        ]

        result = day10.part1(input_list)
        self.assertEqual(41, result)

    input_list_example5 = [
        ".#..##.###...#######",
        "##.############..##.",
        ".#.######.########.#",
        ".###.#######.####.#.",
        "#####.##.#.##.###.##",
        "..#####..#.#########",
        "####################",
        "#.####....###.#.#.##",
        "##.#################",
        "#####.##.###..####..",
        "..######..##.#######",
        "####.##.####...##..#",
        ".#####..#.######.###",
        "##...#.##########...",
        "#.##########.#######",
        ".####.#.###.###.#.##",
        "....##.##.###..#####",
        ".#.#.###########.###",
        "#.#.#.#####.####.###",
        "###.##.####.##.#..##",
    ]

    def test_part1_example5(self):
        result = day10.part1(self.input_list_example5)
        self.assertEqual(210, result)

    def test_part1_input(self):
        result = day10.part1(aoc.read_input('day10.input'))
        self.assertEqual(269, result)

    def test_part2_example1(self):
        result = day10.part2(self.input_list_example5)
        self.assertEqual(802, result)

    def test_part2_input(self):
        result = day10.part2(aoc.read_input('day10.input'))
        self.assertEqual(612, result)


if __name__ == '__main__':
    unittest.main()
