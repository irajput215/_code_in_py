from LLD.prac_tictactoe.enums.symbol import Symbol


# Player class follows SRP (Single Responsibility Principle).
# It only stores player-related information.

class Player:

    def __init__(self, name: str, symbol: Symbol):
       # validation check
        if symbol == Symbol.EMPTY:
            raise ValueError("Player cannot have EMPTY symbol")

        self._name = name
        # storing symbol in-self which mean it is association relationship
        self._symbol = symbol 
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def symbol(self) -> Symbol:
        return self._symbol
    
    def __str__(self) -> str:
        return f"{self._name} ({self._symbol.display_char})"


# Inheritance is used for BotPlayer to extend the behavior of a Player.

