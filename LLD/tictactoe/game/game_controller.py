from typing import List
from LLD.tictactoe.models.board import Board
from LLD.tictactoe.models.move import Move
from LLD.tictactoe.models.player import Player
from LLD.tictactoe.strategies.winning_strategy import WinningStrategy
from LLD.tictactoe.enums.game_status import GameStatus

# GameController is the "Orchestrator".
# It coordinates between models (Board, Player, Move) and strategies.
# This follows the Dependency Inversion Principle as it depends on an abstraction (WinningStrategy).
class GameController:
    """
    The GameController demonstrates both Composition and Aggregation:
    
    1. Composition (Death Relationship): 
       - 'self.board' is created inside the constructor. 
       - The board's lifecycle is tied to the controller; if the controller is destroyed, the board is too.
    
    2. Aggregation (Has-a Relationship): 
       - 'self.players' and 'self.winning_strategy' are passed from outside (Dependency Injection).
       - They can exist independently of the GameController (e.g., players can exist in a database).
    """
    def __init__(self, size: int, players: List[Player], winning_strategy: WinningStrategy):
        self.board: Board = Board(size)
        self.players: List[Player] = players
        self.winning_strategy: WinningStrategy = winning_strategy
        self.current_player_index: int = 0
        self.status: GameStatus = GameStatus.IN_PROGRESS
        self.moves: List[Move] = []

    def get_current_player(self) -> Player:
        return self.players[self.current_player_index]

    # This is the main "entry point" for game actions.
    def make_move(self, row: int, col: int) -> None:
        # 1. State check
        if self.status != GameStatus.IN_PROGRESS:
            print("Game is already over.")
            return

        player: Player = self.get_current_player()
        move: Move = Move(row, col, player)
        
        # 2. Delegate board validation and placement to the Board model.
        success: bool = self.board.place_move(move)
        if not success:
            print(f"Invalid move by {player.name} at ({row}, {col})")
            return

        # 3. Update game history
        self.moves.append(move)
        print(f"{player.name} placed {player.symbol.value} at ({row}, {col})")
        self.board.print_board()

        # 4. Delegate winning logic to the Strategy.
        if self.winning_strategy.check_winner(self.board, move):
            self.status = GameStatus.WIN
            print(f"🎉 {player.name} wins!")
            return

        # 5. Check for Draw
        if self.board.is_full():
            self.status = GameStatus.DRAW
            print("🤝 It's a draw!")
            return

        # 6. Switch turn
        self.current_player_index = (self.current_player_index + 1) % len(self.players)
