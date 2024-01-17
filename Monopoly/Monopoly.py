import random


class Player:
#    def __init__(self,name,money,double,in_jail):
    def __init__(self, name, money, position, jail, jail_free, house, hotel):
        self.name = name
        self.money = money
        self.position = position
        self.places_owned = []
        self.jail = jail
        self.jail_free = jail_free
        self.house = house
        self.hotel = hotel


class Property:
    def __init__(self, name, cost, rent, monopoly, one, two, three, four, hotel, mortgage, houses):
        self.name = name
        self.cost = cost
        self.rent = rent
        self.monopoly = monopoly
        self.one = one
        self.two = two
        self.three = three
        self.four = four
        self.hotel = hotel
        self.mortgage = mortgage
        self.houses = houses

    def is_owned(self):
        return self.owner is not None


class Owned:
    def __init__(self,bought,monopoly,one,two,three,four,hotel):
        self.bought = bought
        self.monopoly = monopoly
        self.one = one
        self.two = two
        self.three = three
        self.four = four
        self.hotel = hotel


class Stations:
    def __init__(self, name, cost, rent, two, three, four, mortgage):
        self.name = name
        self.cost = cost
        self.rent = rent
        self.two = two
        self.three = three
        self.four = four
        self.mortgage = mortgage


class StationsOwned:
    def __init__(self, bought, two, three, four):
        self.bought = bought
        self.two = two
        self.three = three
        self.four = four

class Monopoly:
    def __init__(self, name, monopoly):
        self.name = name
        self.monopoly = monopoly



Brown = Monopoly("Brown", 0),
Light_Blue = Monopoly("Light Blue", 0),
Purple = Monopoly("Purple", 0),
Orange = Monopoly("Orange", 0)
Red = Monopoly("Red", 0),
Yellow = Monopoly("Yellow", 0),
Green = Monopoly("Green", 0),
Dark_Blue = Monopoly("Dark Blue", 0)






board = [
    Property("Old Kent Road", 50, 2, 4, 10, 30, 90, 160, 250, 50, 50),
    Property("Whitechapel Road", 60, 4, 8, 20, 60, 180, 320, 450, 50, 50),
    Property("The Angel, Islington", 100, 6, 12, 30, 90, 270, 400, 550, 50, 50),
    Property("Euston Road", 100, 6, 12, 30, 90, 270, 400, 550, 50, 50),
    Property("Pentonville Road", 120, 8, 16, 40, 100, 300, 450, 600, 50, 50),
    Property("Pall Mall", 140, 10, 20, 50, 150, 450, 625, 750, 100, 100),
    Property("Whitehall", 140, 10, 20, 50, 150, 450, 625, 750, 100, 100),
    Property("Northumberland Avenue", 160, 12, 24, 60, 180, 500, 700, 900, 100, 100),
    Property("Bow Street", 180, 14, 28, 70, 200, 550, 750, 950, 100, 100),
    Property("Marlborough Street", 180, 14, 28, 70, 200, 550, 750, 950, 100, 100),
    Property("Vine Street", 200, 16, 32, 80, 220, 600, 800, 1000, 100, 100),
    Property("Strand", 220, 18, 36, 90, 250, 700, 875, 1050, 150, 150),
    Property("Fleet Street", 220, 18, 36, 90, 250, 700, 875, 1050, 150, 150),
    Property("Trafalgar Square", 240, 20, 40, 100, 300, 750, 925, 1100, 150, 150),
    Property("Leicester Square", 260, 22, 44, 110, 330, 800, 975, 1150, 150, 150),
    Property("Coventry Street", 260, 22, 44, 110, 330, 800, 975, 1150, 150, 150),
    Property("Piccadilly", 280, 24, 48, 120, 360, 850, 1025, 1200, 150, 150),
    Property("Regent Street", 300, 26, 52, 130, 390, 900, 1100, 1275, 200, 200),
    Property("Oxford Street", 300, 26, 52, 130, 390, 900, 1100, 1275, 200, 200),
    Property("Bond Street", 320, 28, 56, 150, 450, 1000, 1200, 1400, 200, 200),
    Property("Park Lane", 350, 35, 70, 175, 500, 1100, 1300, 1500, 200, 200),
    Property("Mayfair", 400, 50, 100, 200, 600, 1400, 1700, 2000, 200, 200),
]

