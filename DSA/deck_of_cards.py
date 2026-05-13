from abc import ABC, abstractmethod
from enum import Enum
import random

class Suit(Enum):
    HEART = "Hearts"
    DIAMOND = "Diamonds"
    CLUBS = "Clubs"
    SPADE = "Spades"

class Card(ABC):
    def __init__(self, value, suit):
        self._value = value  # Internal raw value (1-13)
        self.suit = suit
        self.is_available = True

    @property
    @abstractmethod
    def value(self):
        pass

    def __repr__(self):
        # Convert internal 1, 11, 12, 13 to names
        names = {1: "Ace", 11: "Jack", 12: "Queen", 13: "King"}
        card_name = names.get(self._value, str(self._value))
        return f"{card_name} of {self.suit.value}"

class BlackJackCard(Card):
    @property
    def value(self):
        if self.is_ace():
            return 1 
        if 10 <= self._value <= 13:
            return 10
        return self._value

    def is_ace(self):
        return self._value == 1

class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def show_cards(self):
        return ", ".join([str(card) for card in self.cards])

class BlackJackHand(Hand):
    def possible_scores(self):
        scores = {0}
        for card in self.cards:
            new_scores = set()
            for s in scores:
                new_scores.add(s + card.value)
                if card.is_ace():
                    new_scores.add(s + 11)
            scores = new_scores
        return scores

    def score(self):
        scores = self.possible_scores()
        valid_scores = [s for s in scores if s <= 21]
        return max(valid_scores) if valid_scores else min(scores)

class Deck:
    def __init__(self):
        self.cards = [BlackJackCard(v, s) for s in Suit for v in range(1, 14)]
        self.deal_index = 0

    def shuffle(self):
        random.shuffle(self.cards)
        self.deal_index = 0

    def deal_card(self):
        if self.deal_index < len(self.cards):
            card = self.cards[self.deal_index]
            self.deal_index += 1
            return card
        return None

# --- Execution ---
deck = Deck()
deck.shuffle()

player_hand = BlackJackHand()

# Deal two cards
player_hand.add_card(deck.deal_card())
player_hand.add_card(deck.deal_card())

# Output
print("--- Player's Hand ---")
print(f"Cards: {player_hand.show_cards()}")
print(f"Total Score: {player_hand.score()}")