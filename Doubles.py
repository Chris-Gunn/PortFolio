import random
player = 0
turn = 0
game = 0
double = 0
num = 0
num2 = 0

def dice():
    dice_roll = random.randint(1,6)
    dice_roll_2 = random.randint(1, 6)
    roll_result = dice_roll + dice_roll_2

    return dice_roll, dice_roll_2, roll_result

result = dice()
position = 0

print("Dice 1 is: ", result[0])
print("Dice 2 is: ", result[1])
print("Roll is: ", result[2])

if result[0] == result[1]:
    print("Double!")
else:
    pass

print(position)

position = position + result[2]

print(position)


