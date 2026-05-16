from typing import List
from LLD.tictactoe.models.cell import Cell
from LLD.tictactoe.models.move import Move

# Board manages the grid and low-level validation.
# It doesn't know about game rules (like winning), only about its own state.
class Board:
    def __init__(self, size: int):
        # Validation: Board size must be positive.
        if size <= 0:
            raise ValueError("Board size must be positive")
            
        self._size: int = size
        # Composition: Board contains multiple Cell objects.
        self._cells: List[List[Cell]] = [
            [Cell(i, j) for j in range(size)]
            for i in range(size)
        ]

    @property
    def size(self) -> int:
        return self._size

    @property
    def cells(self) -> List[List[Cell]]:
        return self._cells

    # This method only cares if a move is physically possible on the grid.
    def place_move(self, move: Move) -> bool:
        row: int = move.row
        col: int = move.col

        # Boundary validation
        if row < 0 or row >= self._size or col < 0 or col >= self._size:
            return False

        cell: Cell = self._cells[row][col]
        # Occupancy validation
        if not cell.is_empty():
            return False

        # State update (uses the cell's setter)
        cell.symbol = move.player.symbol
        return True

    def is_full(self) -> bool:
        for row in self._cells:
            for cell in row:
                if cell.is_empty():
                    return False
        return True

    def print_board(self) -> None:
        for row in self._cells:
            values: List[str] = [cell.symbol.display_char for cell in row]
            print(" | ".join(values))
            print("-" * (self._size * 4 - 1))
        print()
