# imports needed module
import random


# creates the deck of cards as a dictionary, shuffles them, deals them, and gives points
deck = {'Ace of Clubs': ["Ace", "Clubs", 1], '2 of Clubs': [2, "Clubs", 2], '3 of Clubs': [3, "Clubs", 3],
        '4 of Clubs': [4, "Clubs", 4], '5 of Clubs': [5, "Clubs", 5], '6 of Clubs': [6, "Clubs", 6],
        '7 of Clubs': [7, "Clubs", 7], '8 of Clubs': [8, "Clubs", 8], '9 of Clubs': [9, "Clubs", 9],
        '10 of Clubs': [10, "Clubs", 10], 'Jack of Clubs': ["Jack", "Clubs", 10],
        'Queen of Clubs': ["Queen", "Clubs", 10], 'King of Clubs': ["King", "Clubs", 10],

        'Ace of Diamonds': ["Ace", "Diamonds", 1], '2 of Diamonds': [2, "Diamonds", 2],
        '3 of Diamonds': [3, "Diamonds", 3], '4 of Diamonds': [4, "Diamonds", 4], '5 of Diamonds': [5, "Diamonds", 5],
        '6 of Diamonds': [8, "Diamonds", 8], '7 of Diamonds': [8, "Diamonds", 8], '8 of Diamonds': [8, "Diamonds", 8],
        '9 of Diamonds': [9, "Diamonds", 9], '10 of Diamonds': [10, "Diamonds", 10],
        'Jack of Diamonds': ["Jack", "Diamonds", 10], 'Queen of Diamonds': ["Queen", "Diamonds", 10],
        'King of Diamonds': ["King", "Diamonds", 10],

        'Ace of Hearts': ["Ace", "Hearts", 1], '2 of Hearts': [2, "Hearts", 2], '3 of Hearts': [3, "Hearts", 3],
        '4 of Hearts': [4, "Hearts", 4], '5 of Hearts': [5, "Hearts", 5], '6 of Hearts': [6, "Hearts", 6],
        '7 of Hearts': [7, "Hearts", 7], '8 of Hearts': [8, "Hearts", 8], '9 of Hearts': [9, "Hearts", 9],
        '10 of Hearts': [10, "Hearts", 10], 'Jack of Hearts': ["Jack", "Hearts", 10],
        'Queen of Hearts': ["Queen", "Hearts", 10], 'King of Hearts': ["King", "Hearts", 10],

        'Ace of Spades': ["Ace", "Spades", 1], '2 of Spades': [2, "Spades", 2], '3 of Spades': [3, "Spades", 3],
        '4 of Spades': [4, "Spades", 4], '5 of Spades': [5, "Spades", 5], '6 of Spades': [6, "Spades", 6],
        '7 of Spades': [7, "Spades", 7], '8 of Spades': [8, "Spades", 8], '9 of Spades': [9, "Spades", 9],
        '10 of Spades': [10, "Spades", 10], 'Jack of Spades': ["Jack", "Spades", 10],
        'Queen of Spades': ["Queen", "Spades", 10], 'King of Spades': ["King", "Spades", 10]}
dealerHand = [pop(deck), pop(deck)]
dealerShowCard = dealerHand[0]
yourHand = [pop(deck), pop(deck)]
yourPoints = yourHand[0] + yourHand[1]
print(yourHand)
dealerPoints = dealerHand[0] + dealerHand[1]
deckPosition = 4
print(keys)


# function to change the value of an ace to 1 or 11 as needed
def checkAce():
    global yourPoints
    global dealerPoints
    for card in range(len(yourHand)):
        if points(yourHand[card]) == 1 and yourPoints < 12:
            yourPoints += 10
    for card in range(len(dealerHand)):
        if points(dealerHand[card]) == 1 and dealerPoints < 12:
            dealerPoints += 10


# function to draw another card
def hit():
    global deckPosition
    global yourPoints
    global yourHand
    yourHand.append(keys[deckPosition])
    deckPosition += 1
    print("YOUR CARDS: ")
    i = 0
    while i < len(yourHand):
        print(yourHand[i])
        i += 1
    yourPoints += points(yourHand[deckPosition - 3])
    checkAce()
    print()


# function for dealer to play if you stand
def stand():
    global deckPosition
    global dealerPoints
    global dealerHand
    dealerHand.append(keys[deckPosition])
    deckPosition += 1
    print("DEALER'S CARDS: ")
    i = 0
    while i < len(dealerHand):
        print(dealerHand[i])
        i += 1
    dealerPoints += points(dealerHand[deckPosition - 3])
    checkAce()
    print()


# checks to see if you got a blackjack
def blackjack():
    if (yourHand[0][2] == 1) and (yourHand[1][2] == 10):
        return True
    elif (yourHand[0][2] == 10) and (yourHand[1][2] == 1):
        return True
    return False


# function to reshuffle the deck, get new cards, assign the new point values, and reset the deck position
def play():
    global deck
    global dealerHand
    global dealerShowCard
    global yourHand
    global yourPoints
    global dealerPoints
    global deckPosition
    random.shuffle(keys)
    dealerHand = keys[:2]
    dealerShowCard = keys[:1]
    yourHand = keys[2:4]
    yourPoints = points(yourHand[0]) + points(yourHand[1])
    dealerPoints = points(dealerHand[0]) + points(dealerHand[1])
    deckPosition = 4