platform = [
    Stations("King's Cross Station", 200, 25, 50, 100, 200, 100),
    Stations("Marylebone Station", 200, 25, 50, 100, 200, 100),
    Stations("Fenchurch St. Station", 200, 25, 50, 100, 200, 100),
    Stations("Liverpool St. Station", 200, 25, 50, 100, 200, 100)
]

# change OKR etc. to p1, p2 etc. then call them p[number]
OKR = Owned(False, False, 0, 0, 0, 0, 0)
WC = Owned(False, False, 0, 0, 0, 0, 0)
TAI = Owned(False, False, 0, 0, 0, 0, 0)
ER = Owned(False, False, 0, 0, 0, 0, 0)
PR = Owned(False, False, 0, 0, 0, 0, 0)
PM = Owned(False, False, 0, 0, 0, 0, 0)
WH = Owned(False, False, 0, 0, 0, 0, 0)
NA = Owned(False, False, 0, 0, 0, 0, 0)
BoS = Owned(False, False, 0, 0, 0, 0, 0)
MS = Owned(False, False, 0, 0, 0, 0, 0)
VS = Owned(False, False, 0, 0, 0, 0, 0)
S = Owned(False, False, 0, 0, 0, 0, 0)
FS = Owned(False, False, 0, 0, 0, 0, 0)
TS = Owned(False, False, 0, 0, 0, 0, 0)
LS = Owned(False, False, 0, 0, 0, 0, 0)
CS = Owned(False, False, 0, 0, 0, 0, 0)
P = Owned(False, False, 0, 0, 0, 0, 0)
RS = Owned(False, False, 0, 0, 0, 0, 0)
OS = Owned(False, False, 0, 0, 0, 0, 0)
BdS = Owned(False, False, 0, 0, 0, 0, 0)
PL = Owned(False, False, 0, 0, 0, 0, 0)
MF = Owned(False, False, 0, 0, 0, 0, 0)

KCS = StationsOwned(False, 0, 0, 0)
MLB = StationsOwned(False, 0, 0, 0)
FCH = StationsOwned(False, 0, 0, 0)
LIV = StationsOwned(False, 0, 0, 0)

player1 = Player("Player 1", 1500, 0, 0, 1, 3, 1)
player2 = Player("Player 2", 1500, 0, 0, 0, 0, 0)
player3 = Player("Player 3", 1500, 0, 0, 0, 0, 0)
player4 = Player("Player 4", 1500, 0, 0, 0, 0, 0)

pos = 0

def dice():
    dice_roll = random.randint(1, 6)
    dice_roll_2 = random.randint(1, 6)
    roll_result = dice_roll + dice_roll_2

    return dice_roll, dice_roll_2, roll_result


def advance_to_go():
    player1.money = player1.money + 200
    pos = 0
    print("Advance to Go (Collect £200)")
    return player1.money, pos

def Advance_to_Trafalgar(pos):
    if pos > 24:
        player1.money = player1.money + 200
    pos = 24
    print("Advance to Trafalgar Square. If you pass Go, collect £200.")
    print(pos)
    return pos, player1.money

def Advance_to_Mayfair():
    pos = 39
    print("Advance to Mayfair.")
    print(pos)
    return pos

def Advance_to_Pall_Mall(pos):
    if pos > 11:
        player1.money = player1.money + 200
    pos = 11
    print("Advance to Pall Mall. If you pass Go, collect £200.")
    print(pos)
    return pos, player1.money

def Advance_to_Station(pos):
    if pos == 7:
        pos = 15
        print("You have landed on Marylebone Station")
    elif pos == 22:
        pos = 25
        print("You have landed on Fenchurch St. Station")
    elif pos == 36:
        pos = 5
        print("You have landed on Kings Cross Station")
    return pos

def Advance_to_Utility(pos):
    if pos == 22:
        pos = 28
        print("You have landed on Water Works")
    elif pos == 7 or 36:
        pos = 12
        print("You have landed on Electric Company")
    return pos

