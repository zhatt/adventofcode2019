#!/usr/bin/env python3
import collections

import aoc
import int_code_computer

Packet = collections.namedtuple('Packet', ['address', 'x_value', 'y_value'])


class NetworkComputer:
    # InputStream is a list that will pop() a -1 if it is empty.
    # We also keep track of the number of times in a row that we pop -1 in null_count.
    class InputStream(collections.UserList):  # pylint: disable=too-many-ancestors
        def __init__(self, stream):
            self.null_count = 0  # Number of nulls input in a row.13G
            super().__init__(stream)

        def pop(self, i=-1):
            if len(self.data) == 0:
                # The stream is empty so inject a -1.
                self.data.append(-1)
                self.null_count += 1
            else:
                self.null_count = 0

            return super().pop(i)

    def __init__(self, int_code, address):
        self.int_code = int_code.copy()
        # The intcode needs the address as the first input value.
        self.input_stream = self.InputStream([address])
        self.output_stream = []
        self.computer = int_code_computer.IntCodeComputer(self.int_code,
                                                          self.input_stream,
                                                          self.output_stream)

    def step(self):
        self.computer.step()

    def output_packet(self):
        if len(self.output_stream) >= 3:
            address = self.output_stream.pop(0)
            x_value = self.output_stream.pop(0)
            y_value = self.output_stream.pop(0)
            return Packet(address, x_value, y_value)

        return None

    def input_packet(self, packet):
        self.input_stream.append(packet.x_value)
        self.input_stream.append(packet.y_value)

    def is_idle(self):
        return len(self.input_stream) == 0 and self.input_stream.null_count > 5


class Nat:
    def __init__(self):
        self.packet = None

    def input_packet(self, packet):
        self.packet = packet

    def get(self):
        return self.packet


def simulate(input_list, part):
    int_code = int_code_computer.IntCodeComputer.parse_input(input_list[0])

    # Create 50 computers and with addresses 0-49
    computers = []
    for address in range(50):
        computer = NetworkComputer(int_code, address)
        computers.append(computer)

    nat = Nat()
    last_y = None

    while True:
        all_idle = True
        for computer in computers:
            computer.step()

            if not computer.is_idle():
                all_idle = False

            packet = computer.output_packet()
            if packet is not None:
                if packet.address == 255 and part == 1:
                    return packet.y_value

                # Packets addressed to 255 go to the NAT.
                if packet.address == 255:
                    nat.input_packet(packet)
                else:
                    computers[packet.address].input_packet(packet)

        if all_idle:
            # All computers are idle.  Get the last NAT value and send it to computer 0.
            nat_packet = nat.get()

            computers[0].input_packet(nat_packet)

            # If we sent the same value 2 times in a row then part 2 is done.
            if part == 2 and last_y == nat_packet.y_value:
                return last_y

            last_y = nat_packet.y_value


def part1(input_list):
    return simulate(input_list, part=1)


def part2(input_list):
    return simulate(input_list, part=2)


if __name__ == "__main__":
    aoc.main(part1, part2)
