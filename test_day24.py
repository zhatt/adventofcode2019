import unittest

import aoc
import day24


class TestDay24(unittest.TestCase):
    example1_input = [
        "....#",
        "#..#.",
        "#..##",
        "..#..",
        "#....",
    ]

    example1_minute1 = [
        "#..#.",
        "####.",
        "###.#",
        "##.##",
        ".##..",
    ]

    example1_minute2 = [
        "#####",
        "....#",
        "....#",
        "...#.",
        "#.###",
    ]

    example1_minute3 = [
        "#....",
        "####.",
        "...##",
        "#.##.",
        ".##.#",
    ]

    example1_minute4 = [
        "####.",
        "....#",
        "##..#",
        ".....",
        "##...",
    ]

    example1_final = [
        ".....",
        ".....",
        ".....",
        "#....",
        ".#...",
    ]

    def test_parse_input(self):
        expected_map = \
            "....#\n" \
            "#..#.\n" \
            "#..##\n" \
            "..#..\n" \
            "#....\n"

        eris = day24.Eris(self.example1_input)
        eris_map = eris.get_map_string(0)
        self.assertEqual(expected_map, eris_map)

    def test_part1_simulate_minutes(self):
        eris = day24.Eris(self.example1_input)

        eris_minute1 = day24.Eris(self.example1_minute1)
        eris_minute2 = day24.Eris(self.example1_minute2)
        eris_minute3 = day24.Eris(self.example1_minute3)
        eris_minute4 = day24.Eris(self.example1_minute4)

        eris.simulate()
        self.assertEqual(eris_minute1.get_map_string(level=0), eris.get_map_string(level=0))

        eris.simulate()
        self.assertEqual(eris_minute2.get_map_string(level=0), eris.get_map_string(level=0))

        eris.simulate()
        self.assertEqual(eris_minute3.get_map_string(level=0), eris.get_map_string(level=0))

        eris.simulate()
        self.assertEqual(eris_minute4.get_map_string(level=0), eris.get_map_string(level=0))

    def test_part1_biodiversity_rating(self):
        eris = day24.Eris(self.example1_final)
        self.assertEqual(2129920, eris.calculate_biodiversity(0))

    def test_part1_input(self):
        result = day24.part1(aoc.read_input('day24.input'))
        self.assertEqual(26840049, result)

    def test_part2_simulate_minutes(self):
        eris = day24.Eris(self.example1_input, recursive=True)
        for _ in range(10):
            eris.simulate()

        depth_neg5 = "..#..\n.#.#.\n....#\n.#.#.\n..#..\n"
        depth_neg4 = "...#.\n...##\n.....\n...##\n...#.\n"
        depth_neg3 = "#.#..\n.#...\n.....\n.#...\n#.#..\n"
        depth_neg2 = ".#.##\n....#\n....#\n...##\n.###.\n"
        depth_neg1 = "#..##\n...##\n.....\n...#.\n.####\n"
        depth____0 = ".#...\n.#.##\n.#...\n.....\n.....\n"
        depth____1 = ".##..\n#..##\n....#\n##.##\n#####\n"
        depth____2 = "###..\n##.#.\n#....\n.#.##\n#.#..\n"
        depth____3 = "..###\n.....\n#....\n#....\n#...#\n"
        depth____4 = ".###.\n#..#.\n#....\n##.#.\n.....\n"
        depth____5 = "####.\n#..#.\n#..#.\n####.\n.....\n"

        self.assertEqual(depth_neg5, eris.get_map_string(-5))
        self.assertEqual(depth_neg4, eris.get_map_string(-4))
        self.assertEqual(depth_neg3, eris.get_map_string(-3))
        self.assertEqual(depth_neg2, eris.get_map_string(-2))
        self.assertEqual(depth_neg1, eris.get_map_string(-1))
        self.assertEqual(depth____0, eris.get_map_string(0))
        self.assertEqual(depth____1, eris.get_map_string(1))
        self.assertEqual(depth____2, eris.get_map_string(2))
        self.assertEqual(depth____3, eris.get_map_string(3))
        self.assertEqual(depth____4, eris.get_map_string(4))
        self.assertEqual(depth____5, eris.get_map_string(5))

        self.assertEqual(99, eris.number_of_bugs())

    def test_part2_input(self):
        result = day24.part2(aoc.read_input('day24.input'))
        self.assertEqual(1995, result)


if __name__ == '__main__':
    unittest.main()
