# imports needed modules
from decimal import Decimal
from decimal import ROUND_HALF_UP

# opens the money.txt file, reads the value, and converts it to a decimal
try:
    file = open("money.txt", "r")
except FileNotFoundError as e:
    file = input("File not found. Enter file name: ")
    file = open(file, "r")
moneyStr = file.read()
money = Decimal(moneyStr).quantize(Decimal("1.00"), ROUND_HALF_UP)


# writes the new value of money to money.txt
def write():
    wr = open("money.txt", "w")
    wr.write(str(money))
