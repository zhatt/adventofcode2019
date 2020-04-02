#!/usr/bin/env python3
import copy
import re
from collections import deque

import aoc
import int_code_computer

VERBOSE = False


class Droid:
    _next_serial_number = 0
    _keypad_parser = re.compile(r"typing (\d+) on the keypad")

    BAD_ITEMS = {
        "infinite loop",
        "molten lava",
        "photons",
    }

    def __init__(self, int_code):
        self._serial_number = self._next_serial_number
        self._next_serial_number += 1
        self._input_stream = []
        self._output_stream = []
        self._computer = int_code_computer.IntCodeComputer(int_code, self._input_stream,
                                                           self._output_stream)
        self._room = ''
        self._rooms_visited = []
        self._doors = []
        self._items_here = []
        self._items_carried = set()

        self._output = ""
        self._keypad_code = None

        self._run()

    def room(self):
        return self._room

    def doors(self):
        return self._doors.copy()

    def items_here(self):
        return self._items_here.copy()

    def items_carried(self):
        return self._items_carried.copy()

    def keypad_code(self):
        return self._keypad_code

    def _printer(self, output):
        if VERBOSE:
            for line in str(output).split("\n"):
                line = "SERIAL:%03d %s" % (self._serial_number, line)
                self._output += line + "\n"

    def print_state(self):
        if VERBOSE:
            self._printer("ROOM %s" % self._room)
            self._printer("VISITED %s" % self._rooms_visited)
            self._printer("DOORS %s" % self._doors)
            self._printer("ITEMS %s" % self._items_here)
            self._printer("ITEMS_CARRIED %s" % self._items_carried)
            print("==========BEGIN")
            print(self._output, end="")
            print("==========END")

    def command(self, command):
        self._input_stream += list(map(ord, command))
        self._input_stream.append(ord("\n"))
        self._printer("COMMAND: %s" % command)
        self._run()

    def take(self, item):
        if VERBOSE:
            print("TAKE", item)
        command = "take " + item
        self.command(command)
        self._items_carried.add(item)
        self._run()

    def drop(self, item):
        if VERBOSE:
            print("DROP", item)
        command = "drop " + item
        self.command(command)
        self._items_carried.remove(item)
        self._run()

    def _run(self):
        self._computer.run(until=self._computer.INPUT)
        output = self._peek_output()
        self._printer(output)
        self._parse_output()

    def copy(self):
        new_droid = copy.deepcopy(self)
        new_droid._serial_number = self._next_serial_number
        self._next_serial_number += 1
        return new_droid

    def _peek_output(self):
        output = "".join(map(chr, self._output_stream))
        return output

    def _get_output(self):
        output = "".join(map(chr, self._output_stream))
        self._output_stream.clear()
        return output

    def _parse_output(self):
        section = ''
        output = self._get_output()
        for line in output.split("\n"):
            if line == '':
                section = ''

            elif line.startswith("=="):
                self._room = line
                self._rooms_visited.append((line, self._items_carried.copy()))
                section = ''

            elif line == "Doors here lead:":
                section = 'doors'
                self._doors.clear()

            elif section == 'doors':
                self._doors += [line[2:]]

            elif line == "Items here:":
                section = 'items'
                self._items_here.clear()

            elif section == 'items':
                self._items_here += [line[2:]]

            else:
                match = self._keypad_parser.search(line)
                if match:
                    self._keypad_code = match.group(1)


rooms_visited = set()


def already_visited(droid):
    visited_state = (droid.room(), frozenset(droid.items_carried()))
    if visited_state in rooms_visited:
        return True

    rooms_visited.add(visited_state)
    return False


def part1(input_list):
    int_code = int_code_computer.IntCodeComputer.parse_input(input_list[0])

    droid = Droid(int_code)

    # There are no items in the first room.
    work_queue = deque()
    work_queue.append(droid.copy())

    while work_queue:
        if VERBOSE:
            print("WQLEN", len(work_queue))

        if droid.keypad_code() is not None:
            return droid.keypad_code()

        droid = work_queue.popleft()
        droid.print_state()

        items_here = droid.items_here()
        items_carried = droid.items_carried()

        for item_to_drop in items_carried:
            new_droid = droid.copy()
            new_droid.drop(item_to_drop)
            if not already_visited(new_droid):
                work_queue.append(new_droid)

        for item_to_take in items_here:
            if item_to_take in Droid.BAD_ITEMS:
                # Don't pick it up.
                continue

            new_droid = droid.copy()
            new_droid.take(item_to_take)
            if not already_visited(new_droid):
                work_queue.append(new_droid)

        for door in droid.doors():
            new_droid = droid.copy()
            new_droid.command(door)
            if not already_visited(new_droid):
                work_queue.append(new_droid)

    return None


def part2(input_list):
    pass


if __name__ == "__main__":
    aoc.main(part1, part2)
