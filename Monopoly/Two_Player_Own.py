import random

class Player:
    def __init__(self, name,position=0):
        self.name = name
        self.position = position
        self.owned_spaces = set()

    def roll_dice(self):
        return random.randint(1, 6), random.randint(1, 6)

    def move(self, num_spaces):
        roll1, roll2 = self.roll_dice()
        print(f"")
        self.position = (self.position + num_spaces) % 40

    def check_if_owned(self, space):
        if space in self.owned_spaces:
            print(f"{self.name} already owns space {space}!")
        else:
            self.owned_spaces.add(space)
            print(f"{self.name} now owns space {space}!")

    def play_turn(self):
        print(f"{self.name}'s turn")
        roll1, roll2 = self.roll_dice()
        print(f"{self.name} rolled {roll1} and {roll2}")
        if roll1 == roll2:
            print("It's a double! Roll again.")
            self.play_turn()
        else:
            self.move(roll1 + roll2)
            print(f"{self.name} moved to space {self.position}")
            self.check_if_owned(self.position)

player1 = Player("Alice")
player2 = Player("Bob")

while True:
    player1.play_turn()
    player2.play_turn()
