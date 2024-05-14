import random

# def starting_order():


def player_dice_roll(position, double):
    # dice_roll_1 = random.randint(1, 6)
    # dice_roll_2 = random.randint(1, 6)
    dice_roll_1 = 3
    dice_roll_2 = 3
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


player1['position'], player1['double'], player1['dice_roll_1'], player1['dice_roll_2'] = \
        player_dice_roll(player1['position'], player1['double'])

print(player1)
if player1['double'] == 1:
    player1['position'], player1['double'], player1['dice_roll_1'], player1['dice_roll_2'] = \
        player_dice_roll(player1['position'], player1['double'])
    print(player1)

    if player1['double'] == 2:
        player1['position'], player1['double'] = 30, 3
        print(player1)



