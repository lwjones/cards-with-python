from card import Card
from random import shuffle

class Deck:
    def __init__(self):
        self.cards = []
        self.empty = True

    # add (append) a card 
    def addCard(self, card):
        self.cards.append(card)
        self.empty = False

    # remove (pop) the top card
    def takeCard(self):
        if len(self.cards) == 0:
            return False
        if len(self.cards) - 1 == 0:
            self.empty = False
        return self.cards.pop()

    # shuffle the deck
    def shuffle(self):
        cards = self.cards
        shuffle(cards)
        self.cards = cards

    # clear and return contents of deck
    def clearCards(self):
        cards = self.cards
        self.cards = []
        self.empty = True
        return cards

    # set contents of a deck from another deck
    def moveContentsTo(self, deckToTakeFrom):
        cards = deckToTakeFrom.clearDeck()
        self.cards = cards

    # to string contents of array
    def toString(self):
        output = ""
        lastIndex = len(self.cards)
        for idx, card in enumerate(self.cards):
            output += card.toString()
            if idx != lastIndex - 1:
                output += ', '
        return output
