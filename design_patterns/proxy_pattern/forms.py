"A Lion Class"
import random
from interface import IProteus


class Lion(IProteus):
    "Proteus in the form of a Lion"

    name = "Lion"

    def tell_me_the_future(self):
        "Proteus will change to something random"
        self.__class__ = Leopard if random.randint(
            0, 1) else Serpent

    @classmethod
    def tell_me_your_form(cls):
        print("I am the form of a " + cls.name)


class Serpent(IProteus):
    "Proteus in the form of a Serpent"

    name = "Serpent"

    def tell_me_the_future(self):
        "Proteus will change to something random"
        self.__class__ = Leopard if random.randint(0, 1) else Lion

    @classmethod
    def tell_me_your_form(cls):
        print("I am the form of a " + cls.name)


class Leopard(IProteus):
    "Proteus in the form of a Leopard"

    name = "Leopard"

    def tell_me_the_future(self):
        "Proteus will change to something random"
        self.__class__ = Serpent if random.randint(0, 1) else Lion

    @classmethod
    def tell_me_your_form(cls):
        print("I am the form of a " + cls.name)