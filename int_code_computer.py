#!/usr/bin/env python3

# See Day 2 and Day 5 for documentation.

class IntCodeComputer:
    ADD = 1
    MULT = 2
    INPUT = 3
    OUTPUT = 4
    JMP_IF_TRUE = 5
    JMP_IF_FALSE = 6
    LESS_THAN = 7
    EQUALS = 8
    HALT = 99

    IS_DEST = 99
    MODE_POS = 0
    MODE_IMM = 1

    MODE1_POS = 0
    MODE2_POS = 0
    MODE3_POS = 0

    MODE1_IMM = 100
    MODE2_IMM = 1000
    MODE3_IMM = 10000

    @staticmethod
    def parse_input(line):
        int_code = list(map(int, line.split(',')))
        return int_code

    def _i_add(self, parameters):
        self._memory[parameters[2]] = parameters[0] + parameters[1]
        self._ip += 4

    def _i_mult(self, parameters):
        self._memory[parameters[2]] = parameters[0] * parameters[1]
        self._ip += 4

    def _i_halt(self, _):
        self._halted = True
        self._ip += 0

    def _i_input(self, parameters):
        self._memory[parameters[0]] = self._input_stream.pop(0)
        self._ip += 2

    def _i_output(self, parameters):
        self._output_stream.append(parameters[0])
        self._ip += 2

    def _i_jmp_if_true(self, parameters):
        if parameters[0] != 0:
            self._ip = parameters[1]
        else:
            self._ip += 3

    def _i_jmp_if_false(self, parameters):
        if parameters[0] == 0:
            self._ip = parameters[1]
        else:
            self._ip += 3

    def _i_less_than(self, parameters):
        if parameters[0] < parameters[1]:
            self._memory[parameters[2]] = 1
        else:
            self._memory[parameters[2]] = 0
        self._ip += 4

    def _i_equals(self, parameters):
        if parameters[0] == parameters[1]:
            self._memory[parameters[2]] = 1
        else:
            self._memory[parameters[2]] = 0
        self._ip += 4

    # opcode : (num_parameters, function)
    _config = {
        ADD: ([{MODE_POS, MODE_IMM}, {MODE_POS, MODE_IMM}, {IS_DEST, MODE_POS}], _i_add),
        MULT: ([{MODE_POS, MODE_IMM}, {MODE_POS, MODE_IMM}, {IS_DEST, MODE_POS}], _i_mult),
        INPUT: ([{IS_DEST, MODE_POS}], _i_input),
        OUTPUT: ([{MODE_POS, MODE_IMM}], _i_output),
        JMP_IF_TRUE: ([{MODE_POS, MODE_IMM}, {MODE_POS, MODE_IMM}], _i_jmp_if_true),
        JMP_IF_FALSE: ([{MODE_POS, MODE_IMM}, {MODE_POS, MODE_IMM}], _i_jmp_if_false),
        LESS_THAN: ([{MODE_POS, MODE_IMM}, {MODE_POS, MODE_IMM}, {IS_DEST, MODE_POS}],
                    _i_less_than),
        EQUALS: ([{MODE_POS, MODE_IMM}, {MODE_POS, MODE_IMM}, {IS_DEST, MODE_POS}], _i_equals),
        HALT: ([], _i_halt),
    }

    def __init__(self, int_code, input_stream=None, output_stream=None):
        self._memory = int_code[:]
        self._ip = 0
        self._halted = False

        if input_stream is not None:
            self._input_stream = input_stream
        else:
            self._input_stream = []

        if output_stream is not None:
            self._output_stream = output_stream
        else:
            self._output_stream = []

    def dump(self):
        return self._memory[:]

    def get_memory(self, address):
        return self._memory[address]

    def run(self):
        self._halted = False
        while not self._halted:
            int_code = self._memory[self._ip]

            opcode = int_code % 100
            int_code //= 100
            assert opcode in self._config

            config = self._config[opcode]

            parameters = []
            for pnum in range(len(config[0])):
                mode = int_code % 10
                assert mode in config[0][pnum]
                int_code //= 10

                immediate_value = self._memory[self._ip + 1 + pnum]

                if mode == IntCodeComputer.MODE_POS and IntCodeComputer.IS_DEST in config[0][pnum]:
                    parameters.append(immediate_value)

                elif mode == IntCodeComputer.MODE_POS:
                    parameters.append(self._memory[immediate_value])

                elif mode == IntCodeComputer.MODE_IMM:
                    parameters.append(immediate_value)

                else:
                    assert False

            # Call the function that implements the opcode.
            config[1](self, parameters)


if __name__ == "__main__":
    pass
