"The Strategy Pattern Example Use Case"
import movements
from game_character import GameCharacter


GAME_CHARACTER = GameCharacter()
GAME_CHARACTER.move(movements.Walking())
# Character sees the enemy
GAME_CHARACTER.move(movements.Running())
# Character finds a small cave to hide in
GAME_CHARACTER.move(movements.Crawling())
