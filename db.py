# opens the money.txt file, reads the value, and converts it to a float with 2 decimal places
try:
    file = open("money.txt", "r")
except FileNotFoundError as e:
    file = input("File not found. Enter file name: ")
    file = open(file, "r")
moneyStr = file.read()
money = float(moneyStr)
format(money, ".2f")

# writes the new value of money to money.txt
def write():
    wr = open("money.txt", "w")
    format(money, ".2f")
    wr.write(str(money))
