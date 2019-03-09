from card import Card, Suit
from deck import Deck

class Hand(Deck):
    
    # remove a user specified card, no matter where the card occurs
    def takeCard(self, cardIndex):
        if len(self.cards) == 0:
            return False
        if len(self.cards) - 1 == 0:
            self.empty = False
        return self.cards.pop(cardIndex)

