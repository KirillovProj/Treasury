from abc import abstractmethod, ABCMeta


class IState(metaclass=ABCMeta):
    "A State Interface"

    @staticmethod
    @abstractmethod
    def __call__():
        "Set the default method"


class Started(IState):
    "A ConcreteState Subclass"

    @staticmethod
    def method():
        "A task of this class"
        print("Task Started")

    __call__ = method


class Running(IState):
    "A ConcreteState Subclass"

    @staticmethod
    def method():
        "A task of this class"
        print("Task Running")

    __call__ = method


class Finished(IState):
    "A ConcreteState Subclass"

    @staticmethod
    def method():
        "A task of this class"
        print("Task Finished")

    __call__ = method
