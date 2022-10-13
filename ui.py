# imports needed modules
import time
from datetime import datetime
from decimal import Decimal
from decimal import ROUND_HALF_UP
import locale as lc
import objects
import db

# sets start time and locale
startTime = time.strftime("%H:%M:%S")
startTime = datetime.strptime(startTime, "%H:%M:%S")
result = lc.setlocale(lc.LC_ALL, "")
if result == "C":
    lc.setlocale(lc.LC_ALL, "en_US")

# prints starting statements
print("BLACKJACK!")
print("Blackjack payout is 3:2")
print("Start Time: ", startTime.strftime("%r"))
print()

# while loop that allows you to play again
play = "y"
while play == "y":

    # places bet, offers money if needed, and validates the bet amount
    betMin = 5
    betMax = 1000
    print("Money: ", lc.currency(db.money, grouping=True))
    if db.money < 5:
        moreMoney = input("You have less than $5, want to buy more chips? (y/n): ")
        if moreMoney == "y":
            db.money += Decimal(5.00)
            print("Money: ", lc.currency(db.money, grouping=True))
            db.write()
        else:
            print("You don't have enough money to play!")
            break
    try:
        bet = input("Bet amount: ")
        bet = Decimal(bet).quantize(Decimal("1.00"), ROUND_HALF_UP)
    except ValueError as e:
        bet = input("Please enter a float or int. Bet amount: ")
        bet = Decimal(bet).quantize(Decimal("1.00"), ROUND_HALF_UP)
    validBet = False
    while not validBet:
        if float(bet) < betMin:
            bet = input("Bet must be 5 or more. Bet amount: ")
            bet = Decimal(bet).quantize(Decimal("1.00"), ROUND_HALF_UP)
        elif float(bet) > betMax:
            bet = input("Bet must be 1000 or less. Bet amount: ")
            bet = Decimal(bet).quantize(Decimal("1.00"), ROUND_HALF_UP)
        elif float(bet) > db.money:
            bet = input("You don't have that much money. Bet amount: ")
            bet = Decimal(bet).quantize(Decimal("1.00"), ROUND_HALF_UP)
        else:
            validBet = True
    print()

    # prints dealer's show card and your cards
    print("DEALER'S SHOW CARD: ")
    print(objects.dealerShowCard)
    print()
    print("YOUR CARDS: ")
    i = 0
    while i < len(objects.yourHand.cards):
        print(objects.yourHand.cards[i])
        i += 1
    print()

    # if a player has an ace, gives appropriate value
    objects.Hand.checkForAce(objects.yourHand)
    objects.Hand.checkForAce(objects.dealerHand)

    # lets you hit/stand until the round is over
    selection = ""
    while objects.yourHand.value < 21 and objects.dealerHand.value < 21 and selection != "stand":
        selection = input("Hit or stand? (hit/stand): ")
        print()
        if selection == "hit":
            objects.hit(objects.deck, objects.yourHand)
        elif selection == "stand":
            if objects.dealerHand.value < 17:
                while objects.dealerHand.value < 17:
                    objects.stand()
                break
            else:
                print("DEALER'S CARDS: ")
                i = 0
                while i < len(objects.dealerHand.cards):
                    print(objects.dealerHand.cards[i])
                    i += 1
                print()
                break

    # determines if you got a blackjack
    blackjackBool = objects.blackjack()

    # prints point values
    print("YOUR POINTS: ", objects.yourHand.value)
    print("DEALER'S POINTS: ", objects.dealerHand.value)
    print()

    # determines who won and updates your money
    if objects.yourHand.value == objects.dealerHand.value:
        print("Push. You tied.")
        print("Money: ", lc.currency(db.money, grouping=True))
        db.write()
    elif blackjackBool:
        print("Blackjack! You win!")
        db.money = Decimal(db.money) + (bet * Decimal(1.50))
        print("Money: ", lc.currency(db.money, grouping=True))
        db.write()
    elif objects.yourHand.value > 21:
        print("Bust. You lose.")
        db.money = Decimal(db.money) - bet
        print("Money: ", lc.currency(db.money, grouping=True))
        db.write()
    elif objects.dealerHand.value > 21:
        print("The dealer busted. You win!")
        db.money = Decimal(db.money) + bet
        print("Money: ", lc.currency(db.money, grouping=True))
        db.write()
    elif 22 > objects.yourHand.value > objects.dealerHand.value:
        print("You have more points than the dealer. You win!")
        db.money = Decimal(db.money) + bet
        print("Money: ", lc.currency(db.money, grouping=True))
        db.write()
    elif 22 > objects.dealerHand.value > objects.yourHand.value:
        print("The Dealer has more points. You lose.")
        db.money = Decimal(db.money) - bet
        print("Money: ", lc.currency(db.money, grouping=True))
        db.write()
    print()

    # asks if you want to play another round and prints the ending statements if not
    play = input("Play again? (y/n): ")
    print()
    if play == "y":
        objects.play()
    elif play == "n":
        stopTime = time.strftime("%H:%M:%S")
        stopTime = datetime.strptime(stopTime, "%H:%M:%S")
        elapsedTime = stopTime - startTime
        print("Stop time: ", stopTime.strftime("%r"))
        print("Elapsed time: ", elapsedTime)
        print("Come back soon!")
        print("Bye!")
        break
    else:
        print("Play again? (y/n): ")
