import random

class Player:
    def __init__(self, name, position, money, roll_double=0):
        self.name = name
        self.position = position
        self.money = money
        self.owned_spaces = set()
        self.roll_double = roll_double

    def roll_dice(self):
        return random.randint(1, 6), random.randint(1, 6)


    def board_move(self):
        roll1,roll2 = self.roll_dice()
        print(f"{self.name} rolled {roll1} and {roll2}")
        current_position = self.position
        print("My current position is: ", current_position)
        new_position = current_position + roll1 + roll2
        print("The new position is: ", new_position)
        a = self.roll_double
        if roll1 == roll2:
            a += 1
            print(a)
            if a >= 3:
                print("jail")
            else:
                a = 0
        return a



    def board_position(self):
        self.position = self.board_move()
        return self.position
        #self.position = (self.position + self.roll_dice) % 40


    def doubles(self):
        roll1,roll2 = self.roll_dice()
        print(roll1)
        print(roll2 )
        if roll1 == roll2:
            print("Double!")
        elif roll1 != roll2:
            print("End")

# Creating an instance of the class
player1 = Player("Hat", 0, 2000,0)
player2 = Player("Car", 0, 2000,0)
player3 = Player("Battleship", 0, 2000,0)
player4 = Player("Thimble", 0, 2000,0)


player1.board_move()
b = player1.roll_double
print(b)
#print(player1.position)

