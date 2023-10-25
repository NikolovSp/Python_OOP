from pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon_: Pokemon):
        if pokemon_ in self.pokemons:
            return "This pokemon is already caught"

        self.pokemons.append(pokemon_)

        return f"Caught {pokemon_.pokemon_details()}"

    def release_pokemon(self, pokemon_name: str):
        # try:
        #     pokemon = next(filter(lambda x: x.pokemon_name == pokemon_name, self.pokemons))
        #
        # except StopIteration:
        #     return "Pokemon is not caught"
        try:
            pokemon_ = [p for p in self.pokemons if p.name == pokemon_name][0]

        except IndexError:
            return "Pokemon is not caught"

        self.pokemons.remove(pokemon_)

        return f"You have released {pokemon_name}"

    def trainer_data(self):
        pokemons_data = '\n'.join([f"- {p.pokemon_details()}" for p in self.pokemons])

        return (f"Pokemon Trainer {self.name}\n"
                f"Pokemon count {len(self.pokemons)}\n"
                f"{pokemons_data}")


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charioted", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
