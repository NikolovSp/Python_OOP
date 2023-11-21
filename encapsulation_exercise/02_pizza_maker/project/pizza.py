from typing import Dict

from project.dough import Dough
from project.topping import Topping


class Pizza:
    def __init__(self, name: str, dough: Dough, max_number_of_toppings: int):
        self.name = name
        self.dough: Dough = dough
        self.max_number_of_toppings = max_number_of_toppings
        self.toppings: Dict[Topping.topping_type, Topping.weight] = {}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) == 0:
            raise ValueError("The name cannot be an empty string")
        self.__name = value

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value):
        if value is None:
            raise ValueError("You should add dough to the pizza")
        self.__dough = value

    @property
    def max_number_of_toppings(self):
        return self.__max_number_of_toppings

    @max_number_of_toppings.setter
    def max_number_of_toppings(self, value):
        if value <= 0:
            raise ValueError("The maximum number of toppings cannot be less or equal to zero")
        self.__max_number_of_toppings = value

    def add_topping(self, topping: Topping):
        if len(self.toppings) >= self.max_number_of_toppings:
            raise ValueError("Not enough space for another topping")
        topping_type = topping.topping_type
        weight = topping.weight
        if topping_type not in self.toppings:
            self.toppings[topping_type] = 0
        self.toppings[topping_type] += weight

    def calculate_total_weight(self):
        # total_weight = sum([w for w in self.toppings.values()])
        # total_weight += self.dough.weight
        # return total_weight
        return self.dough.weight + sum(self.toppings.values())
