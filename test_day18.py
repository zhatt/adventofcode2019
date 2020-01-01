import unittest

import aoc
import day18


class TestDay18(unittest.TestCase):

    def test_part1_exampe1(self):
        example_input = [
            "#########",
            "#b.A.@.a#",
            "#########",
        ]
        result = day18.part1(example_input)
        self.assertEqual(8, result)

    def test_part1_example2(self):
        example_input = [
            "########################",
            "#f.D.E.e.C.b.A.@.a.B.c.#",
            "######################.#",
            "#d.....................#",
            "########################",
        ]
        result = day18.part1(example_input)
        self.assertEqual(86, result)

    def test_part1_example3(self):
        example_input = [
            "########################",
            "#...............b.C.D.f#",
            "#.######################",
            "#.....@.a.B.c.d.A.e.F.g#",
            "########################",
        ]
        result = day18.part1(example_input)
        self.assertEqual(132, result)

    def test_part1_example4(self):
        example_input = [
            "#################",
            "#i.G..c...e..H.p#",
            "########.########",
            "#j.A..b...f..D.o#",
            "########@########",
            "#k.E..a...g..B.n#",
            "########.########",
            "#l.F..d...h..C.m#",
            "#################",
        ]
        result = day18.part1(example_input)
        self.assertEqual(136, result)

    def test_part1_example5(self):
        example_input = [
            "########################",
            "#@..............ac.GI.b#",
            "###d#e#f################",
            "###A#B#C################",
            "###g#h#i################",
            "########################",
        ]
        result = day18.part1(example_input)
        self.assertEqual(81, result)

    def test_part1_input(self):
        result = day18.part1(aoc.read_input('day18.input'))
        self.assertEqual(5964, result)

    def test_part2_example1(self):
        example_input = [
            "#######",
            "#a.#Cd#",
            "##...##",
            "##.@.##",
            "##...##",
            "#cB#Ab#",
            "#######",
        ]
        result = day18.part2(example_input)
        self.assertEqual(8, result)

    def test_part2_example2(self):
        example_input = [
            "###############",
            "#d.ABC.#.....a#",
            "######...######",
            "######.@.######",
            "######...######",
            "#b.....#.....c#",
            "###############",
        ]
        result = day18.part2(example_input)
        self.assertEqual(24, result)

    def test_part2_example3(self):
        example_input = [
            "#############",
            "#DcBa.#.GhKl#",
            "#.###...#I###",
            "#e#d#.@.#j#k#",
            "###C#...###J#",
            "#fEbA.#.FgHi#",
            "#############",
        ]
        result = day18.part2(example_input)
        self.assertEqual(32, result)

    def test_part2_example4(self):
        example_input = [
            "#############",
            "#g#f.D#..h#l#",
            "#F###e#E###.#",
            "#dCba...BcIJ#",
            "#####.@.#####",
            "#nK.L...G...#",
            "#M###N#H###.#",
            "#o#m..#i#jk.#",
            "#############",
        ]
        result = day18.part2(example_input)
        self.assertEqual(74, result)

    def test_part2_input(self):
        result = day18.part2(aoc.read_input('day18.input'))
        self.assertEqual(1996, result)


if __name__ == '__main__':
    unittest.main()
