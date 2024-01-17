import random
player = 0
turn = 0
game = 0
double = 0

def dice():
    global dice_roll
    global dice_roll_2
    dice_roll = random.randint(1,6)
    dice_roll_2 = random.randint(1, 6)
    roll_result = dice_roll + dice_roll_2
    print("Dice 1 is: " + str(dice_roll))
    print("Dice 2 is: " + str(dice_roll_2))
    print("Roll is: " + str(roll_result))

    return dice_roll
    return dice_roll_2
    return roll_result

while game == 0:
    while player == 0:
        print("Player 1")
        dice()
        if dice_roll == dice_roll_2:
            print("Double")
            double += 1
            dice()
            if dice_roll == dice_roll_2:
                print("Double")
                double += 1
                dice()
                if double == 3:
                    print("Go to jail!")
                    double = 0
        else:
            double == 0
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
        dice()
        turn = int(input("End of your turn? Press 1: "))
        if turn == 1:
            break

    player = 0
    print("Player 2")
    game = int(input("End of the game? Press 2: "))
    if game == 2:
        break