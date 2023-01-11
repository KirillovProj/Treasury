from abc import abstractmethod, ABCMeta


class IVisitor(metaclass=ABCMeta):
    "An interface that custom Visitors should implement"
    @staticmethod
    @abstractmethod
    def visit(element):
        "Visitors visit Elements/Objects within the application"


class PrintPartsVisitor(IVisitor):
    "Print out the part name and sku"
    @staticmethod
    def visit(element):
        if hasattr(element, 'sku'):
            print(f"{element.name}\t:{element.sku}".expandtabs(6))


class TotalPriceVisitor(IVisitor):
    "Print out the total cost of the parts in the car"
    total_price = 0

    @classmethod
    def visit(cls, element):
        if hasattr(element, 'price'):
            cls.total_price += element.price
        return cls.total_price
