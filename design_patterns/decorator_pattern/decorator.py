class Decorator:
    def __init__(self, obj):
        self.object = obj

    def method(self):
        print('Calling a method from decorator_pattern')
        self.object.method()


class Decorated:
    def method(self):
        print('Some method called from its class')


Decorator(Decorator(Decorated())).method()  # You can call it recursively
