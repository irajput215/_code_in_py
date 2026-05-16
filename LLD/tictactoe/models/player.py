from LLD.tictactoe.enums.symbol import Symbol

# Player class follows SRP (Single Responsibility Principle).
# It only stores player-related information.
class Player:
    def __init__(self, name: str, symbol: Symbol):
        # Validation: A player must have a valid game symbol (X or O).
        if symbol == Symbol.EMPTY:
            raise ValueError("Player cannot have EMPTY symbol")
        
        # Encapsulation: Using private variables (prefixed with _)
        self._name: str = name
        self._symbol: Symbol = symbol

    @property
    def name(self) -> str:
        return self._name

    @property
    def symbol(self) -> Symbol:
        return self._symbol

    def __str__(self) -> str:
        return f"{self._name} ({self._symbol.display_char})"

# Inheritance is used for BotPlayer to extend the behavior of a Player.
class BotPlayer(Player):
    def __init__(self, name: str, symbol: Symbol, difficulty: str):
        super().__init__(name, symbol)
        self._difficulty: str = difficulty

    @property
    def difficulty(self) -> str:
        return self._difficulty
