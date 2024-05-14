# import random
#
# def dice():
#
#     roll_result = random.randint(1,6)
#     print("Roll is: " + str(roll_result))
#
#     return roll_result
#
# def dice2():
#
#     roll_result_2 = random.randint(1,6)
#     print("Roll is: " + str(roll_result_2))
#
#     return roll_result_2
#
#
# if dice() == dice2():
#     print("Win")
#     print(f"{dice} and {dice2}")
# else:
#     print(f"{dice} and {dice2}")


import random

roll_result = random.randint(1,6)
print("Roll is: " + str(roll_result))
roll_result_2 = random.randint(1,6)
print("Roll is: " + str(roll_result_2))

if roll_result == roll_result_2:
    print("Win")
    print(f"{roll_result} and {roll_result_2}")
else:
    print(f"{roll_result} and {roll_result_2}")
