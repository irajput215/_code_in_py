from LLD.tictactoe.enums.symbol import Symbol

# Cell is the smallest unit of the board.
# It holds the state (Symbol) of a single position.
class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.symbol = Symbol.EMPTY

    def is_empty(self):
        return self.symbol == Symbol.EMPTY
