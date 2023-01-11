from abc import abstractmethod, ABCMeta


class IMove(metaclass=ABCMeta):
    "A Concrete Strategy Interface"

    @staticmethod
    @abstractmethod
    def __call__():
        "Implementors must select the default method"


class Walking(IMove):
    "A Concrete Strategy Subclass"

    @staticmethod
    def walk(position):
        "A walk algorithm"
        position[0] += 1
        print(f"I am Walking. New position = {position}")

    __call__ = walk


class Running(IMove):
    "A Concrete Strategy Subclass"

    @staticmethod
    def run(position):
        "A run algorithm"
        position[0] += 2
        print(f"I am Running. New position = {position}")

    __call__ = run


class Crawling(IMove):
    "A Concrete Strategy Subclass"

    @staticmethod
    def crawl(position):
        "A crawl algorithm"
        position[0] += 0.5
        print(f"I am Crawling. New position = {position}")

    __call__ = crawl
