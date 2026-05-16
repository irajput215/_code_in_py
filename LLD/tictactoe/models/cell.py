from LLD.tictactoe.enums.symbol import Symbol

# Cell is the smallest unit of the board.
# It holds the state (Symbol) of a single position.
class Cell:
    def __init__(self, row: int, col: int):
        self._row: int = row
        self._col: int = col
        self._symbol: Symbol = Symbol.EMPTY

    @property
    def row(self) -> int:
        return self._row

    @property
    def col(self) -> int:
        return self._col

    @property
    def symbol(self) -> Symbol:
        return self._symbol

    @symbol.setter
    def symbol(self, value: Symbol) -> None:
        self._symbol = value

    def is_empty(self) -> bool:
        return self._symbol == Symbol.EMPTY
