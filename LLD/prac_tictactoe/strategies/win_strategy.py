from abc import ABC, abstractmethod

from LLD.prac_tictactoe.models.move import Move
from LLD.prac_tictactoe.models.board import Board

class WinStrategy(ABC):

    @abstractmethod
    def check_winner(self, board: Board, move: Move) -> bool:
        pass
