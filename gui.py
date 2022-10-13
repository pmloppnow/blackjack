# imports needed modules
import time
from datetime import datetime
from decimal import Decimal
from decimal import ROUND_HALF_UP
import locale as lc
import objects as o
import db
import tkinter as tk
from tkinter import ttk


# function for hit button
def clickHit():
    o.yourHand.addCard(o.deck.deal())
    o.yourHand.checkForAce()
    yCardsText.set(o.yourHand)
    yPointsText.set(o.yourHand.value)
    if o.yourHand.value > 21:
        dCardsText.set(o.dealerHand)
        dPointsText.set(o.dealerHand.value)
        resultText.set("Bust. You lose.")
        moneyText.set(float(moneyText.get()) - float(betText.get()))
    elif o.yourHand.value == 21 and o.dealerHand.value == 21:
        dCardsText.set(o.dealerHand)
        dPointsText.set(o.dealerHand.value)
        resultText.set("Push. You tied.")
    elif o.yourHand.value == 21:
        dCardsText.set(o.dealerHand)
        dPointsText.set(o.dealerHand.value)
        resultText.set("You have more points. You win!")
        moneyText.set(float(moneyText.get()) + float(betText.get()))


# function for stand button
def clickStand():
    if o.dealerHand.value < 17:
        o.dealerHand.addCard(o.deck.deal())
        dCardsText.set(o.dealerHand)
        o.dealerHand.checkForAce()
        dPointsText.set(o.dealerHand.value)
        clickStand()
    else:
        if o.yourHand.value == o.dealerHand.value:
            dCardsText.set(o.dealerHand)
            dPointsText.set(o.dealerHand.value)
            resultText.set("Push. You tied.")
        elif o.dealerHand.value > 21:
            dCardsText.set(o.dealerHand)
            dPointsText.set(o.dealerHand.value)
            resultText.set("The dealer busted. You win!")
            moneyText.set(float(moneyText.get()) + float(betText.get()))
        elif o.yourHand.value > o.dealerHand.value:
            dCardsText.set(o.dealerHand)
            dPointsText.set(o.dealerHand.value)
            resultText.set("You have more points than the dealer. You win!")
            moneyText.set(float(moneyText.get()) + float(betText.get()))
        elif o.yourHand.value < o.dealerHand.value:
            dCardsText.set(o.dealerHand)
            dPointsText.set(o.dealerHand.value)
            resultText.set("You have less points than the dealer. You lose.")
            moneyText.set(float(moneyText.get()) - float(betText.get()))


# function for play button
def clickPlay():
    try:
        if betText.get() is not None and betText.get() != "" and float(betText.get()) <= float(moneyText.get()):
            if Decimal(betText.get()).quantize(Decimal("1.00"), ROUND_HALF_UP) > 0:
                betText.set(Decimal(betText.get()).quantize(Decimal("1.00"), ROUND_HALF_UP))
                resultText.set("")
                o.deck.shuffle()
                o.yourHand = o.Hand()
                o.yourHand.addCard(o.deck.deal())
                o.yourHand.addCard(o.deck.deal())
                o.dealerHand = o.Hand()
                o.dealerHand.addCard(o.deck.deal())
                o.dealerHand.addCard(o.deck.deal())
                o.dealerShowCard = o.dealerHand.cards[0]
                o.yourHand.checkForAce()
                o.dealerHand.checkForAce()
                dCardsText.set(o.dealerShowCard)
                dPointsText.set(o.dealerShowCard.value)
                yCardsText.set(o.yourHand)
                yPointsText.set(o.yourHand.value)
                if o.yourHand.value == 21 and o.dealerHand.value == 21:
                    dCardsText.set(o.dealerHand)
                    dPointsText.set(o.dealerHand.value)
                    resultText.set("You both got blackjacks! You tie.")
                elif o.yourHand.value == 21:
                    dCardsText.set(o.dealerHand)
                    dPointsText.set(o.dealerHand.value)
                    resultText.set("Blackjack! You win! Payout is 3:2.")
                    moneyText.set(float(moneyText.get()) + (float(betText.get()) * 1.5))
            else:
                resultText.set("Place a valid bet to play.")
        elif float(betText.get()) > float(moneyText.get()):
            resultText.set("Bet can't exceed money.")
        else:
            resultText.set("Place a valid bet to play.")
    except ValueError:
        resultText.set("Place a valid bet to play.")


