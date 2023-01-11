from backpack import Backpack
from pokemon import Pokemon


class Trainer:
    def __init__(self):
        self.pokemon_list = [Pokemon('Pikachu', 5)]

    def use_item(self, item, pokemon):
        item = Backpack.get_item(item)
        if item:
            if pokemon in self.pokemon_list:
                pokemon.apply_item(item)
            else:
                print('There is no such pokemon')
        else:
            print('There is no such item')

    def catch_pokemon(self, name, lvl):
        self.pokemon_list.append(Pokemon(name, lvl))

    def check_pokemons(self):
        if not self.pokemon_list:
            print('You have not caught a single pokemon yet!')
        else:
            for pokemon in self.pokemon_list:
                print(pokemon.name, pokemon.lvl, pokemon.status)

    @staticmethod
    def check_backpack():
        items = Backpack.get_contents()
        if not items:
            print('Oh no! There are no items in your backpack')
        else:
            for item in items:
                print(item)
