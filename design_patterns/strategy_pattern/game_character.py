class GameCharacter:
    "This is the context whose strategy will change"

    position = [0, 0]

    @classmethod
    def move(cls, movement_style):
        "The movement algorithm has been decided by the client"
        movement_style(cls.position)
