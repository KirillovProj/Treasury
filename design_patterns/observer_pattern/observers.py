"An observer"


class TableView:
    "The concrete observer"

    def __init__(self, observable):
        self._observable = observable
        self._id = self._observable.subscribe(self)

    def notify(self, data):
        print(f"TableView, id:{self._id}")
        self.draw(data)

    def draw(self, data):
        print(f"Drawing a Table view using data:{data}")

    def delete(self):
        self._observable.unsubscribe(self._id)


class BarGraphView:
    "The concrete observer"

    def __init__(self, observable):
        self._observable = observable
        self._id = self._observable.subscribe(self)

    def notify(self, data):
        print(f"BarGraph, id:{self._id}")
        self.draw(data)

    def draw(self, data):
        print(f"Drawing a Bar graph using data:{data}")

    def delete(self):
        self._observable.unsubscribe(self._id)


class PieGraphView:
    "The concrete observer"

    def __init__(self, observable):
        self._observable = observable
        self._id = self._observable.subscribe(self)

    def notify(self, data):
        print(f"PieGraph, id:{self._id}")
        self.draw(data)

    def draw(self, data):
        print(f"Drawing a Pie graph using data:{data}")

    def delete(self):
        self._observable.unsubscribe(self._id)
