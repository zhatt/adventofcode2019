#!/usr/bin/env python3

# See Day 2, 5 and 9 descriptions for documentation about opcodes.
from collections import UserList


class Memory(UserList):  # pylint: disable=too-many-ancestors
    def __setitem__(self, index, value):
        # Extend list to contain index.
        self.data.extend([0] * (index - len(self.data) + 1))

        self.data[index] = value

    def __getitem__(self, index):
        # We don't support slicing.
        assert not isinstance(index, slice)
        # Extend list to contain index.
        self.data.extend([0] * (index - len(self.data) + 1))

        return self.data[index]


class IntCodeComputer:
    ADD = 1
    MULT = 2
    INPUT = 3
    OUTPUT = 4
    JMP_IF_TRUE = 5
    JMP_IF_FALSE = 6
    LESS_THAN = 7
    EQUALS = 8
    ADJUST_BASE = 9
    STEP = 98
    HALT = 99

    IS_DEST = 99
    MODE_POS = 0
    MODE_IMM = 1
    MODE_RBASE = 2
    MODE_SOURCE = {MODE_POS, MODE_IMM, MODE_RBASE}
    MODE_DEST = {IS_DEST, MODE_POS, MODE_RBASE}

    MODE1_POS = 0  # MODE_POS * 100
    MODE2_POS = 0
    MODE3_POS = 0

    MODE1_IMM = 100  # MODE_IMM * 100
    MODE2_IMM = 1000
    MODE3_IMM = 10000

    MODE1_RBASE = 200  # MODE_RBASE * 100
    MODE2_RBASE = 2000
    MODE3_RBASE = 20000

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
        self._output_generated = True
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

    def _i_adjust_base(self, parameters):
        self._rb += parameters[0]
        self._ip += 2

    # opcode : ([num and type of parameters], function)
    _config = {
        ADD: ([MODE_SOURCE, MODE_SOURCE, MODE_DEST], _i_add),
        MULT: ([MODE_SOURCE, MODE_SOURCE, MODE_DEST], _i_mult),
        INPUT: ([MODE_DEST], _i_input),
        OUTPUT: ([MODE_SOURCE], _i_output),
        JMP_IF_TRUE: ([MODE_SOURCE, MODE_SOURCE], _i_jmp_if_true),
        JMP_IF_FALSE: ([MODE_SOURCE, MODE_SOURCE], _i_jmp_if_false),
        LESS_THAN: ([MODE_SOURCE, MODE_SOURCE, MODE_DEST], _i_less_than),
        EQUALS: ([MODE_SOURCE, MODE_SOURCE, MODE_DEST], _i_equals),
        ADJUST_BASE: ([MODE_SOURCE], _i_adjust_base),
        HALT: ([], _i_halt),
    }

    def __init__(self, int_code, input_stream=None, output_stream=None):
        self._memory = Memory(int_code[:])
        self._ip = 0
        self._rb = 0
        self._halted = False
        self._output_generated = False

        if input_stream is not None:
            self._input_stream = input_stream
        else:
            self._input_stream = []

        if output_stream is not None:
            self._output_stream = output_stream
        else:
            self._output_stream = []

    def dump(self):
        return self._memory.copy()

    def get_memory(self, address):
        return self._memory[address]

    def is_halted(self):
        return self._halted

    def step(self):
        self.run(until=self.STEP)

    def run(self, until=HALT):
        assert (until in {self.HALT, self.STEP, self.OUTPUT, self.INPUT})

        self._output_generated = False
        self._halted = False
        need_input = False
        while not self._halted and \
                not (until == self.OUTPUT and self._output_generated) and \
                not (until == self.INPUT and need_input):

            int_code = self._memory[self._ip]

            opcode = int_code % 100
            int_code //= 100
            assert opcode in self._config

            if opcode == IntCodeComputer.INPUT and not self._input_stream and until == self.INPUT:
                need_input = True
                break

            config = self._config[opcode]

            parameters = []
            for pnum in range(len(config[0])):
                mode = int_code % 10
                assert mode in config[0][pnum]
                int_code //= 10

                immediate_value = self._memory[self._ip + 1 + pnum]

                if mode == IntCodeComputer.MODE_POS and IntCodeComputer.IS_DEST in config[0][pnum]:
                    parameters.append(immediate_value)

                elif mode == IntCodeComputer.MODE_RBASE and IntCodeComputer.IS_DEST in \
                        config[0][pnum]:
                    parameters.append(self._rb + immediate_value)

                elif mode == IntCodeComputer.MODE_POS:
                    parameters.append(self._memory[immediate_value])

                elif mode == IntCodeComputer.MODE_IMM:
                    parameters.append(immediate_value)

                elif mode == IntCodeComputer.MODE_RBASE:
                    parameters.append(self._memory[self._rb + immediate_value])

                else:
                    assert False

            # Call the function that implements the opcode.
            config[1](self, parameters)

            if until == self.STEP:
                break


if __name__ == "__main__":
    pass
