import random
player = 0
turn = 0
game = 0

while game == 0:
    while player == 0:
        print("Player 1")
        dice_roll = random.randint(1, 6)
        print(dice_roll)
        dice_roll_2 = random.randint(1, 6)
        print(dice_roll_2)
        dice = dice_roll + dice_roll_2
        print("You have rolled a " + str(dice))
        turn = int(input("End of your turn? Press 1: "))
        if turn == 1:
            break

    player = 1
    print("Player 1")
    game = int(input("End of the game? Press 2: "))
    if game == 2:
        break

    while player == 1:
        print("Player 2")
        dice_roll = random.randint(1, 6)
        print(dice_roll)
        dice_roll_2 = random.randint(1, 6)
        print(dice_roll_2)
        dice = dice_roll + dice_roll_2
        print("You have rolled a " + str(dice))
        turn = int(input("End of your turn? Press 1: "))
        if turn == 1:
            break

    player = 0
    print("Player 2")
    game = int(input("End of the game? Press 2: "))
    if game == 2:
        break