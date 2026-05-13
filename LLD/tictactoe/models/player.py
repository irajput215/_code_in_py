# Player class follows SRP (Single Responsibility Principle).
# It only stores player-related information.
class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

# Inheritance is used for BotPlayer to extend the behavior of a Player.
class BotPlayer(Player):
    def __init__(self, name, symbol, difficulty):
        super().__init__(name, symbol)
        self.difficulty = difficulty
