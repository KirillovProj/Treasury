"The ATM Dispenser Chain"
from dispencers import Dispenser10, Dispenser20, Dispenser50


class ATMDispenserChain:  # pylint: disable=too-few-public-methods
    "The Chain Client"

    def __init__(self):
        # initializing the successors chain
        self.chain1 = Dispenser50()
        self.chain2 = Dispenser20()
        self.chain3 = Dispenser10()
        # Setting a default successor chain that will process the 50s
        # first, the 20s second and the 10s last. The successor chain
        # will be recalculated dynamically at runtime.
        self.chain1.next_successor(self.chain2)
        self.chain2.next_successor(self.chain3)
