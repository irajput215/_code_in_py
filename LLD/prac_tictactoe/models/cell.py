from LLD.prac_tictactoe.enums.symbol import Symbol

class Cell:
    def __init__(self,row: int, col: int):
        self._row = row
        self._col = col
        self._symbol = Symbol.EMPTY

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
    def symbol(self, symbol: Symbol):
        self._symbol = symbol

    def is_empty(self) -> bool:
        return self._symbol == Symbol.EMPTY
    
    def __str__(self) -> str:
        return f"({self._row},{self._col}) -> {self._symbol.display_char}"