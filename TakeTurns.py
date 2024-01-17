import random


class Player:
    def __init__(self, name, money, position):
        self.name = name
        self.money = money
        self.position = position
        self.places_owned = []


class Property:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost


def roll_dice():
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    result = roll1 + roll2
    return result


def determine_starting_player(players):
    highest_roll = 0
    starting_player = None

    for player in players:
        roll = roll_dice()
        print("{} rolled: {}".format(player.name, roll))

        if roll > highest_roll:
            highest_roll = roll
            starting_player = player

    print("{} starts the game!".format(starting_player.name))
    return starting_player


def handle_turn(player):
    print("It's {}'s turn.".format(player.name))

    # Perform actions for the player's turn
    # ...


# Create player objects
player1 = Player("Player 1", 1500, 0)
player2 = Player("Player 2", 1500, 0)
player3 = Player("Player 3", 1500, 0)
player4 = Player("Player 4", 1500, 0)

No_of_Players = 0

# Store players in a list
players = [player1, player2, player3, player4]



def no_players():
    playernum = int(input("How many players are in the game? "))
    if playernum == 2:
        players.pop(3)
        players.pop(2)
    elif playernum == 3:
        players.pop(3)
        print(players)
    else:
        pass


no_players()

# Determine starting player
current_player = determine_starting_player(players)
i = 0
# Main game loop
while i < 10:

    handle_turn(current_player)

    # Move to the next player
    current_player_index = players.index(current_player)
    current_player = players[(current_player_index + 1) % len(players)]
    i += 1