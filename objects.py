# imports needed module
import random

ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
suits = ["Hearts", "Spades", "Diamonds", "Clubs"]
points = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Jack": 10, "Queen": 10, "King": 10,
          "Ace": 11}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = points[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))
        self.count = len(self.deck)

    def __str__(self):
        deckComp = ""
        for card in self.deck:
            deckComp += card.__str__() + ", "
        return "Deck: " + deckComp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        oneCard = self.deck.pop()
        self.count -= 1
        return oneCard


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
        self.count = len(self.cards)
        self.__list = []

    def addCard(self, card):
        self.cards.append(card)
        self.count += 1
        self.value += card.value
        if card.rank == "Ace":
            self.aces += 1

    def checkForAce(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

    def __iter__(self):
        self.__index = -1
        return self

    def __next__(self):
        if self.__index == len(self.__list) - 1:
            raise StopIteration
        self.__index += 1
        card = self.__list[self.__index]
        return card


deck = Deck()
deck.shuffle()
yourHand = Hand()
yourHand.addCard(deck.deal())
yourHand.addCard(deck.deal())
dealerHand = Hand()
dealerHand.addCard(deck.deal())
dealerHand.addCard(deck.deal())
dealerShowCard = dealerHand.cards[0]


# function to draw another card
def hit(cardDeck, hand):
    hand.addCard(cardDeck.deal())
    hand.checkForAce()
    print("YOUR CARDS: ")
    i = 0
    while i < len(yourHand.cards):
        print(yourHand.cards[i])
        i += 1
    print()


# function for dealer to play if you stand
def stand():
    global dealerHand
    dealerHand.addCard(deck.deal())
    print("DEALER'S CARDS: ")
    i = 0
    while i < len(dealerHand.cards):
        print(dealerHand.cards[i])
        i += 1
    dealerHand.checkForAce()
    print()


# checks to see if you got a blackjack
def blackjack():
    if (yourHand.cards[0].rank == "Ace") and (yourHand.cards[1].value == 10):
        return True
    elif (yourHand.cards[0].value == 10) and (yourHand.cards[1].value == "Ace"):
        return True
    return False


# function to reshuffle the deck, get new cards, assign the new point values, and reset the deck position
def play():
    global deck
    global dealerHand
    global dealerShowCard
    global yourHand
    deck.shuffle()
    yourHand = Hand()
    yourHand.addCard(deck.deal())
    yourHand.addCard(deck.deal())
    dealerHand = Hand()
    dealerHand.addCard(deck.deal())
    dealerHand.addCard(deck.deal())
    dealerShowCard = dealerHand.cards[0]
