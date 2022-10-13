import random

# creates the deck of cards, shuffles them, deals them, and gives points
deckList = []
ranks = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]
suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
points = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
for r in ranks:
    for s in suits:
        if r == "Jack" or r == "Queen" or r == "King":
            deckList.append([r, s, points[9]])
        elif r == "Ace":
            deckList.append([r, s, points[0]])
        else:
            deckList.append([r, s, points[r - 1]])
random.shuffle(deckList)
dealerHand = deckList[:2]
dealerShowCard = deckList[:1]
yourHand = deckList[2:4]
yourPoints = yourHand[0][2] + yourHand[1][2]
dealerPoints = dealerHand[0][2] + dealerHand[1][2]


# function to change the value of an ace to 1 if points are over 21
def checkAce():
    j = 0
    for cards in yourHand:
        if yourHand[j] == "Ace" and yourPoints > 21:
            yourPoints = yourPoints - 10
    for cards in dealerHand:
        if dealerHand[j] == "Ace" and dealerPoints > 21:
            dealerPoints = dealerPoints - 10


# function to hit if the player wants to draw another card
def hit(hitNum):
    k = 4
    yourHand.append(deckList[k + hitNum])
    k += 1
    hitNum += 1
    print("YOUR CARDS: ")
    m = 0
    while m < len(yourHand):
        print(yourHand[m][0], "of", yourHand[m][1])
        m += 1
    print()
    checkAce()


# function for dealer to play if player stands
def stand(hitNum):
    if dealerPoints < yourPoints or dealerPoints < 17:
        k = 4
        dealerHand.append(deckList[k + hitNum])
        k += 1
        hitNum += 1
        print("DEALER'S CARDS: ")
        m = 0
        while m < len(dealerHand):
            print(dealerHand[m][0], "of", dealerHand[m][1])
            m += 1
        print()
        checkAce()
