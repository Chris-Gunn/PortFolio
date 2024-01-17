class Player:
#    def __init__(self,name,money,double,in_jail):
    def __init__(self,name,money,position):
        self.name = name
        self.money = money
        self.position = position
        #self.double = double
        #self.jail = in_jail
        self.places_owned = []

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

    Stations("King's Cross Station", 200, 25, 50, 100, 200, 100),
    Stations("Marylebone Station", 200, 25, 50, 100, 200, 100),
    Stations("Fenchurch St. Station", 200, 25, 50, 100, 200, 100),
    Stations("Liverpool St. Station", 200, 25, 50, 100, 200, 100)
]


player1 = Player("Player 1", 1500, 0)
player2 = Player("Player 2", 1500, 0)
player3 = Player("Player 3", 1500, 0)
player4 = Player("Player 4", 1500, 0)

KCS = StationsOwned(True, 0, 0, 0, 0)
MLB = StationsOwned(True, 1, 1, 1, 0)
FCH = StationsOwned(True, 1, 1, 1, 0)
LIV = StationsOwned(True, 1, 1, 1, 0)

pos = 5
num = 0
snum = 0

s = [KCS, MLB, FCH, LIV]

if pos == 5:
    snum = 0         #King's Cross Station
elif pos == 15:
    snum = 1         #Marylebone Station
elif pos == 25:
    snum = 2         #Fenchurch Station
elif pos == 35:
    snum = 3         #Liverpool Street Station


if s[snum].bought == True:
    if s[snum].one == 1:
        if s[snum].two == 1:
            if s[snum].three == 1:
                if s[snum].four == 1:

                    print(player1.money)
                    print("A player owns " + board[snum].name + " and the other three stations. You owe this player "  
                            "£" +str(board[snum].four) + " in rent.")
                    player1.money = player1.money - board[snum].four
                    print(player1.money)
                else:
                    print(player1.money)
                    print("A player owns " + board[snum].name + " and two other stations. You owe this player "
                        "£" + str(board[snum].three) + " in rent.")
                    player1.money = player1.money - board[snum].three
                    print(player1.money)
            else:
                print(player1.money)
                print("A player owns " + board[snum].name + " and one other station. You owe this player £" + str(
                    board[snum].two) + " in rent.")
                player1.money = player1.money - board[snum].two
                print(player1.money)
        else:
            print(player1.money)
            print("A player owns " + board[snum].name + ". You owe this player £" + str(
                board[snum].rent) + " in rent.")
            player1.money = player1.money - board[snum].rent
            print(player1.money)
else:
    print("Player 1 balance is:" + str(player1.money))
    # print(p[snum].bought)
    buy = input("Would you like to buy " + board[snum].name + "? ")
    if buy.lower() in ["yes", "y", "Y", "YES"]:
        s[snum].bought = True
        print("Player 1 has payed " + "£" + str(board[snum].cost) + " for " + str(board[snum].name))
        player1.money = player1.money - board[snum].cost
        print("You now own " + board[snum].name + "!")
        print("Player 1 new balance is: " + str(player1.money))
        player1.places_owned.append(board[snum].name)
        print(player1.places_owned)

    elif buy.lower() in ["no", "n", "N", "NO"]:
        print("This property will be sent to auction!")
        print("Welcome to the Auction House!!!")
        print(board[snum].name + " is up for grabs! How exciting!!")
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
                bid1 = input("Player 1, would you like to bid for " + board[snum].name + "? ")
                if bid1.lower() in ["yes", "y", "Y", "YES"]:
                    bid = bid + int(input("Player 1 has bid: "))
                    print(bid)
                else:
                    auction1 = False
                    sold -= 1
                    gavel1 = 0
                    print("Player 1 is out of the bidding!")
            if gavel2 == 1:
                bid2 = input("Player 2, would you like to bid for " + board[snum].name + "? ")
                if bid2.lower() in ["yes", "y", "Y", "YES"]:
                    bid = bid + int(input("Player 2 has bid: "))
                    print(bid)
                else:
                    auction2 = False
                    sold -= 1
                    gavel2 = 0
                    print("Player 2 is out of the bidding!")
            if gavel3 == 1:
                bid3 = input("Player 3, would you like to bid for " + board[snum].name + "? ")
                if bid3.lower() in ["yes", "y", "Y", "YES"]:
                    bid = bid + int(input("Player 3 has bid: "))
                    print(bid)
                else:
                    auction3 = False
                    sold -= 1
                    gavel3 = 0
                    print("Player 3 is out of the bidding!")
            if gavel4 == 1:
                bid4 = input("Player 4, would you like to bid for " + board[snum].name + "? ")
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
            player1.places_owned.append(board[snum].name)
            print("Player 1 Properties: " + str(player1.places_owned))
            s[snum].bought = True

        elif auction2:
            print("Player 2's")
            print(bid)
            player2.money = player2.money - bid
            print(player2.money)
            player2.places_owned.append(board[snum].name)
            print("Player 2 Properties: " + str(player2.places_owned))
            s[snum].bought = True

        elif auction3:
            print("Player 3's")
            print(bid)
            player3.money = player3.money - bid
            print(player3.money)
            player3.places_owned.append(board[snum].name)
            print("Player 3 Properties: " + str(player3.places_owned))
            s[snum].bought = True

        elif auction4:
            print("Player 4's")
            print(bid)
            player4.money = player4.money - bid
            print(player4.money)
            player4.places_owned.append(board[snum].name)
            print("Player 4 Properties: " + str(player4.places_owned))
            s[snum].bought = True
