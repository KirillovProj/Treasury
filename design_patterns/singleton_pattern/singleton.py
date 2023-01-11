class Singleton(type):
    def __init__(self, name, bases, namespace):
        super(Singleton, self).__init__(name, bases, namespace)
        self._instance = super(Singleton, self).__call__()

    def __call__(self, *args, **kw):
        return self._instance


class SingleObject(metaclass=Singleton):
    counter = 0

    def __init__(self):
        print('You will see it once')

    def do_something(self):
        self.counter += 1
