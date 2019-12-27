import unittest

import aoc
import day14


class TestDay14(unittest.TestCase):
    example_input1 = [
        "10 ORE => 10 A",
        "1 ORE => 1 B",
        "7 A, 1 B => 1 C",
        "7 A, 1 C => 1 D",
        "7 A, 1 D => 1 E",
        "7 A, 1 E => 1 FUEL",
    ]

    example_input2 = [
        "9 ORE => 2 A",
        "8 ORE => 3 B",
        "7 ORE => 5 C",
        "3 A, 4 B => 1 AB",
        "5 B, 7 C => 1 BC",
        "4 C, 1 A => 1 CA",
        "2 AB, 3 BC, 4 CA => 1 FUEL",
    ]

    example_input3 = [
        "157 ORE => 5 NZVS",
        "165 ORE => 6 DCFZ",
        "44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL",
        "12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ",
        "179 ORE => 7 PSHF",
        "177 ORE => 5 HKGWZ",
        "7 DCFZ, 7 PSHF => 2 XJWVT",
        "165 ORE => 2 GPVTF",
        "3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT",
    ]

    example_input4 = [
        "2 VPVL, 7 FWMGM, 2 CXFTF, 11 MNCFX => 1 STKFG",
        "17 NVRVD, 3 JNWZP => 8 VPVL",
        "53 STKFG, 6 MNCFX, 46 VJHF, 81 HVMC, 68 CXFTF, 25 GNMV => 1 FUEL",
        "22 VJHF, 37 MNCFX => 5 FWMGM",
        "139 ORE => 4 NVRVD",
        "144 ORE => 7 JNWZP",
        "5 MNCFX, 7 RFSQX, 2 FWMGM, 2 VPVL, 19 CXFTF => 3 HVMC",
        "5 VJHF, 7 MNCFX, 9 VPVL, 37 CXFTF => 6 GNMV",
        "145 ORE => 6 MNCFX",
        "1 NVRVD => 8 CXFTF",
        "1 VJHF, 6 MNCFX => 4 RFSQX",
        "176 ORE => 6 VJHF",
    ]

    example_input5 = [
        "171 ORE => 8 CNZTR",
        "7 ZLQW, 3 BMBT, 9 XCVML, 26 XMNCP, 1 WPTQ, 2 MZWV, 1 RJRHP => 4 PLWSL",
        "114 ORE => 4 BHXH",
        "14 VRPVC => 6 BMBT",
        "6 BHXH, 18 KTJDG, 12 WPTQ, 7 PLWSL, 31 FHTLT, 37 ZDVW => 1 FUEL",
        "6 WPTQ, 2 BMBT, 8 ZLQW, 18 KTJDG, 1 XMNCP, 6 MZWV, 1 RJRHP => 6 FHTLT",
        "15 XDBXC, 2 LTCX, 1 VRPVC => 6 ZLQW",
        "13 WPTQ, 10 LTCX, 3 RJRHP, 14 XMNCP, 2 MZWV, 1 ZLQW => 1 ZDVW",
        "5 BMBT => 4 WPTQ",
        "189 ORE => 9 KTJDG",
        "1 MZWV, 17 XDBXC, 3 XCVML => 2 XMNCP",
        "12 VRPVC, 27 CNZTR => 2 XDBXC",
        "15 KTJDG, 12 BHXH => 5 XCVML",
        "3 BHXH, 2 VRPVC => 7 MZWV",
        "121 ORE => 7 VRPVC",
        "7 XCVML => 6 RJRHP",
        "5 BHXH, 4 VRPVC => 5 LTCX",
    ]

    def test_parse_input(self):
        # pylint: disable=protected-access
        fuel_factory = day14.FuelFactory(self.example_input1)

        expected = {
            "A": fuel_factory.Recipe(10, [fuel_factory.Ingredient("ORE", 10)]),
            "B": fuel_factory.Recipe(1, [fuel_factory.Ingredient("ORE", 1)]),
            "C": fuel_factory.Recipe(1, [fuel_factory.Ingredient("A", 7),
                                         fuel_factory.Ingredient("B", 1)]),
            "D": fuel_factory.Recipe(1, [fuel_factory.Ingredient("A", 7),
                                         fuel_factory.Ingredient("C", 1)]),
            "E": fuel_factory.Recipe(1, [fuel_factory.Ingredient("A", 7),
                                         fuel_factory.Ingredient("D", 1)]),
            "FUEL": fuel_factory.Recipe(1, [fuel_factory.Ingredient("A", 7),
                                            fuel_factory.Ingredient("E", 1)]),
        }

        self.assertEqual(expected, fuel_factory._reaction_table)

    def test_part1_example1(self):
        result = day14.part1(self.example_input1)
        self.assertEqual(31, result)

    def test_part1_example2(self):
        result = day14.part1(self.example_input2)
        self.assertEqual(165, result)

    def test_part1_example3(self):
        result = day14.part1(self.example_input3)
        self.assertEqual(13312, result)

    def test_part1_example4(self):
        result = day14.part1(self.example_input4)
        self.assertEqual(180697, result)

    def test_part1_example5(self):
        result = day14.part1(self.example_input5)
        self.assertEqual(2210736, result)

    def test_part1_input(self):
        result = day14.part1(aoc.read_input('day14.input'))
        self.assertEqual(907302, result)

    def test_part2_example1(self):
        result = day14.part2(self.example_input3)
        self.assertEqual(82892753, result)

    def test_part2_example2(self):
        result = day14.part2(self.example_input4)
        self.assertEqual(5586022, result)

    def test_part2_example3(self):
        result = day14.part2(self.example_input5)
        self.assertEqual(460664, result)

    def test_part2_input(self):
        result = day14.part2(aoc.read_input('day14.input'))
        self.assertEqual(1670299, result)


if __name__ == '__main__':
    unittest.main()
