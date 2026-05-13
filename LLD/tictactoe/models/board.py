from LLD.tictactoe.models.cell import Cell

# Board manages the grid and low-level validation.
# It doesn't know about game rules (like winning), only about its own state.
class Board:
    def __init__(self, size):
        self.size = size
        # Composition: Board contains multiple Cell objects.
        self.cells = [
            [Cell(i, j) for j in range(size)]
            for i in range(size)
        ]

    # This method only cares if a move is physically possible on the grid.
    def place_move(self, move):
        row = move.row
        col = move.col

        # Boundary validation
        if row < 0 or row >= self.size or col < 0 or col >= self.size:
            return False

        cell = self.cells[row][col]
        # Occupancy validation
        if not cell.is_empty():
            return False

        # State update
        cell.symbol = move.player.symbol
        return True

    def is_full(self):
        for row in self.cells:
            for cell in row:
                if cell.is_empty():
                    return False
        return True

    def print_board(self):
        for row in self.cells:
            values = [cell.symbol.value for cell in row]
            print(" | ".join(values))
            print("-" * (self.size * 4 - 1))
        print()
