
"Each component stays synchronized through a mediator"
from abc import ABCMeta, abstractmethod


class IComponent(metaclass=ABCMeta):
    "An interface that each component will implement"

    @staticmethod
    @abstractmethod
    def notify(message):
        "The required notify method"

    @staticmethod
    @abstractmethod
    def receive(message):
        "The required receive method"


class Component(IComponent):
    "Each component stays synchronized through a mediator"

    def __init__(self, mediator, name):
        self._mediator = mediator
        self._name = name

    def notify(self, message):
        print(self._name + ": >>> Out >>> : " + message)
        self._mediator.notify(message, self)

    def receive(self, message):
        print(self._name + ": <<< In <<< : " + message)
