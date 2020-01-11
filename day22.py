#!/usr/bin/env python3

import re
from collections import deque

import aoc

class DeckOfSpaceCards:
    _cut_n_re = re.compile(r"cut (-?\d+)")
    _deal_with_increment_n_re = re.compile(r"deal with increment (\d+)")

    def __init__(self, size):
        self._deck = deque([x for x in range(size)])

    def shuffle(self, techniques):
        for technique in techniques:
            if technique == "deal into new stack":
                self.deal_into_new_stack()
                continue

            match = self._cut_n_re.match(technique)
            if match:
                cut_number = int(match.group(1))
                self.cut_n(cut_number)
                continue

            match = self._deal_with_increment_n_re.match(technique)
            if match:
                increment = int(match.group(1))
                self.deal_with_increment(increment)
                continue

            assert False

    def get_card(self,position):
        return self._deck[position]

    def get_all_cards(self):
        return list(self._deck)

    def find_card(self, card):
        return self._deck.index(card)

    def deal_into_new_stack(self):
        self._deck.reverse()

    def cut_n(self, number):
        self._deck.rotate(-number)

    def deal_with_increment(self, increment):
        deck_size = len(self._deck)
        old_deck = list(self._deck)
        current = 0
        for card in old_deck:
            self._deck[current] = card
            current += increment
            current %= deck_size

def part1(input_list):
    deck = DeckOfSpaceCards(10007)
    deck.shuffle(input_list)
    return deck.find_card(2019)


def part2(input_list):
    deck = DeckOfSpaceCards(119315717514047)
    return None
    deck.shuffle(input_list)
    return deck.get_card(2020)


if __name__ == "__main__":
    aoc.main(part1, part2)
