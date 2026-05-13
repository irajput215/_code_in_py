from enum import Enum

# GameStatus keeps track of the state of the game.
# Using an Enum avoids using "magic numbers" or strings.
class GameStatus(Enum):
    IN_PROGRESS = 1
    WIN = 2
    DRAW = 3
