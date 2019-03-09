from enum import Enum

VALUES = "A23456789TJQK"
DEFAULT_VALUE = "A"
Suit = Enum("Suit", "clubs diamonds hearts spades")
DEFAULT_SUIT = Suit.spades


class Card:
    def __init__(self, suit=DEFAULT_SUIT, value=DEFAULT_VALUE):
        self.suit = suit.name
        self.value = value

    def __repr__(self):
        return self.toString()

    def toString(self):
        return "{value} of {suit}".format(value=str(self.value), suit=self.suit.title())