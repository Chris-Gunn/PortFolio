import random
player = 0
turn = 0
game = 0

while game == 0:
    while player == 0:
        print(player)
        dice_roll = random.randint(1, 6)
        print(dice_roll)
        turn = int(input("End of your turn? Press 1:"))
        if turn == 1:
            break

    player = 1
    print(player)

    while player == 1:
        print(player)
        dice_roll = random.randint(1, 6)
        print(dice_roll)
        turn = int(input("End of your turn? Press 1:"))
        if turn == 1:
            break

    player = 0
    print(player)
    game = int(input("End of the game? Press 2: "))
    if game == 2:
        break