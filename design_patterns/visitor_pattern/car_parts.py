from abc import abstractmethod, ABCMeta


class IVisitable(metaclass=ABCMeta):
    """
    An interface that concrete objects should implement that allows
    the visitor to traverse a hierarchical structure of objects
    """
    @staticmethod
    @abstractmethod
    def accept(visitor):
        """
        The Visitor traverses and accesses each object through this
        method
        """


class AbstractCarPart:
    "The Abstract Car Part"
    @property
    def name(self):
        "a name for the part"
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def sku(self):
        "The Stock Keeping Unit (sku)"
        return self._sku

    @sku.setter
    def sku(self, value):
        self._sku = value

    @property
    def price(self):
        "The price per unit"
        return self._price

    @price.setter
    def price(self, value):
        self._price = value


class Body(AbstractCarPart, IVisitable):
    "A part of the car"

    def __init__(self, name, sku, price):
        self.name = name
        self.sku = sku
        self.price = price

    def accept(self, visitor):
        visitor.visit(self)


class Engine(AbstractCarPart, IVisitable):
    "A part of the car"

    def __init__(self, name, sku, price):
        self.name = name
        self.sku = sku
        self.price = price

    def accept(self, visitor):
        visitor.visit(self)


class Wheel(AbstractCarPart, IVisitable):
    "A part of the car"

    def __init__(self, name, sku, price):
        self.name = name
        self.sku = sku
        self.price = price

    def accept(self, visitor):
        visitor.visit(self)


class Car(AbstractCarPart, IVisitable):
    "A Car with parts"

    def __init__(self, name):
        self.name = name
        self._parts = [
            Body("Utility", "ABC-123-21", 1001),
            Engine("V8 engine", "DEF-456-21", 2555),
            Wheel("FrontLeft", "GHI-789FL-21", 136),
            Wheel("FrontRight", "GHI-789FR-21", 136),
            Wheel("BackLeft", "GHI-789BL-21", 152),
            Wheel("BackRight", "GHI-789BR-21", 152),
        ]

    def accept(self, visitor):
        for parts in self._parts:
            parts.accept(visitor)
        visitor.visit(self)
