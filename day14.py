#!/usr/bin/env python3

from collections import defaultdict
from collections import namedtuple

import aoc

SHIP_CARGO_CAPACITY = 1000000000000


class FuelFactory:
    Ingredient = namedtuple('Ingredient', ['ingredient', 'amount'])
    Recipe = namedtuple('Recipe', ['makes', 'ingredients'])

    def __init__(self, input_list):
        # Recipes indexed by ingredient name.
        self._reaction_table = {}  # Recipes indexed by ingredient name.

        # Keep track of ingredients we have made and not yet used.  Amount available indexed by
        # ingredient name.
        self._available = defaultdict(int)

        # Total ORE used.
        self._ore_used = 0

        self._parse_input_to_reaction_table(input_list)

    def _parse_input_to_reaction_table(self, input_list):
        for line in input_list:
            raw_materials, produced = line.split("=>")

            amount_produced, chemical_produced = produced.split()
            amount_produced = int(amount_produced)

            assert chemical_produced not in self._reaction_table

            ingredients = []

            for material in raw_materials.split(","):
                material.strip()
                quantity, chemical = material.split()
                quantity = int(quantity)

                ingredients += [self.Ingredient(ingredient=chemical, amount=quantity)]

            recipe = self.Recipe(makes=amount_produced, ingredients=ingredients)
            self._reaction_table[chemical_produced] = recipe

    def get_ore_used(self):
        return self._ore_used

    def make_fuel(self, amount=1):
        return self._make_ingredient("FUEL", amount)

    def _make_ingredient(self, ingredient, amount):
        if ingredient == "ORE":
            self._ore_used += amount
            return

        while self._available[ingredient] < amount:

            # We may have some available so calculate how much more we need.
            amount_to_make = amount - self._available[ingredient]

            recipe = self._reaction_table[ingredient]

            batches_to_make = amount_to_make // recipe.makes
            if amount_to_make % recipe.makes != 0:
                batches_to_make += 1

            for ingredient_info in recipe.ingredients:
                # Recursively call to make each ingredient needed.
                amount_needed = ingredient_info.amount * batches_to_make
                self._make_ingredient(ingredient_info.ingredient, amount_needed)

            self._available[ingredient] += recipe.makes * batches_to_make

        self._available[ingredient] -= amount


def part1(input_list):
    fuel_factory = FuelFactory(input_list)
    fuel_factory.make_fuel()
    return fuel_factory.get_ore_used()


def part2(input_list):
    fuel_factory = FuelFactory(input_list)

    fuel_factory.make_fuel(1)
    units_made = 1
    ore_per_unit = fuel_factory.get_ore_used()

    while fuel_factory.get_ore_used() < SHIP_CARGO_CAPACITY:
        units_to_make = (SHIP_CARGO_CAPACITY - fuel_factory.get_ore_used()) // ore_per_unit

        fuel_factory.make_fuel(units_to_make)
        if units_to_make == 0:
            break

        units_made += units_to_make

    return units_made


if __name__ == "__main__":
    aoc.main(part1, part2)
