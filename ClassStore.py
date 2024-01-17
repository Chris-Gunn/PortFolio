import random

class Player:
    def __init__(self, name, position, money):
        self.name = name
        self.position = position
        self.money = money

    def board_move(self, new_position):
        print("My current position is: ", self.position)
        self.position = new_position
        roll = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        roll_result = roll + roll2
        print(roll_result)
        new_position = roll_result
        self.position = new_position
        print("The new position is: ", self.position)

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
player1.board_move(5)
player2.money_change(-1000)

print(player1.position)
print(player2.money)
print(player3.position)
print(player4.position)