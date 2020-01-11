import unittest

import aoc
import day22


class TestDay21(unittest.TestCase):

    def test_deal_into_new_stack(self):
        techniques = [
            "deal into new stack"
        ]
        deck = day22.DeckOfSpaceCards(10)
        deck.shuffle(techniques)
        cards = deck.get_all_cards()
        self.assertEqual(list(map(int, "9 8 7 6 5 4 3 2 1 0".split())), cards)

    def test_cut_n(self):
        techniques = [
            "cut 3"
        ]
        deck = day22.DeckOfSpaceCards(10)
        deck.shuffle(techniques)
        cards = deck.get_all_cards()
        self.assertEqual(list(map(int, "3 4 5 6 7 8 9 0 1 2".split())), cards)

    def test_cut_n_negative(self):
        techniques = [
            "cut -4"
        ]
        deck = day22.DeckOfSpaceCards(10)
        deck.shuffle(techniques)
        cards = deck.get_all_cards()
        self.assertEqual(list(map(int, "6 7 8 9 0 1 2 3 4 5".split())), cards)

    def test_deal_with_increment(self):
        techniques = [
            "deal with increment 3"
        ]
        deck = day22.DeckOfSpaceCards(10)
        deck.shuffle(techniques)
        cards = deck.get_all_cards()
        self.assertEqual(list(map(int, "0 7 4 1 8 5 2 9 6 3".split())), cards)

    def test_part1_example1(self):
        techniques = [
            "deal with increment 7",
            "deal into new stack",
            "deal into new stack",
        ]
        expected = "0 3 6 9 2 5 8 1 4 7"
        deck = day22.DeckOfSpaceCards(10)
        deck.shuffle(techniques)
        cards = deck.get_all_cards()
        self.assertEqual(list(map(int, expected.split())), cards)

    def test_part2_example2(self):
        techniques = [
            "cut 6",
            "deal with increment 7",
            "deal into new stack",
        ]
        expected = "3 0 7 4 1 8 5 2 9 6"
        deck = day22.DeckOfSpaceCards(10)
        deck.shuffle(techniques)
        cards = deck.get_all_cards()
        self.assertEqual(list(map(int, expected.split())), cards)

    def test_part2_example3(self):
        techniques = [
            "deal with increment 7",
            "deal with increment 9",
            "cut -2",
        ]
        expected = "6 3 0 7 4 1 8 5 2 9"
        deck = day22.DeckOfSpaceCards(10)
        deck.shuffle(techniques)
        cards = deck.get_all_cards()
        self.assertEqual(list(map(int, expected.split())), cards)

    def test_part2_example4(self):
        techniques = [
            "deal into new stack",
            "cut -2",
            "deal with increment 7",
            "cut 8",
            "cut -4",
            "deal with increment 7",
            "cut 3",
            "deal with increment 9",
            "deal with increment 3",
            "cut -1",
        ]
        expected = "9 2 5 8 1 4 7 0 3 6"
        deck = day22.DeckOfSpaceCards(10)
        deck.shuffle(techniques)
        cards = deck.get_all_cards()
        self.assertEqual(list(map(int, expected.split())), cards)

    def test_part1_input(self):
        result = day22.part1(aoc.read_input('day22.input'))
        self.assertEqual(6326, result)

    @unittest.skip
    def test_part2_input(self):
        result = day22.part2(aoc.read_input('day22.input'))
        self.assertEqual(40522432670594, result)


if __name__ == '__main__':
    unittest.main()