# function for exit button
def clickExit():
    stopTime = datetime.now().strftime("%G-%m-%d %H:%M:%S.%f")
    s = (startTime, session.stopMoney, stopTime, moneyText.get())
    db.addSessions(s)
    root.destroy()
    db.close()


# connects to database
db.connect()
db.createSession()
row = db.getLastSession()
session = o.Session(row)

# sets start time and locale
startTime = datetime.now().strftime("%G-%m-%d %H:%M:%S.%f")
result = lc.setlocale(lc.LC_ALL, "")
if result == "C":
    lc.setlocale(lc.LC_ALL, "en_US")

# creates GUI window
root = tk.Tk()
root.title("Blackjack")
root.geometry("300x350")
frame = ttk.Frame(root, padding="15 15 15 15")
frame.grid()

# creates GUI label and text box for money
ttk.Label(frame, text="Money: ").grid(column=0, row=0)
moneyText = tk.StringVar()
moneyText.set(session.stopMoney)
moneyEntry = ttk.Entry(frame, width=25, textvariable=moneyText, state="readonly").grid(column=1, row=0)

# creates GUI label and text box for bet
ttk.Label(frame, text="Bet: ").grid(column=0, row=1)
betText = tk.StringVar()
betEntry = ttk.Entry(frame, width=25, textvariable=betText).grid(column=1, row=1)

# creates GUI label for dealer
ttk.Label(frame, text="DEALER").grid(column=0, row=2)

# creates GUI label and text box for dealer's cards
ttk.Label(frame, text="Cards: ").grid(column=0, row=3)
dCardsText = tk.StringVar()
dCardsEntry = ttk.Entry(frame, width=25, textvariable=dCardsText, state="readonly").grid(column=1, row=3)

# creates GUI label and text box for dealer's points
ttk.Label(frame, text="Points: ").grid(column=0, row=4)
dPointsText = tk.StringVar()
dPointsEntry = ttk.Entry(frame, width=25, textvariable=dPointsText, state="readonly").grid(column=1, row=4)

# creates GUI label for you
ttk.Label(frame, text="YOU").grid(column=0, row=5)

# creates GUI label and text box for your cards
ttk.Label(frame, text="Cards: ").grid(column=0, row=6)
yCardsText = tk.StringVar()
yCardsEntry = ttk.Entry(frame, width=25, textvariable=yCardsText, state="readonly").grid(column=1, row=6)

# creates GUI label and text box for your points
ttk.Label(frame, text="Points: ").grid(column=0, row=7)
yPointsText = tk.StringVar()
yPointsEntry = ttk.Entry(frame, width=25, textvariable=yPointsText, state="readonly").grid(column=1, row=7)

# creates GUI buttons to hit and stand
hit = ttk.Button(frame, text="Hit", command=clickHit)
hit.grid(column=0, row=8)
stand = ttk.Button(frame, text="Stand", command=clickStand)
stand.grid(column=1, row=8)

# creates GUI label and text box for result
ttk.Label(frame, text="RESULT: ").grid(column=0, row=9)
resultText = tk.StringVar()
resultEntry = ttk.Entry(frame, width=25, textvariable=resultText, state="readonly").grid(column=1, row=9)

# creates GUI buttons to play and exit
playButton = ttk.Button(frame, text="Play", command=clickPlay)
playButton.grid(column=0, row=10)
exit = ttk.Button(frame, text="Exit", command=clickExit)
exit.grid(column=1, row=10)

# pads elements to space them out
for child in frame.winfo_children():
    child.grid_configure(padx=3, pady=3)

# opens GUI window
root.mainloop()
