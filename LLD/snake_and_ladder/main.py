from LLD.snake_and_ladder.controller.game_controller import GameController
from LLD.snake_and_ladder.models.dice import Dice
from LLD.snake_and_ladder.models.snake import Snake
from LLD.snake_and_ladder.models.ladder import Ladder


def main():
    board_entities = [
        Snake(17, 7),
        Snake(54, 34),
        Snake(62, 19),
        Snake(98, 79),
        Ladder(3, 38),
        Ladder(24, 33),
        Ladder(42, 93),
        Ladder(72, 84)
    ]

    player_names = ["Alice", "Bob", "Charlie"]

    game = (GameController.Builder()
        .set_board(100, board_entities)
        .set_players(player_names)
        .set_dice(Dice(1, 6))
        .build())

    game.play()

if __name__ == "__main__":
    main()