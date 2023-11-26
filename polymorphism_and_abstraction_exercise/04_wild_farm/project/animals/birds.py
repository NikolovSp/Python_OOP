from project.animals.animal import Bird
from project.food import Meat, Vegetable, Fruit, Seed


class Owl(Bird):
    def make_sound(self):
        return "Hoot Hoot"

    def food_multiplier(self):
        return 0.25

    def does_it_eat(self):
        return [Meat]


class Hen(Bird):
    def make_sound(self):
        return "Cluck"

    def food_multiplier(self):
        return 0.35

    def does_it_eat(self):
        return [Meat, Vegetable, Fruit, Seed]
