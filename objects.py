# imports needed module
import random
import db

# variables to build the deck
ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
suits = ["H", "S", "D", "C"]
points = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Jack": 10, "Queen": 10, "King": 10,
          "Ace": 11}


# card class
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = points[rank]

    def __str__(self):
        return self.rank + self.suit


# deck class
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

    # shuffles the deck
    def shuffle(self):
        random.shuffle(self.deck)

    # deals the cards
    def deal(self):
        oneCard = self.deck.pop()
        self.count -= 1
        return oneCard


# hand class
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
        self.count = len(self.cards)
        self.__list = []

    # adds card to hand
    def addCard(self, card):
        self.cards.append(card)
        self.count += 1
        self.value += card.value
        if card.rank == "Ace":
            self.aces += 1

    # changes value of ace if needed
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

    def __str__(self):
        cardStr = ""
        for card in self.cards:
            cardStr += str(card) + " "
        return cardStr


# session class
class Session:
    def __init__(self, row):
        self.sessionID = row[0]
        self.startTime = row[1]
        self.startMoney = row[2]
        self.stopTime = row[3]
        self.stopMoney = row[4]


# builds deck and both player's hands
deck = Deck()
deck.shuffle()
yourHand = Hand()
yourHand.addCard(deck.deal())
yourHand.addCard(deck.deal())
dealerHand = Hand()
dealerHand.addCard(deck.deal())
dealerHand.addCard(deck.deal())
dealerShowCard = dealerHand.cards[0]
