import argparse
import sys
from LLD.prac_tictactoe.models.player import Player
from LLD.prac_tictactoe.enums.symbol import Symbol
from LLD.prac_tictactoe.strategies.order_one_winning_strategy import OrderOneWinningStrategy
from LLD.prac_tictactoe.game.game_controller import GameController
from LLD.prac_tictactoe.models.score_card import ScoreCard

def main() -> None:
    # 1. Argument Parsing for Reset Command
    parser = argparse.ArgumentParser(description="Tic Tac Toe Game with persistent scoring.")
    parser.add_argument("--reset", action="store_true", help="Reset the ScoreCard database to 0.")
    args = parser.parse_args()

    # 2. Initialize ScoreCard
    score_card: ScoreCard = ScoreCard()

    # 3. Handle Reset Command
    if args.reset:
        score_card.reset_scores()
        return  # Exit after reset if requested

    # 4. Standard Game Initialization
    # Dependency Injection: We create the dependencies (Players, Strategy) 
    player1: Player = Player("Ishu", Symbol.X)
    player2: Player = Player("Alex", Symbol.O)
    
    size: int = 3
    winning_strategy: OrderOneWinningStrategy = OrderOneWinningStrategy(size)
    
    # 5. Initialize Game Controller
    game: GameController = GameController(size, [player1, player2], winning_strategy, score_card)
    
    # 6. Simulate a Win for Ishu
    # Round 1 Simulation
    game.make_move(0, 0)
    game.make_move(1, 0)
    game.make_move(0, 1)
    game.make_move(1, 1)
    game.make_move(0, 2)

    # 7. Display Final ScoreCard
    game.display_score_card()

    print("\n--- Game Simulation Complete ---")

if __name__ == "__main__":
    main()
