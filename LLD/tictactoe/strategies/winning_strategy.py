from abc import ABC, abstractmethod
from LLD.tictactoe.models.board import Board
from LLD.tictactoe.models.move import Move

# The Strategy Pattern is used here to decouple the winning logic from the GameController.
# This allows us to plug in different algorithms (e.g., O(N) vs O(1)) easily.
class WinningStrategy(ABC):
    @abstractmethod
    def check_winner(self, board: Board, move: Move) -> bool:
        pass
