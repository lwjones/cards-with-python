from card import Card, Suit
from deck import Deck
from hand import Hand



newCard = Card(Suit.clubs, "3")
print(newCard)
defaultCard = Card()
print(defaultCard)

dealerDeck = Deck()
discardDeck = Deck()
playerHand = Hand()

for value in "A23456789TJQK":
    for suit in Suit:
        card = Card(suit, value)
        dealerDeck.addCard(card)

print(dealerDeck)
dealerDeck.shuffle()
print(dealerDeck.toString())
playerHand.addCard(dealerDeck.takeCard())
playerHand.addCard(dealerDeck.takeCard())
playerHand.addCard(dealerDeck.takeCard())
playerHand.addCard(dealerDeck.takeCard())
playerHand.addCard(dealerDeck.takeCard())

print(playerHand.toString())
cardToPlay = playerHand.takeCard(2)
discardDeck.addCard(cardToPlay)
cardToPlay = playerHand.takeCard(0)
discardDeck.addCard(cardToPlay)
print("Player's Hand: " + playerHand.toString())
print("Discard Pile: " + discardDeck.toString())