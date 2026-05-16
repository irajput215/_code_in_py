from typing import Dict, List
from LLD.tictactoe.strategies.winning_strategy import WinningStrategy
from LLD.tictactoe.enums.symbol import Symbol
from LLD.tictactoe.models.board import Board
from LLD.tictactoe.models.move import Move

# This is an optimized implementation of the WinningStrategy.
# Time Complexity: O(1) - We don't traverse the whole board.
# Space Complexity: O(N) - We store counts for each row and column.
class OrderOneWinningStrategy(WinningStrategy):
    def __init__(self, size: int):
        self.size: int = size
        # We use counters to track how many symbols are in each row, column, and diagonal.
        # Once a counter reaches 'size', we have a winner!
        self.row_counts: Dict[Symbol, List[int]] = {Symbol.X: [0] * size, Symbol.O: [0] * size}
        self.col_counts: Dict[Symbol, List[int]] = {Symbol.X: [0] * size, Symbol.O: [0] * size}
        self.diag_counts: Dict[Symbol, int] = {Symbol.X: 0, Symbol.O: 0}
        self.anti_diag_counts: Dict[Symbol, int] = {Symbol.X: 0, Symbol.O: 0}

    def check_winner(self, board: Board, move: Move) -> bool:
        row: int = move.row
        col: int = move.col
        symbol: Symbol = move.player.symbol

        # Update the counts for the current move's row and column.
        self.row_counts[symbol][row] += 1
        self.col_counts[symbol][col] += 1
        
        # Check if the move is on the main diagonal.
        if row == col:
            self.diag_counts[symbol] += 1
        
        # Check if the move is on the anti-diagonal.
        if row + col == self.size - 1:
            self.anti_diag_counts[symbol] += 1

        # O(1) Check: Just look at the updated counters.
        if (self.row_counts[symbol][row] == self.size or
            self.col_counts[symbol][col] == self.size or
            self.diag_counts[symbol] == self.size or
            self.anti_diag_counts[symbol] == self.size):
            return True
            
        return False
