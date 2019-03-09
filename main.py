from card import Card, Suit
from deck import Deck



newCard = Card(Suit.clubs, "3")
print(newCard)
defaultCard = Card()
print(defaultCard)

dealerDeck = Deck()

for value in "A23456789TJQK":
    for suit in Suit:
        card = Card(suit, value)
        dealerDeck.addCard(card)

print(dealerDeck)
dealerDeck.shuffle()
print(dealerDeck)