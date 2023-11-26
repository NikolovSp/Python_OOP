from project.animals.animal import Mammal
from project.food import Vegetable, Fruit, Meat


class Mouse(Mammal):
    def make_sound(self):
        return "Squeak"

    def food_multiplier(self):
        return 0.10

    def does_it_eat(self):
        return [Vegetable, Fruit]


class Dog(Mammal):
    def make_sound(self):
        return "Woof!"

    def food_multiplier(self):
        return 0.40

    def does_it_eat(self):
        return [Meat]


class Cat(Mammal):
    def make_sound(self):
        return "Meow"

    def food_multiplier(self):
        return 0.30

    def does_it_eat(self):
        return [Meat, Vegetable]


class Tiger(Mammal):
    def make_sound(self):
        return "ROAR!!!"

    def food_multiplier(self):
        return 1

    def does_it_eat(self):
        return [Meat]
