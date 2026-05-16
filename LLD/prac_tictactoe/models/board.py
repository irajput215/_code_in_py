from LLD.prac_tictactoe.enums.symbol import Symbol
from LLD.prac_tictactoe.models.cell import Cell
from LLD.prac_tictactoe.models.move import Move
from typing import List

class Board:
    def __init__(self, size: int):
        self._size = size
        # initialize board with empty cells
        self._cells : List[List[Cell]] = [[Cell(r,c) for c in range(size)] for r in range(size)]

    @property
    def size(self) -> int:
        return self._size

    @property
    def cells(self) -> List[List[Cell]]:
        return self._cells
    
    def is_full(self) -> bool:
        for row in self._cells:
            for cell in row:
                if cell.is_empty():
                    return False
        return True

    def place_move(self, move: Move) -> bool :
        row = move.row
        col = move.col

        if row<0 or row>=self._size or col<0 or col>=self._size:
            return False
        cell = self._cells[row][col]

        if not cell.is_empty():
            return False
        
        cell.symbol = move.player.symbol
        return True
    
    def print_board(self):
        for row in self._cells:
            values = [cell.symbol.display_char for cell in row]
            print(" | ".join(values))
            print("-" * (self._size * 4 - 1))
        print()
