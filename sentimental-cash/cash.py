# TODO
from cs50 import get_float


def main():
    while True:
        try:
            change = float(get_float("Changed owed: "))
        except ValueError:
            print("Invalid input!")
        else:
            if change > 0:
                change_owe(change)
                break
            else:
                print("Invalid input!", change)


def change_owe(value):
    coins = 0
    while value != 0:
        if value >= 0.25:
            coins += int(value / 0.25)
            value = round(value % 0.25, 2)
        elif 0.1 <= value < 0.25:
            coins += int(value / 0.1)
            value = round(value % 0.1, 2)
        elif 0.05 <= value < 0.1:
            coins += int(value / 0.05)
            value = round(value % 0.05, 2)
        elif 0.01 <= value < 0.05:
            coins += int(value / 0.01)
            value = round(value % 0.01, 2)

    print(coins)


main()
