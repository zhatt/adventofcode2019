#!/usr/bin/env python3

class IntCodeComputer:

    def __init__(self, int_code):
        self._memory = int_code[:]
        self._ip = 0

    def dump(self):
        return self._memory[:]

    def get_memory(self, address):
        return self._memory[address]

    def run(self):
        halted = False
        while not halted:
            opcode = self._memory[self._ip]

            if opcode == 1:
                src_index1 = self._memory[self._ip + 1]
                src_index2 = self._memory[self._ip + 2]
                dest_index = self._memory[self._ip + 3]
                self._memory[dest_index] = self._memory[src_index1] + self._memory[src_index2]
                self._ip += 4

            elif opcode == 2:
                src_index1 = self._memory[self._ip + 1]
                src_index2 = self._memory[self._ip + 2]
                dest_index = self._memory[self._ip + 3]
                self._memory[dest_index] = self._memory[src_index1] * self._memory[src_index2]
                self._ip += 4

            elif opcode == 99:
                self._ip += 1
                halted = True

            else:
                assert False


if __name__ == "__main__":
    pass
