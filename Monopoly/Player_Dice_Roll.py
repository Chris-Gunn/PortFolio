import random

# def starting_order():


def player_dice_roll(position, double):
    dice_roll_1 = random.randint(1, 6)
    dice_roll_2 = random.randint(1, 6)
    total_roll = dice_roll_1 + dice_roll_2

    if dice_roll_1 == dice_roll_2:
        double += 1
    if dice_roll_1 != dice_roll_2:
        double = 0
    position += total_roll

    return position, double, dice_roll_1, dice_roll_2


order = [1, 2, 3, 4]

player1 = {'position': 0, 'double': 0, 'dice_roll_1': 0, 'dice_roll_2': 0}
rolls = 5

for times in range(rolls):
    player1['position'], player1['double'], player1['dice_roll_1'], player1['dice_roll_2'] = \
        player_dice_roll(player1['position'], player1['double'])

    print("Dice 1: ", player1['dice_roll_1'])
    print("Dice 2: ", player1['dice_roll_2'])
    print("Player 1 Position:", player1['position'])
    print("Player 1 Doubles:", player1['double'])
print(player1)