def Bank_Divedend():
    player1.money = player1.money + 50
    print("Bank pays you dividend of £50")
    print(player1.money)
    return player1.money

def Jail_Free():
    player1.jail_free += 1
    print("You have received a Get Out Of Jail Free Card")
    return player1.jail_free


result = dice()


def Get_Out_Of_Jail_Free():
    if player1.jail_free > 0:
        print("Player 1 - Get Out Of Jail Free Cards: " + str(player1.jail_free))
        free = input("Would you like to use your Get Out Of Jail Free card? ")
        if free.lower() in ["yes", "y", "Y", "YES"]:
            player1.jail_free -= 1
            print("Player 1 - Get Out Of Jail Free Cards: " + str(player1.jail_free))
            print("You are free to go!")
        else:
            pass


def Go_Back_Three_Spaces(pos):
    pos = pos - 3
    print("Go Back Three Spaces.")
    print(pos)
    return pos

def Go_To_Jail():
    pos = 30
    print("Go To Jail. Go directly to Jail, do not pass Go, do not collect £200.")
    print(pos)
    return pos

def Make_General_Repairs():
    print(player1.money)
    player1.money = player1.money - (player1.house*25) - (player1.hotel*100)
    print("Make general repairs on all your property. For each house pay £25. For each hotel pay £100")
    print("You owe £" + str(player1.house*25 + player1.hotel*100))
    print(player1.money)
    return player1.money

def Speeding_Fine():
    player1.money = player1.money - 15
    print("Speeding fine, £15.")
    print(player1.money)
    return player1.money

# Make_General_Repairs()
# Get_Out_Of_Jail_Free()

def Advance_to_Kings_Cross(pos):
    print(player1.money)
    print(pos)
    player1.money = player1.money + 200
    pos = 5
    print("Advance to Kings Cross Station. If you pass Go, collect £200")
    print(player1.money)
    print(pos)
    return pos, player1.money


# Advance_to_Kings_Cross(pos)


def Chairman_Of_The_Board():
    # player1.money = player1.money - (50*(No_Users-1))
    player1.money = player1.money - 150
    player2.money = player2.money + 50
    player3.money = player3.money + 50
    player4.money = player4.money + 50
    print("You have been elected Chairman of the Board. Pay each player £50.")
    print(player1.money)
    print(player2.money)
    print(player3.money)
    print(player4.money)
    return player1.money, player2.money, player3.money, player4.money


# Chairman_Of_The_Board()


def Loan_Matures():
    player1.money = player1.money + 150
    print("Your building loan matures. Collect £150.")
    print(player1.money)
    return player1.money



deck = ["Advance to Go", "Advance to Mayfair", "Advance to Pall Mall", "Advance to the nearest Station",
         "Advance to Trafalgar Square", "Advance to Utility", "Bank Dividend", "Get out of jail free",
         "Go back three spaces", "Go to jail", "Make General Repairs", "Speeding Fine",
         "Advance to King's Cross Station", "Chairman of the Board", "Loan Matures"]

pos = 7

def chance():
    if not deck:  # Check if the list is empty
        reshuffle()  # Refill the list
    card_draw = random.choice(deck)
    if card_draw == "Advance to Go":
        print("Advance to Go is gone")
        advance_to_go()
    elif card_draw == "Advance to Mayfair":
        print("Advance to Mayfair is gone")
        Advance_to_Mayfair()
    elif card_draw == "Advance to Pall Mall":
        print("Advance to Pall Mall is gone")
        Advance_to_Pall_Mall(pos)
    elif card_draw == "Advance to the nearest Station":
        print("Advance to the nearest Station is gone")
        Advance_to_Station(pos)
    elif card_draw == "Advance to Trafalgar Square":
        print("Advance to Trafalgar Square is gone")
        Advance_to_Trafalgar(pos)
    elif card_draw == "Advance to Utility":
        print("Advance to Utility is gone")
        Advance_to_Utility(pos)
    elif card_draw == "Bank Dividend":
        print("Bank Dividend is gone")
        Bank_Divedend()
    elif card_draw == "Get out of jail free":
        print("Get out of jail free is gone")
        Jail_Free()
    elif card_draw == "Go back three spaces":
        print("Go back three spaces is gone")
        Go_Back_Three_Spaces(pos)
    elif card_draw == "Go to jail":
        print("-Go to jail is gone")
        Go_To_Jail()
    elif card_draw == "Make General Repairs":
        print("Make General Repairs is gone")
        Make_General_Repairs()
    elif card_draw == "Speeding Fine":
        print("Speeding Fine is gone")
        Speeding_Fine()
    elif card_draw == "Advance to King's Cross Station":
        print("Advance to King's Cross Station is gone")
        Advance_to_Kings_Cross(pos)
    elif card_draw == "Chairman of the Board":
        print("Chairman of the Board is gone")
        Chairman_Of_The_Board()
    elif card_draw == "Loan Matures":
        print("Loan Matures is gone")
        Loan_Matures()
    deck.remove(card_draw)
    print("You have removed: " + card_draw)
    return card_draw


