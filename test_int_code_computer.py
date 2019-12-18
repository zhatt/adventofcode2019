import unittest

from int_code_computer import IntCodeComputer
from int_code_computer import Memory

# Extra alias for IntCodeComputer to make generated int code simpler.
ICC = IntCodeComputer


# pylint: disable=too-many-public-methods
class TestIntCodeComputer(unittest.TestCase):

    def test_memory(self):
        memory = Memory([1, 2, 3])
        self.assertEqual([1, 2, 3], memory)

        memory[0] = 10
        self.assertEqual([10, 2, 3], memory)

        memory[5] = 15
        self.assertEqual([10, 2, 3, 0, 0, 15], memory)

        # Extend list by referencing past end.
        _ = memory[15]
        self.assertEqual(16, len(memory))

    def test_parse_input(self):
        int_code = IntCodeComputer.parse_input("1,0,0,0,99")
        self.assertEqual([1, 0, 0, 0, 99], int_code)

    def test_icc_add(self):
        int_code = [
            ICC.ADD + ICC.MODE1_POS + ICC.MODE2_POS + ICC.MODE3_POS, 0, 0, 0,  # 0
            ICC.HALT,  # 4
        ]
        computer = IntCodeComputer(int_code)
        computer.run()
        memory = computer.dump()
        self.assertEqual([2, 0, 0, 0, 99], memory)

    def test_icc_mult1(self):
        int_code = [
            ICC.MULT + ICC.MODE1_POS + ICC.MODE2_POS + ICC.MODE3_POS, 3, 0, 3,  # 0
            ICC.HALT,  # 4
        ]
        computer = IntCodeComputer(int_code)
        computer.run()
        memory = computer.dump()
        self.assertEqual([2, 3, 0, 6, 99], memory)

    def test_icc_mult2(self):
        int_code = [
            ICC.MULT + ICC.MODE1_POS + ICC.MODE2_POS + ICC.MODE3_POS, 4, 4, 5,  # 0
            ICC.HALT,  # 4
            0,  # 5
        ]
        computer = IntCodeComputer(int_code)
        computer.run()
        memory = computer.dump()
        self.assertEqual([2, 4, 4, 5, 99, 9801], memory)

    def test_icc_add_imm1(self):
        int_code = [
            ICC.ADD + ICC.MODE1_IMM + ICC.MODE2_IMM + ICC.MODE3_POS, 0, 0, 0,  # 0
            ICC.HALT,  # 4
        ]
        computer = IntCodeComputer(int_code)
        computer.run()
        memory = computer.dump()
        self.assertEqual([0, 0, 0, 0, 99], memory)

    def test_icc_modify_code1(self):
        int_code = [  # 1, 1, 1, 4, ICC.HALT, 5, 6, 0, ICC.HALT]
            ICC.ADD + ICC.MODE1_POS + ICC.MODE2_POS + ICC.MODE3_POS, 1, 1, 4,  # 0, write 1+1 to 4
            ICC.HALT, 5, 6, 0,  # ICC.HALT is overwritten by test first instruction.
            ICC.HALT,
        ]

        computer = IntCodeComputer(int_code)
        computer.run()
        memory = computer.dump()
        self.assertEqual([30, 1, 1, 4, 2, 5, 6, 0, 99], memory)

    def test_icc_input1(self):
        int_code = [
            ICC.INPUT + ICC.MODE1_POS, 3,  # Write input to 3.
            ICC.HALT,
            0,
        ]
        input_stream = [13]

        computer = IntCodeComputer(int_code, input_stream)
        computer.run()
        memory = computer.dump()
        self.assertEqual([3, 3, 99, 13], memory)

    def test_icc_input2(self):
        int_code = [
            ICC.INPUT + ICC.MODE1_POS, 5,  # Write input to 5.
            ICC.INPUT + ICC.MODE1_POS, 6,  # Write input to 6.
            ICC.HALT,
            0,
            0,
        ]
        input_stream = [13, -3]

        computer = IntCodeComputer(int_code, input_stream)
        computer.run()
        memory = computer.dump()
        self.assertEqual([3, 5, 3, 6, 99, 13, -3], memory)

    def test_icc_output(self):
        int_code = [
            ICC.OUTPUT + ICC.MODE1_IMM, 64,  # Output 64.
            ICC.OUTPUT + ICC.MODE1_IMM, 14,  # Output 14.
            ICC.HALT,
        ]

        input_stream = []
        output_stream = []

        computer = IntCodeComputer(int_code, input_stream, output_stream)
        computer.run()
        self.assertEqual([64, 14], output_stream)

    def test_icc_until_output(self):
        int_code = [
            ICC.OUTPUT + ICC.MODE1_IMM, 64,  # Output 64.
            ICC.OUTPUT + ICC.MODE1_IMM, 14,  # Output 14.
            ICC.HALT,
        ]

        input_stream = []
        output_stream = []

        computer = IntCodeComputer(int_code, input_stream, output_stream)

        computer.run(until=ICC.OUTPUT)
        self.assertEqual([64], output_stream)
        output_stream.pop()

        computer.run(until=ICC.OUTPUT)
        self.assertEqual([14], output_stream)

    def test_icc_jmp_if_true1(self):
        int_code = [
            ICC.JMP_IF_TRUE + ICC.MODE1_IMM + ICC.MODE2_IMM, 0, 7,  # 0 don't jump
            ICC.MULT + ICC.MODE1_IMM + ICC.MODE2_IMM + ICC.MODE_POS, 1, 12, 8,  # 3 Store 12 to 8
            ICC.HALT,  # 7
            0,  # 8
        ]

        expected = int_code[:]
        expected[8] = 12

        computer = IntCodeComputer(int_code[:])
        computer.run()
        memory = computer.dump()
        self.assertEqual(expected, memory)

    def test_icc_jmp_if_true2(self):
        int_code = [
            ICC.JMP_IF_TRUE + ICC.MODE1_IMM + ICC.MODE2_IMM, 1, 7,  # 0 do jump
            ICC.MULT + ICC.MODE1_IMM + ICC.MODE2_IMM + ICC.MODE_POS, 1, 12, 8,  # 3 Store 12 to 8
            ICC.HALT,  # 7
            0,  # 8
        ]

        expected = int_code[:]

        computer = IntCodeComputer(int_code[:])
        computer.run()
        memory = computer.dump()
        self.assertEqual(expected, memory)

    def test_icc_jmp_if_false1(self):
        int_code = [
            ICC.JMP_IF_FALSE + ICC.MODE1_IMM + ICC.MODE2_IMM, 1, 7,  # 0 don't jump
            ICC.MULT + ICC.MODE1_IMM + ICC.MODE2_IMM + ICC.MODE_POS, 1, 12, 8,  # 3 Store 12 to 8
            ICC.HALT,  # 7
            0,  # 8
        ]

        expected = int_code[:]
        expected[8] = 12

        computer = IntCodeComputer(int_code[:])
        computer.run()
        memory = computer.dump()
        self.assertEqual(expected, memory)

    def test_icc_jmp_if_false2(self):
        int_code = [
            ICC.JMP_IF_FALSE + ICC.MODE1_IMM + ICC.MODE2_IMM, 0, 7,  # 0 do jump
            ICC.MULT + ICC.MODE1_IMM + ICC.MODE2_IMM + ICC.MODE_POS, 1, 12, 8,  # 3 Store 12 to 8
            ICC.HALT,  # 7
            0,  # 8
        ]

        expected = int_code[:]

        computer = IntCodeComputer(int_code[:])
        computer.run()
        memory = computer.dump()
        self.assertEqual(expected, memory)

    def test_icc_less_than1(self):
        int_code = [
            ICC.LESS_THAN + ICC.MODE1_IMM + ICC.MODE2_IMM + ICC.MODE3_POS, 0, 1, 5,  # 0
            ICC.HALT,  # 4
            -1,
        ]
        expected = int_code[:]
        expected[5] = 1
        computer = IntCodeComputer(int_code)
        computer.run()
        memory = computer.dump()
        self.assertEqual(expected, memory)

    def test_icc_less_than2(self):
        int_code = [
            ICC.LESS_THAN + ICC.MODE1_IMM + ICC.MODE2_IMM + ICC.MODE3_POS, 1, 1, 5,  # 0
            ICC.HALT,  # 4
            -1,
        ]
        expected = int_code[:]
        expected[5] = 0
        computer = IntCodeComputer(int_code)
        computer.run()
        memory = computer.dump()
        self.assertEqual(expected, memory)

    def test_icc_equals1(self):
        int_code = [
            ICC.EQUALS + ICC.MODE1_IMM + ICC.MODE2_IMM + ICC.MODE3_POS, 0, 1, 5,  # 0
            ICC.HALT,  # 4
            -1,
        ]
        expected = int_code[:]
        expected[5] = 0
        computer = IntCodeComputer(int_code)
        computer.run()
        memory = computer.dump()
        self.assertEqual(expected, memory)

    def test_icc_less_equals2(self):
        int_code = [
            ICC.EQUALS + ICC.MODE1_IMM + ICC.MODE2_IMM + ICC.MODE3_POS, 1, 1, 5,  # 0
            ICC.HALT,  # 4
            -1,
        ]
        expected = int_code[:]
        expected[5] = 1
        computer = IntCodeComputer(int_code)
        computer.run()
        memory = computer.dump()
        self.assertEqual(expected, memory)

    def test_icc_add_rb1(self):
        int_code = [
            ICC.ADD + ICC.MODE1_RBASE + ICC.MODE2_POS + ICC.MODE3_POS, 0, 0, 0,  # 0
            ICC.HALT,  # 4
        ]
        computer = IntCodeComputer(int_code)
        computer.run()
        memory = computer.dump()
        self.assertEqual([402, 0, 0, 0, 99], memory)

    def test_icc_add_rb2(self):
        int_code = [
            ICC.ADJUST_BASE + ICC.MODE1_IMM, 3,  # 0
            ICC.ADJUST_BASE + ICC.MODE1_IMM, 6,  # 2
            ICC.ADD + ICC.MODE1_RBASE + ICC.MODE2_IMM + ICC.MODE3_RBASE, 0, 3, 1,  # 4
            ICC.HALT,  # 8
            5, 0,  # 9
        ]

        expected = int_code[:]
        expected[10] = 8

        computer = IntCodeComputer(int_code)
        computer.run()
        memory = computer.dump()
        self.assertEqual(expected, memory)

    def test_icc_day2_part1_example1(self):
        int_code = [1, 0, 0, 0, 99]
        computer = IntCodeComputer(int_code)
        computer.run()
        memory = computer.dump()
        self.assertEqual([2, 0, 0, 0, 99], memory)

    def test_icc_day2_part1_example2(self):
        int_code = [2, 3, 0, 3, 99]
        computer = IntCodeComputer(int_code)
        computer.run()
        memory = computer.dump()
        self.assertEqual([2, 3, 0, 6, 99], memory)

    def test_icc_day2_part1_example3(self):
        int_code = [2, 4, 4, 5, 99, 0]
        computer = IntCodeComputer(int_code)
        computer.run()
        memory = computer.dump()
        self.assertEqual([2, 4, 4, 5, 99, 9801], memory)

    def test_icc_day2_part1_example4(self):
        int_code = [1, 1, 1, 4, 99, 5, 6, 0, 99]
        computer = IntCodeComputer(int_code)
        computer.run()
        memory = computer.dump()
        self.assertEqual([30, 1, 1, 4, 2, 5, 6, 0, 99], memory)

    def test_icc_day5_part1_example1(self):
        int_code = [
            1002, 4, 3, 4, 33
        ]
        expected = int_code[:]
        expected[4] = 99
        computer = IntCodeComputer(int_code)
        computer.run()
        memory = computer.dump()
        self.assertEqual(expected, memory)

    def test_icc_day5_part1_example2(self):
        int_code = [
            1101, 100, -1, 4, 0
        ]
        expected = int_code[:]
        expected[4] = 99
        computer = IntCodeComputer(int_code)
        computer.run()
        memory = computer.dump()
        self.assertEqual(expected, memory)

    def test_icc_day5_part2_example1a(self):
        int_code = [
            3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8
        ]
        input_stream = [8]
        output_stream = []
        computer = IntCodeComputer(int_code, input_stream, output_stream)
        computer.run()
        self.assertEqual([1], output_stream)

    def test_icc_day5_part2_example1b(self):
        int_code = [
            3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8
        ]
        input_stream = [7]
        output_stream = []
        computer = IntCodeComputer(int_code, input_stream, output_stream)
        computer.run()
        self.assertEqual([0], output_stream)

    def test_icc_day5_part2_example2a(self):
        int_code = [
            3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8
        ]
        input_stream = [8]
        output_stream = []
        computer = IntCodeComputer(int_code, input_stream, output_stream)
        computer.run()
        self.assertEqual([0], output_stream)

    def test_icc_day5_part2_example2b(self):
        int_code = [
            3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8
        ]
        input_stream = [7]
        output_stream = []
        computer = IntCodeComputer(int_code, input_stream, output_stream)
        computer.run()
        self.assertEqual([1], output_stream)

    def test_icc_day5_part2_example3a(self):
        int_code = [
            3, 3, 1108, -1, 8, 3, 4, 3, 99
        ]
        input_stream = [8]
        output_stream = []
        computer = IntCodeComputer(int_code, input_stream, output_stream)
        computer.run()
        self.assertEqual([1], output_stream)

    def test_icc_day5_part2_example3b(self):
        int_code = [
            3, 3, 1108, -1, 8, 3, 4, 3, 99
        ]
        input_stream = [7]
        output_stream = []
        computer = IntCodeComputer(int_code, input_stream, output_stream)
        computer.run()
        self.assertEqual([0], output_stream)

    def test_icc_day5_part2_example4a(self):
        int_code = [
            3, 3, 1107, -1, 8, 3, 4, 3, 99
        ]
        input_stream = [8]
        output_stream = []
        computer = IntCodeComputer(int_code, input_stream, output_stream)
        computer.run()
        self.assertEqual([0], output_stream)

    def test_icc_day5_part2_example4b(self):
        int_code = [
            3, 3, 1107, -1, 8, 3, 4, 3, 99
        ]
        input_stream = [7]
        output_stream = []
        computer = IntCodeComputer(int_code, input_stream, output_stream)
        computer.run()
        self.assertEqual([1], output_stream)

    def test_icc_day5_part2_example5a(self):
        int_code = [
            3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9
        ]
        input_stream = [0]
        output_stream = []
        computer = IntCodeComputer(int_code, input_stream, output_stream)
        computer.run()
        self.assertEqual([0], output_stream)

    def test_icc_day5_part2_example5b(self):
        int_code = [
            3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9
        ]
        input_stream = [6]
        output_stream = []
        computer = IntCodeComputer(int_code, input_stream, output_stream)
        computer.run()
        self.assertEqual([1], output_stream)

    def test_icc_day5_part2_example6a(self):
        int_code = [
            3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1
        ]
        input_stream = [0]
        output_stream = []
        computer = IntCodeComputer(int_code, input_stream, output_stream)
        computer.run()
        self.assertEqual([0], output_stream)

    def test_icc_day5_part2_example6b(self):
        int_code = [
            3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1
        ]
        input_stream = [6]
        output_stream = []
        computer = IntCodeComputer(int_code, input_stream, output_stream)
        computer.run()
        self.assertEqual([1], output_stream)

    def test_icc_day5_part2_example7a(self):
        int_code = [
            3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
            1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
            999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99
        ]
        input_stream = [6]
        output_stream = []
        computer = IntCodeComputer(int_code, input_stream, output_stream)
        computer.run()
        self.assertEqual([999], output_stream)

    def test_icc_day5_part2_example7b(self):
        int_code = [
            3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
            1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
            999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99
        ]
        input_stream = [8]
        output_stream = []
        computer = IntCodeComputer(int_code, input_stream, output_stream)
        computer.run()
        self.assertEqual([1000], output_stream)

    def test_icc_day5_part2_example7c(self):
        int_code = [
            3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
            1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
            999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99
        ]
        input_stream = [9]
        output_stream = []
        computer = IntCodeComputer(int_code, input_stream, output_stream)
        computer.run()
        self.assertEqual([1001], output_stream)

    def test_icc_day9_part1_example1(self):
        int_code = [
            109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99
        ]
        expected = int_code[:]
        input_stream = []
        output_stream = []
        computer = IntCodeComputer(int_code, input_stream, output_stream)
        computer.run()
        self.assertEqual(expected, output_stream)

    def test_icc_day9_part1_example2(self):
        int_code = [
            1102, 34915192, 34915192, 7, 4, 7, 99, 0
        ]

        # int_code[1] * int_code[1]
        expected_output_stream = [1219070632396864]
        input_stream = []
        output_stream = []
        computer = IntCodeComputer(int_code, input_stream, output_stream)
        computer.run()
        self.assertEqual(expected_output_stream, output_stream)

    def test_icc_day9_part1_example3(self):
        int_code = [
            104, 1125899906842624, 99
        ]

        # int_code[1]
        expected_output_stream = [1125899906842624]
        input_stream = []
        output_stream = []
        computer = IntCodeComputer(int_code, input_stream, output_stream)
        computer.run()
        self.assertEqual(expected_output_stream, output_stream)


if __name__ == '__main__':
    unittest.main()
