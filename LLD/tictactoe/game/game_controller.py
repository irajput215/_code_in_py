from LLD.tictactoe.models.board import Board
from LLD.tictactoe.models.move import Move
from LLD.tictactoe.enums.game_status import GameStatus

# GameController is the "Orchestrator".
# It coordinates between models (Board, Player, Move) and strategies.
# This follows the Dependency Inversion Principle as it depends on an abstraction (WinningStrategy).
class GameController:
    def __init__(self, size, players, winning_strategy):
        self.board = Board(size)
        self.players = players
        self.winning_strategy = winning_strategy
        self.current_player_index = 0
        self.status = GameStatus.IN_PROGRESS
        self.moves = []

    def get_current_player(self):
        return self.players[self.current_player_index]

    # This is the main "entry point" for game actions.
    def make_move(self, row, col):
        # 1. State check
        if self.status != GameStatus.IN_PROGRESS:
            print("Game is already over.")
            return

        player = self.get_current_player()
        move = Move(row, col, player)
        
        # 2. Delegate board validation and placement to the Board model.
        success = self.board.place_move(move)
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
