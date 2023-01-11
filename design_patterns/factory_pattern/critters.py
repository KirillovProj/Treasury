from abc import ABCMeta, abstractmethod


class CritterInterface(metaclass=ABCMeta):
    """
    Critter interface
    """
    @staticmethod
    @abstractmethod
    def get_name():
        """
        Method that will return name of the object
        :return: name: str
        """
        pass


class SmallCritter(CritterInterface):
    name = 'small critter'

    def get_name(self):
        return self.name


class MediumCritter(CritterInterface):
    name = 'medium critter'

    def get_name(self):
        return self.name


class BigCritter(CritterInterface):
    name = 'big critter'

    def get_name(self):
        return self.name
