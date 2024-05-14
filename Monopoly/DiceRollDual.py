from operator import add
import random

dice = 1
dice_1 = 1
dice_2 = 1

def dice_roll(dice):
    def dice_roll_1(dice_1):

        """"Return a list of integers with length `num_dice`.

        Each integer in the returned list is a random number between
        1 and 6, inclusive.
        """
        roll_result_1 = 0
        for _ in range(dice_1):
            roll_result_1 = random.randint(1, 6)
            print("Roll 1 is: " + str(roll_result_1))

        return roll_result_1

    def dice_roll_2(dice_2):

        """"Return a list of integers with length `num_dice`.

        Each integer in the returned list is a random number between
        1 and 6, inclusive.
        """
        roll_result_2 = 0
        for _ in range(dice_2):
            roll_result_2 = random.randint(1, 6)
            print("Roll 2 is: " + str(roll_result_2))

        return roll_result_2


print


results = dice_roll(dice)


print(results)