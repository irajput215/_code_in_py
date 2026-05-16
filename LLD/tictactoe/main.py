from LLD.tictactoe.models.player import Player
from LLD.tictactoe.enums.symbol import Symbol
from LLD.tictactoe.strategies.order_one_winning_strategy import OrderOneWinningStrategy
from LLD.tictactoe.game.game_controller import GameController

def main() -> None:
    # 1. Dependency Injection: We create the dependencies (Players, Strategy) 
    # and inject them into the GameController.
    player1: Player = Player("Ishu", Symbol.X)
    player2: Player = Player("Alex", Symbol.O)
    
    # 2. Strategy Selection: We choose which algorithm to use.
    # This makes the system flexible and easy to test.
    size: int = 3
    winning_strategy: OrderOneWinningStrategy = OrderOneWinningStrategy(size)
    
    # 3. Initialize Game
    game: GameController = GameController(size, [player1, player2], winning_strategy)
    
    # 4. Simulate a Win for Ishu
    # X - -
    # - - -
    # - - -
    game.make_move(0, 0)
    
    # X - -
    # O - -
    # - - -
    game.make_move(1, 0)
    
    # X X -
    # O - -
    # - - -
    game.make_move(0, 1)
    
    # X X -
    # O O -
    # - - -
    game.make_move(1, 1)
    
    # X X X
    # O O -
    # - - -
    game.make_move(0, 2)

    print("\n--- Game Simulation Complete ---")

if __name__ == "__main__":
    main()