def reshuffle():
    global deck
    deck = ["Advance to Go!", "Advance to Mayfair!", "Advance to Pall Mall!", "Advance to the nearest Station!",
             "Advance to Trafalgar Square!", "Advance to Utility", "Bank Dividend", "Get out of jail free",
             "Go back three spaces", "Go to jail", "Make General Repairs", "Speeding Fine",
             "Advance to King's Cross Station", "Chairman of the Board", "Loan Matures"]


"""print("Initial List:", deck)

chance()

print("Updated List: ", deck)

chance()

print("Updated List: ", deck)

chance()

print("Updated List: ", deck)

chance()

print("Updated List: ", deck)

chance()

print("Updated List: ", deck)

chance()

print("Updated List: ", deck)

chance()

print("Updated List: ", deck)

chance()

print("Updated List: ", deck)

chance()

print("Updated List: ", deck)

chance()

print("Updated List: ", deck)

chance()

print("Updated List: ", deck)

chance()

print("Updated List: ", deck)

chance()

print("Updated List: ", deck)

chance()

print("Updated List: ", deck)

chance()

print("Updated List: ", deck)

chance()

print("Updated List: ", deck) """

# chance()
# Loan_Matures()

# print("Dice 1 is: ", result[0])
# print("Dice 2 is: ", result[1])
# print("Roll is: ", result[2])

# if result[0] == result[1]:
#     print("Double!")
# else:
#     pass

print("Player 1 current position: " + str(pos))







num = 0
snum = 0
#pos = 15

pos = pos + result[2]


print("Player 1 new position: " + str(pos))

p = [OKR, WC, TAI, ER, PR, PM, WH, NA, BoS, MS, VS, S, FS, TS, LS, CS, P, RS, OS, BdS, PL, MF]
s = [KCS, MLB, FCH, LIV]



