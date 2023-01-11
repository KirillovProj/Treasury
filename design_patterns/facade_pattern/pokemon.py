import random

class Pokemon:
    def __init__(self, name, lvl):
        self.name = name
        self.lvl = lvl
        self.status = 'neutral'
        self.hp = 100
        self.moves = 5

    def apply_item(self, item):
        if item == 'healing item':
            self.hp += 100
        elif item == 'status item':
            if self.status == 'negative':
                self.status = 'neutral'
            else:
                print('No need to use item on that pokemon now!')

    @staticmethod
    def attack():
        hit = random.randint(0, 1)
        if hit:
            print('Target is dead')
        else:
            print('You missed!')
