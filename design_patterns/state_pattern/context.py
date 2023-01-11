import states


class Context:
    "This is the object whose behavior will change"

    def __init__(self):

        self.state_handles = [
            states.Started(),
            states.Running(),
            states.Finished()
        ]
        self._handle = iter(self.state_handles)

    def request(self):
        "Each time the request is called, a new class will handle it"
        try:
            self._handle.__next__()()
        except StopIteration:
            # resetting so it loops
            self._handle = iter(self.state_handles)
