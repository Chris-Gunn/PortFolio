class Player:
#    def __init__(self,name,money,double,in_jail):
    def __init__(self,name,money,position):
        self.name = name
        self.money = money
        self.position = position
        #self.double = double
        #self.jail = in_jail
        self.places_owned = []


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
    def __init__(self,bought,one,two,three,four):
        self.bought = bought
        self.one = one
        self.two = two
        self.three = three
        self.four = four





board = [
    Property("Go", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
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
    Stations("King's Cross Station", 200, 25, 50, 100, 200, 100),
    Stations("Marylebone Station", 200, 25, 50, 100, 200, 100),
    Stations("Fenchurch St. Station", 200, 25, 50, 100, 200, 100),
    Stations("Liverpool St. Station", 200, 25, 50, 100, 200, 100)
]

Go = Owned(False, False, 0, 0, 0, 0, 0)
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

KCS = Stations("King's Cross Station", 200, 25, 50, 100, 200, 100)
MLB = Stations("Marylebone Station", 200, 25, 50, 100, 200,100)
FCH = Stations("Fenchurch St. Station", 200, 25, 50, 100, 200, 100)
LIV = Stations("Liverpool St. Station", 200, 25, 50, 100, 200, 100)

KCS = StationsOwned(False, 0, 0, 0, 0)
MLB = StationsOwned(False, 0, 0, 0, 0)
FCH = StationsOwned(False, 0, 0, 0, 0)
LIV = StationsOwned(False, 0, 0, 0, 0)

player1 = Player("Player 1", 1500, 0)
player2 = Player("Player 2", 1500, 0)
player3 = Player("Player 3", 1500, 0)
player4 = Player("Player 4", 1500, 0)

#print(PL.bought)

#print(CS.bought)

OKR.bought = False
print(OKR.bought)

#print(CS.bought)



if OKR.bought == True:
    print(player1.money)
    print("A player already owns " + board[1].name + ". You owe this player £" + str(board[1].rent) + " in rent.")
    player1.money = player1.money - board[1].rent
    print(player1.money)
else:
    print(player1.money)
    print(OKR.bought)
    buy = input("Would you like to buy " + board[1].name + "? ")
    if buy.lower() in ["yes", "y", "Y", "YES"]:
        OKR.bought = True
        print(OKR.bought)
        print(player1.money)
        player1.money = player1.money - board[1].cost
        print("You now own " + board[1].name + "!")
        print(player1.money)
        print(board[1].name)
        print(board[1].cost)
        player1.places_owned.append(board[1].name)
        print(player1.places_owned)

    else:
        pass


if CS.bought == True:
    print(player1.money)
    print("A player already owns Coventry Street. You owe this player £22 in rent.")
    player1.money = player1.money - board[16].rent
    print(player1.money)
else:
    print(player1.money)
    print(CS.bought)
    buy = input("Would you like to buy Coventry Street? ")
    if buy.lower() in ["yes", "y", "Y", "YES"]:
        CS.bought = True
        print(CS.bought)
        print(player1.money)
        player1.money = player1.money - board[16].cost
        print("You own Coventry Street!")
        print(player1.money)
        print(board[16].name)
        print(board[16].cost)
        player1.places_owned.append(board[16].name)
        print(player1.places_owned)

    else:
        pass


#if not board[1].is_owned():
#    if player1.money >= board[1].cost:
#        print(player1.money)
#        player1.money = player1.money - board[1].cost
#        print(player1.money)
#        player1.places_owned.append(board[1].name)
#        board[1].owner = player1.name
#        print("You own Old Kent Road!")
#        print(player1.money)

#    else:
#        player1.money = player1.money - board[1].rent
#        print(player1.money)
#else:
#    print("Someone's got Old Kent Road mate!")
#    print(player1.money)
#    player1.money = player1.money - board[1].rent
#    print(player1.money)


class Player:
#    def __init__(self,name,money,double,in_jail):
    def __init__(self,name,money,position):
        self.name = name
        self.money = money
        self.position = position
        #self.double = double
        #self.jail = in_jail
        self.places_owned = []


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
    def __init__(self,bought,one,two,three,four):
        self.bought = bought
        self.one = one
        self.two = two
        self.three = three
        self.four = four





board = [
    Property("Go", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
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
    Stations("King's Cross Station", 200, 25, 50, 100, 200, 100),
    Stations("Marylebone Station", 200, 25, 50, 100, 200, 100),
    Stations("Fenchurch St. Station", 200, 25, 50, 100, 200, 100),
    Stations("Liverpool St. Station", 200, 25, 50, 100, 200, 100)
]

Go = Owned(False, False, 0, 0, 0, 0, 0)
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

KCS = Stations("King's Cross Station", 200, 25, 50, 100, 200, 100)
MLB = Stations("Marylebone Station", 200, 25, 50, 100, 200,100)
FCH = Stations("Fenchurch St. Station", 200, 25, 50, 100, 200, 100)
LIV = Stations("Liverpool St. Station", 200, 25, 50, 100, 200, 100)

KCS = StationsOwned(False, 0, 0, 0, 0)
MLB = StationsOwned(False, 0, 0, 0, 0)
FCH = StationsOwned(False, 0, 0, 0, 0)
LIV = StationsOwned(False, 0, 0, 0, 0)

player1 = Player("Player 1", 1500, 0)
player2 = Player("Player 2", 1500, 0)
player3 = Player("Player 3", 1500, 0)
player4 = Player("Player 4", 1500, 0)

#print(PL.bought)

#print(CS.bought)

OKR.bought = False
WC.bought = False
print(OKR.bought)
print(WC.bought)

#print(CS.bought)



if OKR.bought == True:
    print(player1.money)
    print("A player already owns " + board[1].name + ". You owe this player £" + str(board[1].rent) + " in rent.")
    player1.money = player1.money - board[1].rent
    print(player1.money)
else:
    print(player1.money)
    print(OKR.bought)
    buy = input("Would you like to buy " + board[1].name + "? ")
    if buy.lower() in ["yes", "y", "Y", "YES"]:
        OKR.bought = True
        print(OKR.bought)
        print(player1.money)
        player1.money = player1.money - board[1].cost
        print("You now own " + board[1].name + "!")
        print(player1.money)
        print(board[1].name)
        print(board[1].cost)
        player1.places_owned.append(board[1].name)
        print(player1.places_owned)

    else:
        pass


#OKR.bought = False
#print(OKR.bought)

#print(CS.bought)



if WC.bought == True:
    print(player1.money)
    print("A player already owns " + board[2].name + ". You owe this player £" + str(board[2].rent) + " in rent.")
    player1.money = player1.money - board[2].rent
    print(player1.money)
else:
    print(player1.money)
    print(WC.bought)
    buy = input("Would you like to buy " + board[2].name + "? ")
    if buy.lower() in ["yes", "y", "Y", "YES"]:
        WC.bought = True
        print(WC.bought)
        print(player1.money)
        player1.money = player1.money - board[2].cost
        print("You now own " + board[2].name + "!")
        print(player1.money)
        print(board[2].name)
        print(board[2].cost)
        player1.places_owned.append(board[2].name)
        print(player1.places_owned)

    elif buy.lower() in ["no", "n", "N", "NO"]:
        print("This property will be sent to auction!")
        print("Welcome to the Auction House!!!")
        print(board[2].name + " is up for grabs! How exciting!!")
        auction1 = True
        auction2 = True
        auction3 = True
        auction4 = True
        bid = 0
        sold = 2
        gavel1 = 1; gavel2 = 1; gavel3 = 1; gavel4 = 1
        while sold >= 0:
            if gavel1 == 1:
                bid1 = input("Player 1, would you like to bid for " + board[2].name + "? ")
                if bid1.lower() in ["yes", "y", "Y", "YES"]:
                    bid = bid + int(input("Player 1 has bid: "))
                    print(bid)
                else:
                    auction1 = False
                    sold -= 1
                    gavel1 = 0
                    print("Player 1 is out of the bidding!")
            if gavel2 == 1:
                bid2 = input("Player 2, would you like to bid for " + board[2].name + "? ")
                if bid2.lower() in ["yes", "y", "Y", "YES"]:
                    bid = bid + int(input("Player 2 has bid: "))
                    print(bid)
                else:
                    auction2 = False
                    sold -= 1
                    gavel2 = 0
                    print("Player 2 is out of the bidding!")
            if gavel3 == 1:
                bid3 = input("Player 3, would you like to bid for " + board[2].name + "? ")
                if bid3.lower() in ["yes", "y", "Y", "YES"]:
                    bid = bid + int(input("Player 3 has bid: "))
                    print(bid)
                else:
                    auction3 = False
                    sold -= 1
                    gavel3 = 0
                    print("Player 3 is out of the bidding!")
            if gavel4 == 1:
                bid4 = input("Player 4, would you like to bid for " + board[2].name + "? ")
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
            player1.places_owned.append(board[2].name)
            print(player1.places_owned)
        elif auction2:
            print("Player 2's")
            print(bid)
            player2.money = player2.money - bid
            print(player2.money)
            player2.places_owned.append(board[2].name)
            print(player2.places_owned)
        elif auction3:
            print("Player 3's")
            print(bid)
            player3.money = player3.money - bid
            print(player3.money)
            player3.places_owned.append(board[2].name)
            print(player3.places_owned)
        elif auction4:
            print("Player 4's")
            print(bid)
            player4.money = player4.money - bid
            print(player4.money)
            player4.places_owned.append(board[2].name)
            print(player4.places_owned)














class Player:
#    def __init__(self,name,money,double,in_jail):
    def __init__(self,name,money,position):
        self.name = name
        self.money = money
        self.position = position
        #self.double = double
        #self.jail = in_jail
        self.places_owned = []


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
    def __init__(self,bought,one,two,three,four):
        self.bought = bought
        self.one = one
        self.two = two
        self.three = three
        self.four = four





board = [
    Property("Go", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
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
    Stations("King's Cross Station", 200, 25, 50, 100, 200, 100),
    Stations("Marylebone Station", 200, 25, 50, 100, 200, 100),
    Stations("Fenchurch St. Station", 200, 25, 50, 100, 200, 100),
    Stations("Liverpool St. Station", 200, 25, 50, 100, 200, 100)
]

Go = Owned(False, False, 0, 0, 0, 0, 0)  #change OKR etc. to p1, p2 etc. then call them p[number]
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

KCS = Stations("King's Cross Station", 200, 25, 50, 100, 200, 100)
MLB = Stations("Marylebone Station", 200, 25, 50, 100, 200,100)
FCH = Stations("Fenchurch St. Station", 200, 25, 50, 100, 200, 100)
LIV = Stations("Liverpool St. Station", 200, 25, 50, 100, 200, 100)

KCS = StationsOwned(False, 0, 0, 0, 0)
MLB = StationsOwned(False, 0, 0, 0, 0)
FCH = StationsOwned(False, 0, 0, 0, 0)
LIV = StationsOwned(False, 0, 0, 0, 0)

pos = 5
num = 0
snum = 0

p = [Go, OKR, WC, TAI, ER, PR, PM, WH, NA, BoS, MS, VS, S, FS, TS, LS, CS, P, RS, OS, BdS, PL, MF]
s = [KCS, MLB, FCH, LIV]
if pos == 1:
    num = 1         #Old Kent Road
elif pos == 3:
    num = 2         #Whitechapel Road
elif pos == 6:
    num = 3         #The Angel, Islington
elif pos == 8:
    num = 4         #Euston Road
elif pos == 9:
    num = 5         #Pentonville Road
elif pos == 11:
    num = 6         #Pall Mall
elif pos == 13:
    num = 7         #Whitehall
elif pos == 14:
    num = 8         #Northumberland Avenue
elif pos == 16:
    num = 9         #Bow Street
elif pos == 18:
    num = 10        #Marlborough Street
elif pos == 19:
    num = 11        #Vine Street
elif pos == 21:
    num = 12        #Strand
elif pos == 23:
    num = 13        #Fleet Street
elif pos == 24:
    num = 14        #Trafalgar Square
elif pos == 26:
    num = 15        #Leicester Square
elif pos == 27:
    num = 16        #Coventry Street
elif pos == 29:
    num = 17        #Piccadilly
elif pos == 31:
    num = 18        #Regent Street
elif pos == 32:
    num = 19        #Oxford Street
elif pos == 34:
    num = 20        #Bond Street
elif pos == 37:
    num = 21        #Park Lane
elif pos == 39:
    num = 22        #Mayfair

if pos == 5:
    snum = 1         #Old Kent Road
elif pos == 15:
    snum = 2         #Whitechapel Road
elif pos == 25:
    snum = 3         #The Angel, Islington
elif pos == 35:
    snum = 4         #Euston Road
player1 = Player("Player 1", 1500, 0)
player2 = Player("Player 2", 1500, 0)
player3 = Player("Player 3", 1500, 0)
player4 = Player("Player 4", 1500, 0)

#print(PL.bought)

#print(CS.bought)



#p[num].bought = False
#p[2].bought = False
#print(p[num].bought)
#print(WC.bought)

#print(CS.bought)


#if p[num].bought == True:
#    print(player1.money)
#    print("A player already owns " + board[1].name + ". You owe this player £" + str(board[1].rent) + " in rent.")
#    player1.money = player1.money - board[1].rent
#    print(player1.money)
#else:
#    print(player1.money)
#    print(p[num].bought)
#    buy = input("Would you like to buy " + board[1].name + "? ")
#    if buy.lower() in ["yes", "y", "Y", "YES"]:
#        p[num].bought = True
#        print(p[num].bought)
#        print(player1.money)
#        player1.money = player1.money - board[1].cost
#        print("You now own " + board[1].name + "!")
#        print(player1.money)
#        print(board[1].name)
#        print(board[1].cost)
#        player1.places_owned.append(board[1].name)
#        print(player1.places_owned)

#    else:
#        pass


#p[num].bought = False
#print(p[num].bought)

#print(CS.bought)





#LAND ON PROPERTIES - NO STATIONS

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




#DICE ROLL


import random
player = 0
turn = 0
game = 0
double = 0
num = 0
num2 = 0

def dice():
    global dice_roll
    global dice_roll_2
    dice_roll = random.randint(1,6)
    dice_roll_2 = random.randint(1, 6)
    roll_result = dice_roll + dice_roll_2
    print("Dice 1 is: " + str(dice_roll))
    print("Dice 2 is: " + str(dice_roll_2))
    print("Roll is: " + str(roll_result))

    return dice_roll
    return dice_roll_2
    return roll_result


def Doubles():
    global num
    global num2
    num = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
    return num
    return num2


print(double)
dice()   #Picks two numbers
if dice_roll == dice_roll_2: #Checks if numbers are equal
    print("Double")
    double += 1  #if numbers are equal, increase double number by 1
    print(double)
    dice()
    if dice_roll == dice_roll_2:
        print("Double")
        double += 1
        print(double)
        dice()
        if double == 2 and dice_roll == dice_roll_2:
            double += 1
            print("Double")
            print(double)
            print("Go to jail!")
            double = 0
            print("Double reset")
        else:
            double == 0
            print("Double reset")
    else:
        double == 0
        print("Double reset")
else:
    double == 0
    print("Double reset")



















class Player:
#    def __init__(self,name,money,double,in_jail):
    def __init__(self,name,money,position):
        self.name = name
        self.money = money
        self.position = position
        #self.double = double
        #self.jail = in_jail
        self.places_owned = []


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
    def __init__(self,bought,one,two,three,four):
        self.bought = bought
        self.one = one
        self.two = two
        self.three = three
        self.four = four





board = [
    Property("Go", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
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
    Stations("King's Cross Station", 200, 25, 50, 100, 200, 100),
    Stations("Marylebone Station", 200, 25, 50, 100, 200, 100),
    Stations("Fenchurch St. Station", 200, 25, 50, 100, 200, 100),
    Stations("Liverpool St. Station", 200, 25, 50, 100, 200, 100)
]

Go = Owned(False, False, 0, 0, 0, 0, 0)
OKR = Owned(False, False, 0, 0, 0, 0, 0)
WC = Owned(True, True, 1, 1, 1, 1, 1)
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

KCS = Stations("King's Cross Station", 200, 25, 50, 100, 200, 100)
MLB = Stations("Marylebone Station", 200, 25, 50, 100, 200,100)
FCH = Stations("Fenchurch St. Station", 200, 25, 50, 100, 200, 100)
LIV = Stations("Liverpool St. Station", 200, 25, 50, 100, 200, 100)

KCS = StationsOwned(False, 0, 0, 0, 0)
MLB = StationsOwned(False, 0, 0, 0, 0)
FCH = StationsOwned(False, 0, 0, 0, 0)
LIV = StationsOwned(False, 0, 0, 0, 0)

player1 = Player("Player 1", 1500, 0)
player2 = Player("Player 2", 1500, 0)
player3 = Player("Player 3", 1500, 0)
player4 = Player("Player 4", 1500, 0)

#print(PL.bought)

#print(CS.bought)

OKR.bought = False
WC.bought = True
print(OKR.bought)
print(WC.bought)

#print(CS.bought)



if OKR.bought == True:
    print(player1.money)
    print("A player already owns " + board[1].name + ". You owe this player £" + str(board[1].rent) + " in rent.")
    player1.money = player1.money - board[1].rent
    print(player1.money)
else:
    print(player1.money)
    print(OKR.bought)
    buy = input("Would you like to buy " + board[1].name + "? ")
    if buy.lower() in ["yes", "y", "Y", "YES"]:
        OKR.bought = True
        print(OKR.bought)
        print(player1.money)
        player1.money = player1.money - board[1].cost
        print("You now own " + board[1].name + "!")
        print(player1.money)
        print(board[1].name)
        print(board[1].cost)
        player1.places_owned.append(board[1].name)
        print(player1.places_owned)

    else:
        pass


#OKR.bought = False
#print(OKR.bought)

#print(CS.bought)



if WC.bought == True:
    if WC.monopoly == True:
        if WC.one == 1:
            if WC.two == 1:
                if WC.three == 1:
                    if WC.four == 1:
                        if WC.hotel == 1:
                            print(player1.money)
                            print("A player has a hotel at " + board[2].name + ". You owe this player £" + str(
                                board[2].hotel) + " in rent.")
                            player1.money = player1.money - board[2].hotel
                            print(player1.money)
                        else:
                            print(player1.money)
                            print("A player has a four houses at " + board[2].name + ". You owe this player £" + str(
                                board[2].four) + " in rent.")
                            player1.money = player1.money - board[2].four
                            print(player1.money)
                    else:
                        print(player1.money)
                        print("A player has a three houses at " + board[2].name + ". You owe this player £" + str(
                            board[2].three) + " in rent.")
                        player1.money = player1.money - board[2].three
                        print(player1.money)
                else:
                    print(player1.money)
                    print("A player has a two houses at " + board[2].name + ". You owe this player £" + str(
                        board[2].two) + " in rent.")
                    player1.money = player1.money - board[2].two
                    print(player1.money)
            else:
                print(player1.money)
                print("A player has a house at " + board[2].name + ". You owe this player £" + str(
                    board[2].one) + " in rent.")
                player1.money = player1.money - board[2].one
                print(player1.money)
        else:
            print(player1.money)
            print("A player has a monopoly at " + board[2].name + ". You owe this player £" + str(
                board[2].monopoly) + " in rent.")
            player1.money = player1.money - board[2].monopoly
            print(player1.money)
    else:
        print(player1.money)
        print("A player already owns " + board[1].name + ". You owe this player £" + str(board[1].rent) + " in rent.")
        player1.money = player1.money - board[1].rent
        print(player1.money)
else:
    print(player1.money)
    print(WC.bought)
    buy = input("Would you like to buy " + board[2].name + "? ")
    if buy.lower() in ["yes", "y", "Y", "YES"]:
        WC.bought = True
        print(WC.bought)
        print(player1.money)
        player1.money = player1.money - board[2].cost
        print("You now own " + board[2].name + "!")
        print(player1.money)
        print(board[2].name)
        print(board[2].cost)
        player1.places_owned.append(board[2].name)
        print(player1.places_owned)

    elif buy.lower() in ["no", "n", "N", "NO"]:
        print("This property will be sent to auction!")
        print("Welcome to the Auction House!!!")
        print(board[2].name + " is up for grabs! How exciting!!")
        auction1 = True
        auction2 = True
        auction3 = True
        auction4 = True
        bid = 0
        sold = 2
        gavel1 = 1; gavel2 = 1; gavel3 = 1; gavel4 = 1
        while sold >= 0:
            if gavel1 == 1:
                bid1 = input("Player 1, would you like to bid for " + board[2].name + "? ")
                if bid1.lower() in ["yes", "y", "Y", "YES"]:
                    bid = bid + int(input("Player 1 has bid: "))
                    print(bid)
                else:
                    auction1 = False
                    sold -= 1
                    gavel1 = 0
                    print("Player 1 is out of the bidding!")
            if gavel2 == 1:
                bid2 = input("Player 2, would you like to bid for " + board[2].name + "? ")
                if bid2.lower() in ["yes", "y", "Y", "YES"]:
                    bid = bid + int(input("Player 2 has bid: "))
                    print(bid)
                else:
                    auction2 = False
                    sold -= 1
                    gavel2 = 0
                    print("Player 2 is out of the bidding!")
            if gavel3 == 1:
                bid3 = input("Player 3, would you like to bid for " + board[2].name + "? ")
                if bid3.lower() in ["yes", "y", "Y", "YES"]:
                    bid = bid + int(input("Player 3 has bid: "))
                    print(bid)
                else:
                    auction3 = False
                    sold -= 1
                    gavel3 = 0
                    print("Player 3 is out of the bidding!")
            if gavel4 == 1:
                bid4 = input("Player 4, would you like to bid for " + board[2].name + "? ")
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
            player1.places_owned.append(board[2].name)
            print(player1.places_owned)
            WC.bought = True

        elif auction2:
            print("Player 2's")
            print(bid)
            player2.money = player2.money - bid
            print(player2.money)
            player2.places_owned.append(board[2].name)
            print(player2.places_owned)
            WC.bought = True

        elif auction3:
            print("Player 3's")
            print(bid)
            player3.money = player3.money - bid
            print(player3.money)
            player3.places_owned.append(board[2].name)
            print(player3.places_owned)
            WC.bought = True

        elif auction4:
            print("Player 4's")
            print(bid)
            player4.money = player4.money - bid
            print(player4.money)
            player4.places_owned.append(board[2].name)
            print(player4.places_owned)
            WC.bought = True




#DOUBLES

import random
player = 0
turn = 0
game = 0
double = 0
num = 0
num2 = 0

def dice():
    global dice_roll
    global dice_roll_2
    dice_roll = random.randint(1,6)
    dice_roll_2 = random.randint(1, 6)
    roll_result = dice_roll + dice_roll_2
    print("Dice 1 is: " + str(dice_roll))
    print("Dice 2 is: " + str(dice_roll_2))
    print("Roll is: " + str(roll_result))

    return dice_roll
    return dice_roll_2
    return roll_result


def Doubles():
    global num
    global num2
    num = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
    return num
    return num2


print(double)
Doubles()   #Picks two numbers
if num == num2: #Checks if numbers are equal
    print("Double")
    double += 1  #if numbers are equal, increase double number by 1
    print(double)
    Doubles()
    if num == num2:
        print("Double")
        double += 1
        print(double)
        Doubles()
        if double == 2 and num == num2:
            print("Go to jail!")
            double = 0
        else:
            double == 0
            print("Double reset")
    else:
        double == 0
        print("Double reset")
else:
    double == 0
    print("Double reset")

dice()
if dice_roll == dice_roll_2:
    print("Double")
    double += 1
    print(double)
    dice()
    if dice_roll == dice_roll_2:
        print("Double")
        double += 1
        print(double)
        dice()
        if double == 3:
            print("Go to jail!")
            double = 0
else:
    double == 0
    print("Double reset")
    print(double)

#Monopoly.py


class Player:
#    def __init__(self,name,money,double,in_jail):
    def __init__(self,name,money):
        self.name = name
        self.money = money
        #self.double = double
        #self.jail = in_jail
        self.places_owned = []


class Property:
    def __init__(self, name, cost, rent, set, one_house, two_houses, three_houses, four_houses, hotel, mortgage, House_Cost):
        self.name = name
        self.cost = cost
        self.rent = rent
        self.set = set
        self.one_house = one_house
        self.two = two_houses
        self.three = three_houses
        self.four = four_houses
        self.hotel = hotel
        self.mortgage = mortgage
        self.House_Cost = House_Cost
        self.owner = None

    def is_owned(self):
        return self.owner is not None

class Owned:
    def __init__(self,property,bought,monopoly,one,two,three,four,hotel):
        self.property = property
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
    def __init__(self,stations,bought,one,two,three,four):
        self.stations = stations
        self.bought = bought
        self.one = one
        self.two = two
        self.three = three
        self.four = four


KCS = Stations("King's Cross Station", 200, 25, 50, 100, 200, 100)
MLB = Stations("Marylebone Station", 200, 25, 50, 100, 200, 100)
FCH = Stations("Fenchurch St. Station", 200, 25, 50, 100, 200, 100)
LIV = Stations("Liverpool St. Station", 200, 25, 50, 100, 200, 100)


Go = Property("Go", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
OKR = Property("Old Kent Road", 50, 2, 4, 10, 30, 90, 160, 250, 50, 50)
WC = Property("Whitechapel Road", 60, 4, 8, 20, 60, 180, 320, 450, 50, 50)
TAI = Property("TheAngel, Islington", 100, 6, 12, 30, 90, 270, 400, 550, 50, 50)
ER = Property("Euston Road", 100, 6, 12, 30, 90, 270, 400, 550, 50, 50)
PR = Property("Pentonville Road", 120, 8, 16, 40, 100, 300, 450, 600, 50, 50)
PM = Property("Pall Mall", 140, 10, 20, 50, 150, 450, 625, 750, 100, 100)
WH = Property("Whitehall", 140, 10, 20, 50, 150, 450, 625, 750, 100, 100)
NA = Property("Northumberland Avenue", 160, 12, 24, 60, 180, 500, 700, 900, 100, 100)
BoS = Property("Bow Street", 180, 14, 28, 70, 200, 550, 750, 950, 100, 100)
MS = Property("Marlborough Street", 180, 14, 28, 70, 200, 550, 750, 950, 100, 100)
VS = Property("Vine Street", 200, 16, 32, 80, 220, 600, 800, 1000, 100, 100)
S = Property("Strand", 220, 18, 36, 90, 250, 700, 875, 1050, 150, 150)
FS = Property("Fleet Street", 220, 18, 36, 90, 250, 700, 875, 1050, 150, 150)
TS = Property("Trafalgar Square", 240, 20, 40, 100, 300, 750, 925, 1100, 150, 150)
LS = Property("Leicester Square", 260, 22, 44, 110, 330, 800, 975, 1150, 150, 150)
CS = Property("Coventry Street", 260, 22, 44, 110, 330, 800, 975, 1150, 150, 150)
P = Property("Piccadilly", 280, 24, 48, 120, 360, 850, 1025, 1200, 150, 150)
RS = Property("Regent Street", 300, 26, 52, 130, 390, 900, 1100, 1275, 200, 200)
OS = Property("Oxford Street", 300, 26, 52, 130, 390, 900, 1100, 1275, 200, 200)
BdS = Property("Bond Street", 320, 28, 56, 150, 450, 1000, 1200, 1400, 200, 200)
PL = Property("Park Lane", 350, 35, 70, 175, 500, 1100, 1300, 1500, 200, 200)
MF = Property("Mayfair", 400, 50, 100, 200, 600, 1400, 1700, 2000, 200, 200)


oGo = Owned(Go, False, False, 0, 0, 0, 0, 0)
oOKR = Owned(OKR, False, False, 0, 0, 0, 0, 0)
oWC = Owned(WC, False, False, 0, 0, 0, 0, 0)
oTAI = Owned(TAI, False, False, 0, 0, 0, 0, 0)
oER = Owned(ER, False, False, 0, 0, 0, 0, 0)
oPR = Owned(PR, False, False, 0, 0, 0, 0, 0)
oPM = Owned(PM, False, False, 0, 0, 0, 0, 0)
oWH = Owned(WH, False, False, 0, 0, 0, 0, 0)
oNA = Owned(NA, False, False, 0, 0, 0, 0, 0)
oBoS = Owned(BoS, False, False, 0, 0, 0, 0, 0)
oMS = Owned(MS, False, False, 0, 0, 0, 0, 0)
oVS = Owned(VS, False, False, 0, 0, 0, 0, 0)
oS = Owned(S, False, False, 0, 0, 0, 0, 0)
oFS = Owned(FS, False, False, 0, 0, 0, 0, 0)
oTS = Owned(TS, False, False, 0, 0, 0, 0, 0)
oLS = Owned(LS, False, False, 0, 0, 0, 0, 0)
oCS = Owned(CS, False, False, 0, 0, 0, 0, 0)
oP = Owned(P, False, False, 0, 0, 0, 0, 0)
oRS = Owned(RS, False, False, 0, 0, 0, 0, 0)
oOS = Owned(OS, False, False, 0, 0, 0, 0, 0)
oBdS = Owned(BdS, False, False, 0, 0, 0, 0, 0)
oPL = Owned(PL, False, False, 0, 0, 0, 0, 0)
oMF = Owned(MF, False, False, 0, 0, 0, 0, 0)

KCS = Stations("King's Cross Station", 200, 25, 50, 100, 200, 100)
MLB = Stations("Marylebone Station", 200, 25, 50, 100, 200,100)
FCH = Stations("Fenchurch St. Station", 200, 25, 50, 100, 200, 100)
LIV = Stations("Liverpool St. Station", 200, 25, 50, 100, 200, 100)

oKCS = StationsOwned(KCS, False, 0, 0, 0, 0)
oMLB = StationsOwned(KCS, False, 0, 0, 0, 0)
oFCH = StationsOwned(KCS, False, 0, 0, 0, 0)
oLIV = StationsOwned(KCS, False, 0, 0, 0, 0)




print(oPL.property.two)
print(oPL.bought)

print(oCS.bought)

oCS.bought = False

print(oCS.bought)

player1 = Player("Player 1", 1500)
player2 = Player("Player 2", 1500)
player3 = Player("Player 3", 1500)
player4 = Player("Player 4", 1500)

if oCS.bought == True:
    print(player1.money)
    player1.money = player1.money - CS.rent
    print(player1.money)
else:
    print(player1.money)
    buy = input("Would you like to buy Coventry Street? ")
    if buy.lower() in ["yes", "y", "Y", "YES"]:
        oCS = True
        print(player1.money)
        player1.money = player1.money - CS.cost
        print(player1.money)
        print(CS.cost)
    else:
        pass


if not board[1].is_owned():
    if player1.money >= board[1].cost:
        print(player1.money)
        player1.money = player1.money - board[1].cost
        print(player1.money)
        player1.places_owned.append(board[1].name)
        board[1].owner = player1.name
        print("You own Old Kent Road!")
        print(player1.money)

    else:
        player1.money = player1.money - board[1].rent
        print(player1.money)
else:
    print("Someone's got Old Kent Road mate!")
    print(player1.money)
    player1.money = player1.money - board[1].rent
    print(player1.money)









































# Monopoly.py with buy, rent and auction for both properties and stations. Early position change as well


import random


class Player:
#    def __init__(self,name,money,double,in_jail):
    def __init__(self,name,money,position):
        self.name = name
        self.money = money
        self.position = position
        #self.double = double
        #self.jail = in_jail
        self.places_owned = []


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


def dice():
    dice_roll = random.randint(1,6)
    dice_roll_2 = random.randint(1, 6)
    roll_result = dice_roll + dice_roll_2

    return dice_roll, dice_roll_2, roll_result


board = [
    Property("Go", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
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

Go = Owned(False, False, 0, 0, 0, 0, 0)  #change OKR etc. to p1, p2 etc. then call them p[number]
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

pos = 0
result = dice()

print("Dice 1 is: ", result[0])
print("Dice 2 is: ", result[1])
print("Roll is: ", result[2])

if result[0] == result[1]:
    print("Double!")
else:
    pass

print("Player 1 current position: " + str(pos))

pos = pos + result[2]

print("Player 1 new position: " + str(pos))

num = 0
snum = 0

p = [Go, OKR, WC, TAI, ER, PR, PM, WH, NA, BoS, MS, VS, S, FS, TS, LS, CS, P, RS, OS, BdS, PL, MF]
s = [KCS, MLB, FCH, LIV]
if pos == 1:
    num = 1         #Old Kent Road
elif pos == 3:
    num = 2         #Whitechapel Road
elif pos == 6:
    num = 3         #The Angel, Islington
elif pos == 8:
    num = 4         #Euston Road
elif pos == 9:
    num = 5         #Pentonville Road
elif pos == 11:
    num = 6         #Pall Mall
elif pos == 13:
    num = 7         #Whitehall
elif pos == 14:
    num = 8         #Northumberland Avenue
elif pos == 16:
    num = 9         #Bow Street
elif pos == 18:
    num = 10        #Marlborough Street
elif pos == 19:
    num = 11        #Vine Street
elif pos == 21:
    num = 12        #Strand
elif pos == 23:
    num = 13        #Fleet Street
elif pos == 24:
    num = 14        #Trafalgar Square
elif pos == 26:
    num = 15        #Leicester Square
elif pos == 27:
    num = 16        #Coventry Street
elif pos == 29:
    num = 17        #Piccadilly
elif pos == 31:
    num = 18        #Regent Street
elif pos == 32:
    num = 19        #Oxford Street
elif pos == 34:
    num = 20        #Bond Street
elif pos == 37:
    num = 21        #Park Lane
elif pos == 39:
    num = 22        #Mayfair

if pos == 5:
    snum = 0         #King's Cross Station
elif pos == 15:
    snum = 1         #Marylebone Station
elif pos == 25:
    snum = 2         #Fenchurch Station
elif pos == 35:
    snum = 3         #Liverpool St. Station

player1 = Player("Player 1", 1500, 0)
player2 = Player("Player 2", 1500, 0)
player3 = Player("Player 3", 1500, 0)
player4 = Player("Player 4", 1500, 0)

#print(PL.bought)

#print(CS.bought)



#p[num].bought = False
#p[2].bought = False
#print(p[num].bought)
#print(WC.bought)

#print(CS.bought)


#if p[num].bought == True:
#    print(player1.money)
#    print("A player already owns " + board[1].name + ". You owe this player £" + str(board[1].rent) + " in rent.")
#    player1.money = player1.money - board[1].rent
#    print(player1.money)
#else:
#    print(player1.money)
#    print(p[num].bought)
#    buy = input("Would you like to buy " + board[1].name + "? ")
#    if buy.lower() in ["yes", "y", "Y", "YES"]:
#        p[num].bought = True
#        print(p[num].bought)
#        print(player1.money)
#        player1.money = player1.money - board[1].cost
#        print("You now own " + board[1].name + "!")
#        print(player1.money)
#        print(board[1].name)
#        print(board[1].cost)
#        player1.places_owned.append(board[1].name)
#        print(player1.places_owned)

#    else:
#        pass


#p[num].bought = False
#print(p[num].bought)

#print(CS.bought)



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