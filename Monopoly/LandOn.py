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

pos = 1
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
    snum = 1         #King's Cross Station
elif pos == 15:
    snum = 2         #Marylebone Station
elif pos == 25:
    snum = 3         #Fenchurch Station
elif pos == 35:
    snum = 4         #Liverpool St. Station

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





