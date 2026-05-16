from LLD.tictactoe.models.player import Player

# Move is a data transfer object (DTO) or a simple record.
# It encapsulates all information needed to represent a player's action.
class Move:
    def __init__(self, row: int, col: int, player: Player):
        self._row: int = row
        self._col: int = col
        self._player: Player = player

    @property
    def row(self) -> int:
        return self._row

    @property
    def col(self) -> int:
        return self._col

    @property
    def player(self) -> Player:
        return self._player
