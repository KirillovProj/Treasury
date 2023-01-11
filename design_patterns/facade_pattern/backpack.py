class Backpack:
    _contents = []

    def __new__(cls, *args, **kwargs):
        return cls

    @classmethod
    def add_item(cls, item):
        cls._contents.append(item)

    @classmethod
    def get_item(cls, item):
        if item in cls._contents:
            cls._contents.remove(item)
            return item
        else:
            return None

    @classmethod
    def get_contents(cls):
        return cls._contents
