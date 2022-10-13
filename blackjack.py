# imports needed modules
import time
from datetime import datetime
from decimal import Decimal
from decimal import ROUND_HALF_UP
import locale as lc
import cards
import db

# sets start time and locale
startTime = time.strftime("%H:%M:%S")
startTime = datetime.strptime(startTime, "%H:%M:%S")
lc.setlocale(lc.LC_ALL, "us")

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
            db.money += 5.00
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
    print(cards.dealerShowCard[0])
    print()
    print("YOUR CARDS: ")
    i = 0
    while i < len(cards.yourHand):
        print(cards.yourHand[i])
        i += 1
    print()

    # if a player has an ace, gives appropriate value
    cards.checkAce()

    # lets you hit/stand until the round is over
    selection = ""
    while int(cards.yourPoints) < 21 and int(cards.dealerPoints) < 21 and selection != "stand":
        selection = input("Hit or stand? (hit/stand): ")
        print()
        if selection == "hit":
            cards.hit()
        elif selection == "stand":
            if cards.dealerPoints < 17:
                while cards.dealerPoints < 17:
                    cards.stand()
                break
            else:
                print("DEALER'S CARDS: ")
                i = 0
                while i < len(cards.dealerHand):
                    print(cards.dealerHand[i])
                    i += 1
                print()
                break

    # determines if you got a blackjack
    blackjackBool = cards.blackjack()

    # prints point values
    print("YOUR POINTS: ", cards.yourPoints)
    print("DEALER'S POINTS: ", cards.dealerPoints)
    print()

    # determines who won and updates your money
    if cards.yourPoints == cards.dealerPoints:
        print("Push. You tied.")
        print("Money: ", lc.currency(db.money, grouping=True))
        db.write()
    elif blackjackBool:
        print("Blackjack! You win!")
        db.money = Decimal(db.money) + (bet * Decimal(1.50))
        print("Money: ", lc.currency(db.money, grouping=True))
        db.write()
    elif cards.yourPoints > 21:
        print("Bust. You lose.")
        db.money = Decimal(db.money) - bet
        print("Money: ", lc.currency(db.money, grouping=True))
        db.write()
    elif cards.dealerPoints > 21:
        print("The dealer busted. You win!")
        db.money = Decimal(db.money) + bet
        print("Money: ", lc.currency(db.money, grouping=True))
        db.write()
    elif 22 > cards.yourPoints > cards.dealerPoints:
        print("You have more points than the dealer. You win!")
        db.money = Decimal(db.money) + bet
        print("Money: ", lc.currency(db.money, grouping=True))
        db.write()
    elif 22 > cards.dealerPoints > cards.yourPoints:
        print("The Dealer has more points. You lose.")
        db.money = Decimal(db.money) - bet
        print("Money: ", lc.currency(db.money, grouping=True))
        db.write()
    print()

    # asks if you want to play another round and prints the ending statements if not
    play = input("Play again? (y/n): ")
    print()
    if play == "y":
        cards.play()
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
