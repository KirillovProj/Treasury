from trainer import Trainer
from backpack import Backpack
from pokemon import Pokemon


class Facade:
    @staticmethod
    def attack():
        Pokemon.attack()

    @staticmethod
    def check_backpack():
        Trainer.check_backpack()

    @staticmethod
    def add_item_to_backpack(item):
        Backpack.add_item(item)
