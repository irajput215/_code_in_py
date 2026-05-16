from typing import List, Deque
from collections import deque
from LLD.snake_and_ladder.models.board import Board
from LLD.snake_and_ladder.models.player import Player
from LLD.snake_and_ladder.models.dice import Dice
from LLD.snake_and_ladder.models.board_entity import BoardEntity
from LLD.snake_and_ladder.enums.game_status import GameStatus

class GameController:
    def __init__(self, board: Board, players: List[Player], dice: Dice):
        self._board = board
        self._players: Deque[Player] = deque(players)
        self._dice = dice
        self._status = GameStatus.NOT_STARTED
        self._winners: List[Player] = []

    class Builder:
        def __init__(self):
            self._board_size = 100
            self._board_entities = []
            self._player_names = []
            self._dice = None

        def set_board(self, size: int, entities: List[BoardEntity]):
            self._board_size = size
            self._board_entities = entities
            return self

        def set_players(self, names: List[str]):
            self._player_names = names
            return self

        def set_dice(self, dice: Dice):
            self._dice = dice
            return self

        def build(self):
            board = Board(self._board_size, self._board_entities)
            players = [Player(name) for name in self._player_names]
            if not self._dice:
                self._dice = Dice(1, 6)
            return GameController(board, players, self._dice)

    def play(self):
        self._status = GameStatus.IN_PROGRESS
        print(f"Game started with {len(self._players)} players.")

        while len(self._players) > 1:
            current_player = self._players.popleft()
            
            self._dice.reset_rolls_counter()
            roll = self._dice.roll()
            
            old_position = current_player.position
            new_position = old_position + roll
            
            if new_position > self._board.size:
                print(f"{current_player.name} rolled a {roll} but cannot move beyond {self._board.size}. Stays at {old_position}.")
                self._players.append(current_player)
                continue
            
            # Check for snakes/ladders
            final_position = self._board.get_final_position(new_position)
            
            if final_position > new_position:
                print(f"{current_player.name} rolled a {roll} and climbed a ladder from {new_position} to {final_position}!")
            elif final_position < new_position:
                print(f"{current_player.name} rolled a {roll} and was bitten by a snake from {new_position} to {final_position}!")
            else:
                print(f"{current_player.name} rolled a {roll} and moved from {old_position} to {new_position}.")
            
            current_player.position = final_position
            
            if current_player.position == self._board.size:
                print(f"*** {current_player.name} has finished the game! ***")
                self._winners.append(current_player)
            else:
                self._players.append(current_player)

        self._status = GameStatus.FINISHED
        print("\nGame over!")
        print("Rankings:")
        for i, winner in enumerate(self._winners):
            print(f"{i+1}. {winner.name}")
        if self._players:
            print(f"{len(self._winners)+1}. {self._players[0].name}")