"A Data Controller that is a Subject"


class DataController:
    "A Subject (Observable)"

    _observers = set()

    def __new__(cls):
        return cls

    @classmethod
    def subscribe(cls, observer):
        cls._observers.add(observer)

    @classmethod
    def unsubscribe(cls, observer):
        cls._observers.remove(observer)

    @classmethod
    def notify(cls, *args):
        for observer in cls._observers:
            observer.notify(*args)