def landon():
    if p[num].bought == True:
        if p[num].monopoly == True:
            if p[num].one == 1:
                if p[num].two == 1:
                    if p[num].three == 1:
                        if p[num].four == 1:
                            if p[num].hotel == 1:
                                print(player1.money)
                                print("A player has a hotel at " + board[num].name + ". You owe this player £" + str(
                                    board[num].hotel) + " in rent.")
                                player1.money = player1.money - board[num].hotel
                                print(player1.money)
                            else:
                                print(player1.money)
                                print("A player has a four houses at " + board[num].name + ". You owe this player £" + str(
                                    board[num].four) + " in rent.")
                                player1.money = player1.money - board[num].four
                                print(player1.money)
                        else:
                            print(player1.money)
                            print("A player has a three houses at " + board[num].name + ". You owe this player £" + str(
                                board[num].three) + " in rent.")
                            player1.money = player1.money - board[num].three
                            print(player1.money)
                    else:
                        print(player1.money)
                        print("A player has a two houses at " + board[num].name + ". You owe this player £" + str(
                            board[num].two) + " in rent.")
                        player1.money = player1.money - board[num].two
                        print(player1.money)
                else:
                    print(player1.money)
                    print("A player has a house at " + board[num].name + ". You owe this player £" + str(
                        board[num].one) + " in rent.")
                    player1.money = player1.money - board[num].one
                    print(player1.money)
            else:
                print(player1.money)
                print("A player has a monopoly at " + board[num].name + ". You owe this player £" + str(
                    board[num].monopoly) + " in rent.")
                player1.money = player1.money - board[num].monopoly
                print(player1.money)
        else:
            print(player1.money)
            print("A player already owns " + board[num].name + ". You owe this player £" + str(board[1].rent) + " in rent.")
            player1.money = player1.money - board[num].rent
            print(player1.money)
    else:
        print("Player 1 balance is:" + str(player1.money))
        #print(p[num].bought)

        buy = input("Would you like to buy " + board[num].name + "? ")
        if buy.lower() in ["yes", "y", "Y", "YES"]:
            p[num].bought = True
            print("Player 1 has payed " + "£" + str(board[num].cost) + " for " + str(board[num].name))
            player1.money = player1.money - board[num].cost
            print("You now own " + board[num].name + "!")
            print("Player 1 new balance is: " + str(player1.money))
            player1.places_owned.append(board[num].name)
            print(player1.places_owned)

        elif buy.lower() in ["no", "n", "N", "NO"]:
            print("This property will be sent to auction!")
            print("Welcome to the Auction House!!!")
            print(board[num].name + " is up for grabs! How exciting!!")
            auction1 = True
            auction2 = True
            auction3 = True
            auction4 = True
            bid = 0
            sold = 2
            gavel1 = 1; gavel2 = 1; gavel3 = 1; gavel4 = 1
            while sold >= 0:
                if gavel1 == 1:
                    bid1 = input("Player 1, would you like to bid for " + board[num].name + "? ")
                    if bid1.lower() in ["yes", "y", "Y", "YES"]:
                        bid = bid + int(input("Player 1 has bid: "))
                        print(bid)
                    else:
                        auction1 = False
                        sold -= 1
                        gavel1 = 0
                        print("Player 1 is out of the bidding!")
                if gavel2 == 1:
                    bid2 = input("Player 2, would you like to bid for " + board[num].name + "? ")
                    if bid2.lower() in ["yes", "y", "Y", "YES"]:
                        bid = bid + int(input("Player 2 has bid: "))
                        print(bid)
                    else:
                        auction2 = False
                        sold -= 1
                        gavel2 = 0
                        print("Player 2 is out of the bidding!")
                if gavel3 == 1:
                    bid3 = input("Player 3, would you like to bid for " + board[num].name + "? ")
                    if bid3.lower() in ["yes", "y", "Y", "YES"]:
                        bid = bid + int(input("Player 3 has bid: "))
                        print(bid)
                    else:
                        auction3 = False
                        sold -= 1
                        gavel3 = 0
                        print("Player 3 is out of the bidding!")
                if gavel4 == 1:
                    bid4 = input("Player 4, would you like to bid for " + board[num].name + "? ")
                    if bid4.lower() in ["yes", "y", "Y", "YES"]:
                        bid = bid + int(input("Player 4 has bid: "))
                        print(bid)
                    else:
                        auction4 = False
                        sold -= 1
                        gavel4 = 0
                        print("Player 4 is out of the bidding!")
            if auction1:
                print("Player 1's")
                print(bid)
                player1.money = player1.money - bid
                print(player1.money)
                player1.places_owned.append(board[num].name)
                print("Player 1 Properties: " + str(player1.places_owned))
                p[num].bought = True

            elif auction2:
                print("Player 2's")
                print(bid)
                player2.money = player2.money - bid
                print(player2.money)
                player2.places_owned.append(board[num].name)
                print("Player 2 Properties: " + str(player2.places_owned))
                p[num].bought = True

            elif auction3:
                print("Player 3's")
                print(bid)
                player3.money = player3.money - bid
                print(player3.money)
                player3.places_owned.append(board[num].name)
                print("Player 3 Properties: " +str(player3.places_owned))
                p[num].bought = True

            elif auction4:
                print("Player 4's")
                print(bid)
                player4.money = player4.money - bid
                print(player4.money)
                player4.places_owned.append(board[num].name)
                print("Player 4 Properties: " +str(player4.places_owned))
                p[num].bought = True


