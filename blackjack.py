import random
import cards
import db

play = "y"
# while loop that allows user to play again
while play == "y":
    hitNum = 0
    betMin = 5
    betMax = 1000

    print("BLACKJACK!")
    print("Blackjack payout is 3:2")
    print()
    print("Money: ", db.money)
    if db.money < 5:
        moreMoney = input("You have less than $5, want to buy more chips? (y/n): ")
        if moreMoney == "y":
            db.money += 5
            print("Money: ", db.money)
            db.write()
        else:
            print("You don't have enough money to play!")
            break
    try:
        bet = input("Bet amount: ")
        bet = round(float(bet), 2)
    except ValueError as e:
        bet = input("Please enter a float or int. Bet amount: ")
        bet = round(float(bet), 2)
    validBet = False
    while not validBet:
        if float(bet) < betMin:
            bet = input("Bet must be 5 or more. Bet amount: ")
            bet = round(float(bet), 2)
        elif float(bet) > betMax:
            bet = input("Bet must be 1000 or less. Bet amount: ")
            bet = round(float(bet), 2)
        elif float(bet) > db.money:
            bet = input("You don't have that much money. Bet amount: ")
            bet = round(float(bet), 2)
        else:
            validBet = True
    print()
    print("DEALER'S SHOW CARD: ")
    print(cards.dealerShowCard[0][0], "of", cards.dealerShowCard[0][1])
    print()
    print("YOUR CARDS: ")
    i = 0
    while i < len(cards.yourHand):
        print(cards.yourHand[i][0], "of", cards.yourHand[i][1])
        i += 1
    print()

    cards.checkAce()

    while cards.yourPoints < 21:
        selection = input("Hit or stand? (hit/stand): ")
        print()
        if selection == "hit":
            cards.hit(hitNum)
            cards.yourPoints += cards.yourHand[2 + hitNum][2]
        elif selection == "stand":
            cards.stand(hitNum)
            cards.dealerPoints += cards.dealerHand[2 + hitNum][2]
            break
        else:
            print("Hit or stand (hit/stand): ")

    print("YOUR POINTS: ", cards.yourPoints)
    print("DEALER'S POINTS: ", cards.dealerPoints)
    print()

    if cards.yourPoints > 21:
        print("Bust. You lose.")
        db.money = db.money - float(bet)
        print("Money: ", db.money)
        db.write()
    elif cards.dealerPoints > 21:
        print("You win!")
        db.money = (float(bet) * 1.5) + db.money - float(bet)
        print("Money: ", db.money)
        db.write()
    elif 22 > cards.yourPoints > cards.dealerPoints:
        print("You win!")
        db.money = (float(bet) * 1.5) + db.money - float(bet)
        print("Money: ", db.money)
        db.write()
    elif 22 > cards.dealerPoints > cards.yourPoints:
        print("Sorry. You lose.")
        db.money = db.money - float(bet)
        print("Money: ", db.money)
        db.write()
    elif cards.yourPoints == cards.dealerPoints:
        print("You Tied.")
        print("Money: ", db.money)
        db.write()
    print()
    play = input("Play again? (y/n): ")
    print()
    if play == "y":
        random.shuffle(cards.deckList)
    elif play == "n":
        print("Come back soon!")
        print("Bye!")
        break
    else:
        print("Play again? (y/n): ")
