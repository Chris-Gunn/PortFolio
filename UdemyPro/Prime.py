pos = 1
money1 = 1000
money2 = 1000
money3 = 1000
money4 = 1000


while pos == 1:
    buy = input("Would you like to buy the property?\n")
    if buy == "yes":
        money1 = money1 - 100
        print(money1)
    elif buy == "no":
        print(money1)
    turn = input("Is it the end of your turn?\n")
    if turn == "yes":
        print("End of player 1's turn")
        pos = 2
    elif buy == "no":
        pass

while pos == 2:
    buy = input("Would you like to buy the property?\n")
    if buy == "yes":
        money2 = money2 - 100
        print(money2)
    elif buy == "no":
        print(money2)
    turn = input("Is it the end of your turn?\n")
    if turn == "yes":
        print("End of player 2's turn")
        pos = 3
    elif buy == "no":
        pass

while pos == 3:
    buy = input("Would you like to buy the property?\n")
    if buy == "yes":
        money3 = money3 - 100
        print(money3)
    elif buy == "no":
        print(money3)
    turn = input("Is it the end of your turn?\n")
    if turn == "yes":
        print("End of player 3's turn")
        pos = 4
    elif buy == "no":
        pass

while pos == 4:
    buy = input("Would you like to buy the property?\n")
    if buy == "yes":
        money4 = money4 - 100
        print(money4)
    elif buy == "no":
        print(money4)
    turn = input("Is it the end of your turn?\n")
    if turn == "yes":
        print("End of player 4's turn")
        pos = 1
    elif buy == "no":
        pass