def landonstation():
    if s[snum].bought == True:
            if s[snum].two == 1:
                if s[snum].three == 1:
                    if s[snum].four == 1:
                        print(player1.money)
                        print("A player owns " + platform[snum].name + " and the three other stations. You owe this player £"
                              + str(platform[snum].four) + " in rent.")
                        player1.money = player1.money - platform[snum].four
                        print(player1.money)
                    else:
                        print(player1.money)
                        print("A player owns " + platform[snum].name + " and two other stations. You owe this player £" + str(
                            platform[snum].three) + " in rent.")
                        player1.money = player1.money - platform[snum].three
                        print(player1.money)
                else:
                    print(player1.money)
                    print("A player owns " + platform[snum].name + " and one other stations. You owe this player £" + str(
                        platform[snum].two) + " in rent.")
                    player1.money = player1.money - platform[snum].two
                    print(player1.money)
            else:
                print(player1.money)
                print("A player owns " + platform[snum].name + ". You owe this player £" + str(
                    platform[snum].rent) + " in rent.")
                player1.money = player1.money - platform[snum].rent
                print(player1.money)

    else:
        print("Player 1 balance is:" + str(player1.money))
        # print(p[snum].bought)
        buy = input("Would you like to buy " + platform[snum].name + "? ")
        if buy.lower() in ["yes", "y", "Y", "YES"]:
            s[snum].bought = True
            print("Player 1 has payed " + "£" + str(platform[snum].cost) + " for " + str(platform[snum].name))
            player1.money = player1.money - platform[snum].cost
            print("You now own " + platform[snum].name + "!")
            print("Player 1 new balance is: " + str(player1.money))
            player1.places_owned.append(platform[snum].name)
            print(player1.places_owned)

        elif buy.lower() in ["no", "n", "N", "NO"]:
            print("This property will be sent to auction!")
            print("Welcome to the Auction House!!!")
            print(platform[snum].name + " is up for grabs! How exciting!!")
            auction1 = True
            auction2 = True
            auction3 = True
            auction4 = True
            bid = 0
            sold = 2
            gavel1 = 1;
            gavel2 = 1;
            gavel3 = 1;
            gavel4 = 1
            while sold >= 0:
                if gavel1 == 1:
                    bid1 = input("Player 1, would you like to bid for " + platform[snum].name + "? ")
                    if bid1.lower() in ["yes", "y", "Y", "YES"]:
                        bid = bid + int(input("Player 1 has bid: "))
                        print(bid)
                    else:
                        auction1 = False
                        sold -= 1
                        gavel1 = 0
                        print("Player 1 is out of the bidding!")
                if gavel2 == 1:
                    bid2 = input("Player 2, would you like to bid for " + platform[snum].name + "? ")
                    if bid2.lower() in ["yes", "y", "Y", "YES"]:
                        bid = bid + int(input("Player 2 has bid: "))
                        print(bid)
                    else:
                        auction2 = False
                        sold -= 1
                        gavel2 = 0
                        print("Player 2 is out of the bidding!")
                if gavel3 == 1:
                    bid3 = input("Player 3, would you like to bid for " + platform[snum].name + "? ")
                    if bid3.lower() in ["yes", "y", "Y", "YES"]:
                        bid = bid + int(input("Player 3 has bid: "))
                        print(bid)
                    else:
                        auction3 = False
                        sold -= 1
                        gavel3 = 0
                        print("Player 3 is out of the bidding!")
                if gavel4 == 1:
                    bid4 = input("Player 4, would you like to bid for " + platform[snum].name + "? ")
                    if bid4.lower() in ["yes", "y", "Y", "YES"]:
                        bid = bid + int(input("Player 4 has bid: "))
                        print(bid)
                    else:
                        auction4 = False
                        sold -= 1
                        gavel4 = 0
                        print("Player 4 is out of the bidding!")
            if auction1:
                print("Player 1's")
                print(bid)
                player1.money = player1.money - bid
                print(player1.money)
                player1.places_owned.append(platform[snum].name)
                print("Player 1 Properties: " + str(player1.places_owned))
                s[snum].bought = True

            elif auction2:
                print("Player 2's")
                print(bid)
                player2.money = player2.money - bid
                print(player2.money)
                player2.places_owned.append(platform[snum].name)
                print("Player 2 Properties: " + str(player2.places_owned))
                s[snum].bought = True

            elif auction3:
                print("Player 3's")
                print(bid)
                player3.money = player3.money - bid
                print(player3.money)
                player3.places_owned.append(platform[snum].name)
                print("Player 3 Properties: " + str(player3.places_owned))
                s[snum].bought = True

            elif auction4:
                print("Player 4's")
                print(bid)
                player4.money = player4.money - bid
                print(player4.money)
                player4.places_owned.append(platform[snum].name)
                print("Player 4 Properties: " + str(player4.places_owned))
                s[snum].bought = True




