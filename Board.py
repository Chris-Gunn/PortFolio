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


board = [
    Property("Go", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    Property("Old Kent Road", 50, 2, 4, 10, 30, 90, 160, 250, 50, 50),
    Property("Whitechapel Road", 60, 4, 8, 20, 60, 180, 320, 450, 50, 50),
    Property("TheAngel, Islington", 100, 6, 12, 30, 90, 270, 400, 550, 50, 50),
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
    #Property("King's Cross Station", 200, 50, 10, 30, 90, 160, 250, 50, 50),
]

Board_Owned = [
    Owned("Go", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    Owned("Old Kent Road", 50, 2, 4, 10, 30, 90, 160, 250, 50, 50),
    Owned("Whitechapel Road", 60, 4, 8, 20, 60, 180, 320, 450, 50, 50),
    Owned("TheAngel, Islington", 100, 6, 12, 30, 90, 270, 400, 550, 50, 50),
    Owned("Euston Road", 100, 6, 12, 30, 90, 270, 400, 550, 50, 50),
    Owned("Pentonville Road", 120, 8, 16, 40, 100, 300, 450, 600, 50, 50),
    Owned("Pall Mall", 140, 10, 20, 50, 150, 450, 625, 750, 100, 100),
    Owned("Whitehall", 140, 10, 20, 50, 150, 450, 625, 750, 100, 100),
    Owned("Northumberland Avenue", 160, 12, 24, 60, 180, 500, 700, 900, 100, 100),
    Owned("Bow Street", 180, 14, 28, 70, 200, 550, 750, 950, 100, 100),
    Owned("Marlborough Street", 180, 14, 28, 70, 200, 550, 750, 950, 100, 100),
    Owned("Vine Street", 200, 16, 32, 80, 220, 600, 800, 1000, 100, 100),
    Owned("Strand", 220, 18, 36, 90, 250, 700, 875, 1050, 150, 150),
    Owned("Fleet Street", 220, 18, 36, 90, 250, 700, 875, 1050, 150, 150),
    Owned("Trafalgar Square", 240, 20, 40, 100, 300, 750, 925, 1100, 150, 150),
    Owned("Leicester Square", 260, 22, 44, 110, 330, 800, 975, 1150, 150, 150),
    Owned("Coventry Street", 260, 22, 44, 110, 330, 800, 975, 1150, 150, 150),
    Owned("Piccadilly", 280, 24, 48, 120, 360, 850, 1025, 1200, 150, 150),
    Owned("Regent Street", 300, 26, 52, 130, 390, 900, 1100, 1275, 200, 200),
    Owned("Oxford Street", 300, 26, 52, 130, 390, 900, 1100, 1275, 200, 200),
    Owned("Bond Street", 320, 28, 56, 150, 450, 1000, 1200, 1400, 200, 200),
    Owned("Park Lane", 350, 35, 70, 175, 500, 1100, 1300, 1500, 200, 200),
    Owned("Mayfair", 400, 50, 100, 200, 600, 1400, 1700, 2000, 200, 200),
    #Owned("King's Cross Station", 200, 50, 10, 30, 90, 160, 250, 50, 50),
]


player1 = Player("Player 1", 1500)
player2 = Player("Player 2", 1500)

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

print(board[1].rent)
print(player1.places_owned)
