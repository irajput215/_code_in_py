from LLD.prac_tictactoe.enums.game_status import GameStatus
from LLD.prac_tictactoe.models.player import Player
from LLD.prac_tictactoe.models.move import Move
from LLD.prac_tictactoe.models.board import Board
from LLD.prac_tictactoe.strategies.win_strategy import WinStrategy
from LLD.prac_tictactoe.models.score_card import ScoreCard
from typing import List, Optional

class GameController:

    def __init__(self, size: int, players: List[Player], win_strategy: WinStrategy, score_card: Optional[ScoreCard] = None):
        self._size = size
        self._players = players
        self._win_strategy = win_strategy
        self._moves: List[Move] = []
        self._board: Board = Board(size)
        self._current_player_index = 0
        self._status = GameStatus.IN_PROGRESS
        self._score_card = score_card if score_card else ScoreCard()

    def get_current_player(self) -> Player:
        return self._players[self._current_player_index]

    # This is the main "entry point" for game actions.
    def make_move(self, row: int, col: int) -> None:
        # 1. State check
        if self._status != GameStatus.IN_PROGRESS:
            print("Game is already over.")
            return

        player: Player = self.get_current_player()
        move: Move = Move(player, row, col)
        
        # 2. Delegate board validation and placement to the Board model.
        success: bool = self._board.place_move(move)
        if not success:
            print(f"Invalid move by {player.name} at ({row}, {col})")
            return

        # 3. Update game history
        self._moves.append(move)
        print(f"{player.name} placed {player.symbol.value} at ({row}, {col})")
        self._board.print_board()

        # 4. Delegate winning logic to the Strategy.
        if self._win_strategy.check_winner(self._board, move):
            self._status = GameStatus.WIN
            print(f"🎉 {player.name} wins!")
            self._score_card.update_win(player)
            return

        # 5. Check for Draw
        if self._board.is_full():
            self._status = GameStatus.DRAW
            print("🤝 It's a draw!")
            return

        # 6. Switch turn
        self._current_player_index = (self._current_player_index + 1) % len(self._players)

    def display_score_card(self) -> None:
        self._score_card.display_scores()
