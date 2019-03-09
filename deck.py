from card import Card
from random import shuffle

class Deck:
    def __init__(self):
        self.deck = []
        self.empty = True

    # add (append) a card 
    def addCard(self, card):
        self.deck.append(card)
        self.empty = False

    # remove (pop) the top card
    def takeCard(self):
        if deck.length == 0:
            return False
        if deck.length - 1 == 0:
            self.empty = False
        return self.deck.pop()

    # shuffle the deck
    def shuffle(self):
        shuffle(self.deck)

    # clear and return contents of deck
    def clearDeck(self):
        cards = self.deck
        self.deck = []
        self.empty = True
        return cards

    # set contents of a deck from another deck
    def moveContentsTo(self, deckToTakeFrom):
        cards = deckToTakeFrom.clearContents()
        self.deck = cards

    # to string contents of array
    def toString(self):
        output = ''
