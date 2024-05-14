import random

# Define the board
board = {
'Go': 0,
'Mediterranean Ave.': 1,
'Community Chest': 2,
'Baltic Ave.': 3,
'Income Tax': 4,
'Reading Railroad': 5,
'Oriental Ave.': 6,
'Chance': 7,
'Vermont Ave.': 8,
'Connecticut Ave.': 9,
'Jail': 10,
'St. Charles Place': 11,
'Electric Company': 12,
'States Ave.': 13,
'Virginia Ave.': 14,
'Pennsylvania Railroad': 15,
'St. James Place': 16,
'Community Chest': 17,
'Tennessee Ave.': 18,
'New York Ave.': 19,
'Free Parking': 20,
'Kentucky Ave.': 21,
'Chance': 22,
'Indiana Ave.': 23,
'Illinois Ave.': 24,
'B. & O. Railroad': 25,
'Atlantic Ave.': 26,
'Ventnor Ave.': 27,
'Water Works': 28,
'Marvin Gardens': 29,
'Go to Jail': 30,
'Pacific Ave.': 31,
'North Carolina Ave.': 32,
'Community Chest': 33,
'Pennsylvania Ave.': 34,
'Short Line': 35,
'Chance': 36,
'Park Place': 37,
'Luxury Tax': 38,
'Boardwalk': 39
}


# Define the players
class Player:
def __init__(self, name):
self.name = name
self.position = 0
self.money = 1500


# Define the game
class Monopoly:
def __init__(self, players):
self.players = players
self.current_player_index = 0
self.num_players = len(players)

def roll_dice(self):
return random.randint(1, 6), random.randint(1, 6)

def move_player(self, player, num_spaces):
player.position = (player.position + num_spaces) % 40

def play_round(self):
# Get the current player
current_player = self.players[self.current_player_index]
print(f"It is {current_player.name}'s turn.")

# Roll the dice
dice_roll = self.roll_dice()
print(f"{current_player.name} rolls {dice_roll[0]} and {dice_roll[1]}.")

# Move the player
num_spaces = sum(dice_roll)
self.move_player(current_player, num_spaces)
print(
f"{current_player.name} moves {num_spaces} spaces and lands on {list(board.keys())[list(board.values()).index(current_player.position)]}.")

# Handle landing on spaces
space = list(board.keys())[list(board.values()).index(current_player.position)]
if space in ['Community Chest', 'Chance']:
card = self.draw_card(space)
print(f"{current_player.name} draws a {card}.")
self.handle_card(card, current_player)
elif space == 'Income Tax':
print(f"{current_player.name} pays $200 in income tax.")
current_player.money -= 200
elif space == 'Luxury Tax':
print(f"{current_player.name}")