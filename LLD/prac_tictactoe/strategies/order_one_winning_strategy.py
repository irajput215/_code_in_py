from LLD.prac_tictactoe.models.move import Move
from LLD.prac_tictactoe.models.board import Board
from LLD.prac_tictactoe.strategies.win_strategy import WinStrategy
from LLD.prac_tictactoe.enums.symbol import Symbol
from typing import Dict, List

class OrderOneWinningStrategy(WinStrategy):
    
    def __init__(self, size: int):
        self._size = size
        self._row_counts: Dict[Symbol, List[int]] = {Symbol.X: [0] * size, Symbol.O: [0] * size}
        self._col_counts: Dict[Symbol, List[int]] = {Symbol.X: [0] * size, Symbol.O: [0] * size}
        self._diag_counts: Dict[Symbol, int] = {Symbol.X: 0, Symbol.O: 0}
        self._anti_diag_counts: Dict[Symbol, int] = {Symbol.X: 0, Symbol.O: 0}

    def check_winner(self, board: Board, move: Move) -> bool:
        row: int = move.row
        col: int = move.col
        symbol: Symbol = move.player.symbol

        # Update the counts for the current move's row and column.
        self._row_counts[symbol][row] += 1
        self._col_counts[symbol][col] += 1

        # Check if the move is on the main diagonal.
        if row == col:
            self._diag_counts[symbol] += 1

        # Check if the move is on the anti-diagonal.
        if row + col == self._size - 1:
            self._anti_diag_counts[symbol] += 1

        # O(1) Check: Just look at the updated counters.
        if (self._row_counts[symbol][row] == self._size or
            self._col_counts[symbol][col] == self._size or
            self._diag_counts[symbol] == self._size or
            self._anti_diag_counts[symbol] == self._size):
            return True

        return False