if pos == 1 or 3 or 5 or 6 or 8 or 9 or 11 or 13 or 14 or 15 or 16 or 18 or 19 or 21 or 23 or 24 or 25 or 26 or 27 or 29 or 31 or 32 or 34 or 35 or 37 or 39:
    if pos == 1:
        num = 0  # Old Kent Road
        landon()
    elif pos == 3:
        num = 1  # Whitechapel Road
        landon()
    elif pos == 6:
        num = 2  # The Angel, Islington
        landon()
    elif pos == 8:
        num = 3  # Euston Road
        landon()
    elif pos == 9:
        num = 4  # Pentonville Road
        landon()
    elif pos == 11:
        num = 5  # Pall Mall
        landon()
    elif pos == 13:
        num = 6  # Whitehall
        landon()
    elif pos == 14:
        num = 7  # Northumberland Avenue
        landon()
    elif pos == 16:
        num = 8  # Bow Street
        landon()
    elif pos == 18:
        num = 9  # Marlborough Street
        landon()
    elif pos == 19:
        num = 10  # Vine Street
        landon()
    elif pos == 21:
        num = 11  # Strand
        landon()
    elif pos == 23:
        num = 12  # Fleet Street
        landon()
    elif pos == 24:
        num = 13  # Trafalgar Square
        landon()
    elif pos == 26:
        num = 14  # Leicester Square
        landon()
    elif pos == 27:
        num = 15  # Coventry Street
        landon()
    elif pos == 29:
        num = 16  # Piccadilly
        landon()
    elif pos == 31:
        num = 17  # Regent Street
        landon()
    elif pos == 32:
        num = 18  # Oxford Street
        landon()
    elif pos == 34:
        num = 19  # Bond Street
        landon()
    elif pos == 37:
        num = 20  # Park Lane
        landon()
    elif pos == 39:
        num = 21  # Mayfair
        landon()
    elif pos == 5:
        snum = 0  # King's Cross Station
        landonstation()
    elif pos == 15:
        snum = 1  # Marylebone Station
        landonstation()
    elif pos == 25:
        snum = 2  # Fenchurch Station
        landonstation()
    elif pos == 35:
        snum = 3  # Liverpool St. Station
        landonstation()






def score():
    print(
        "===============================================================================================================")
    print("             " + "Player 1" + "                      "
          + "Player 2" + "                      "
          + "Player 3" + "                      "
          + "Player 4" + "         ")
    print(
        "                                                                                                             ")
    print("Money" + "        " + str(player1.money) + "                          "
          + str(player2.money) + "                          "
          + str(player3.money) + "                          "
          + str(player4.money) + "             ")
    print(
        "                                                                                                             ")
    print("Position" + "     " + str(10) + "                             "
          + str(0) + "                             "
          + str(0) + "                             "
          + str(0) + "             ")
    print(
        "                                                                                                             ")
    print("Properties" + "   " + str(0) + "                             "
          + str(0) + "                             "
          + str(0) + "                             "
          + str(0) + "             ")
    print(
        "                                                                                                             ")
    print("Monopolies" + "   " + str(0) + "                             "
          + str(0) + "                             "
          + str(0) + "                             "
          + str(0) + "             ")
    print(
        "                                                                                                             ")
    print(
        "========================================================================================================"
        "=======")


# Main program execution
while True:
    user_input = input("Enter a command: ")
    if user_input.lower() == "score":
        score()