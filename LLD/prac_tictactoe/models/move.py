from LLD.prac_tictactoe.models.player import Player

class Move:
    def __init__(self, player:Player, row:int, col:int):
        self._player = player
        self._row = row
        self._col = col

    @property
    def player(self) -> Player:
        return self._player
    
    @property
    def row(self) -> int:
        return self._row
    
    @property
    def col(self) -> int:
        return self._col
    
    def __str__(self) -> str:
        return f"{self._player.name} made move at ({self._row},{self._col})"
        