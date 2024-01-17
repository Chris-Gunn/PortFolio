import random

class Player:
    def __init__(self, name, position, money):
        self.name = name
        self.position = position
        self.money = money

    # def dice_roll(self):
    #     roll = random.randint(1, 6)
    #     roll2 = random.randint(1, 6)
    #     roll_result = roll + roll2
    def board_move(self):
        current_position = self.position
        print("My current position is: ", current_position)
        roll = random.randint(1, 6)
        print(roll)
        roll2 = random.randint(1, 6)
        print(roll2)
        roll_result = roll + roll2
        print("You have rolled a: " + str(roll_result))
        new_position = roll_result + self.position
        self.position = new_position
        print("The new position is: ", self.position)
        return roll, roll2

    def double(self, roll, roll2):
        dice_roll1 = board_move(roll)
        dice_roll2 = board_move(roll2)
        if dice_roll1 == dice_roll2:
            print("double")


    def money_change(self, new_money):
        print("My current balance is: ", self.money)
        self.money = new_money + self.money
        print("My new balance is: ", self.money)



# Creating an instance of the class
player1 = Player("Hat", 0, 2000)
player2 = Player("Car", 0, 2000)
player3 = Player("Battleship", 0, 2000)
player4 = Player("Thimble", 0, 2000)

# Calling the function and changing the value of var2
move = 0

# move = str(input("Would you like to roll the dice?\n"))
# if move == "yes":
#     if player1.board_move() == 4:
#         print("4")
#     else:
#         print("Not 4")



# player1.board_move()
player1.double(3, 4)