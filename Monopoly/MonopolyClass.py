class Space:

    def __init__(self,name,buy,rent,set,one,two,three,four,hotel,CoH,mortgage):
        self.name = name
        self.buy = buy
        self.rent = rent
        self.set = set
        self.one = one
        self.two = two
        self.three = three
        self.four = four
        self.hotel = hotel
        self.CoH = CoH
        self.mortgage = mortgage

OKR = Space('Old Kent Road', 100, 2, 4, 10, 30, 90, 160, 250, 50, 50)
WR = Space('Whitechapel Road', 100, 4, 8, 20, 60, 180, 320, 450, 50, 50)
TAI = Space('The Angel, Islington', 100, 6, 12, 30, 90, 270, 400, 550, 50, 50)
ER = Space('Euston Road', 100, 6, 12, 30, 90, 270, 400, 550, 50, 50)
PR = Space('Pentonville Road', 100, 8, 16, 40, 100, 300, 450, 600, 50, 50)
PM = Space('Pall Mall', 100, 10, 20, 50, 150, 450, 625, 750, 100, 100)
W = Space('Whitehall', 100, 10, 20, 50, 150, 450, 625, 750, 100, 100)
NA = Space('Northumberland Avenue', 100, 12, 24, 60, 180, 500, 700, 900, 100, 100)
BS = Space('Bow Street', 100, 14, 28, 70, 200, 550, 750, 950, 100, 100)
MS = Space('Marlborough Street', 100, 14, 28, 70, 200, 550, 750, 950, 100, 100)
VS = Space('Vine Street', 100, 16, 32, 80, 220, 600, 800, 1000, 100, 100)
S = Space('Strand', 100, 18, 36, 90, 250, 700, 875, 1050, 150, 150)
FS = Space('Fleet Street', 100, 18, 36, 90, 250, 700, 875, 1050, 150, 150)
TS = Space('Trafalgar Square', 100, 20, 40, 100, 300, 750, 925, 1100, 150, 150)
LS = Space('Leicester Square', 100, 22, 44, 110, 330, 800, 975, 1150, 150, 150)
CS = Space('Coventry Street', 100, 22, 44, 110, 330, 800, 975, 1150, 150, 150)
P = Space('Piccadilly', 100, 24, 48, 120, 360, 850, 1025, 1200, 150, 150)
RS = Space('Regent Street', 100, 26, 52, 130, 390, 900, 1100, 1275, 200, 200)
OS = Space('Oxford Street', 100, 26, 52, 130, 390, 900, 1100, 1275, 200, 200)
BS = Space('Bond Street', 100, 28, 56, 150, 450, 1000, 1200, 1400, 200, 200)
PL = Space('Park Lane', 100, 35, 70, 175, 500, 1100, 1300, 1500, 200, 200)
M = Space('Mayfair', 100, 50, 100, 200, 600, 1400, 1700, 2000, 200, 200)

class Stations:
    def __init__(self,name,buy,rent,two,three,four):
        self.name = name
        self.buy = buy
        self.rent = rent
        self.two = two
        self.three = three
        self.four = four

KCS = Stations('Kings Cross Station', 200, 25, 50, 100, 200)
MBS = Stations('Marylebone Station', 200, 25, 50, 100, 200)
FSS = Stations('Fenchurch Street Station', 200, 25, 50, 100, 200)
LSS = Stations('Liverpool Street Station', 200, 25, 50, 100, 200)

x = 2000 - KCS.buy

y = KCS.buy

print(x)

