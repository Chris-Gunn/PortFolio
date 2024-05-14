import random

user_1 = 0

def diceStart():

    roll_result = random.randint(1,6)
    print("Roll is: " + str(roll_result))

    return roll_result

user_1 = diceStart()
print("user_1 has rolled: " + str(user_1))
user_2 = diceStart()
print("user_2 has rolled: " + str(user_2))

if user_1 > user_2:
    print("User 1 goes first")
elif user_1 == user_2:
    print("Roll again")
else:
    print("User 2 goes first")