# Class to show details of shoes
class Board:

    def __init__(self, name, cost, rent, monopoly, one_house, two_houses, three_houses, four_houses, hotel, mortgage,
                 house_cost, mortgage_cost):

        self.name = name
        self.cost = cost
        self.rent = rent
        self.monopoly = monopoly
        self.one_house = one_house
        self.two_houses = two_houses
        self.three_houses = three_houses
        self.four_houses = four_houses
        self.hotel = hotel
        self.mortgage = mortgage
        self.house_cost = house_cost
        self.mortgage_cost = mortgage_cost

    def __str__(self):

        return f"""
Country : {self.name}
Code : {self.cost}
Product : {self.rent}
Cost : {self.monopoly}
One house : {self.one_house}
Two Houses : {self.two_houses}
Three Houses : {self.three_houses}
Four Houses : {self.four_houses}
Hotel : {self.hotel}
Mortgage : {self.mortgage}
Mortgage Value : {self.mortgage_cost}
House Cost : {self.house_cost}
"""

board_data = []


def read_data():
    # reads the text file inventory.txt, more improved way of writing: file = open("inventory.txt", "r")
    with open('Monopoly_Places.txt', 'r') as file:
        for lines in file:
            data = lines.strip().split(',')
            if "Name" not in data:
                board_data.append(Board(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8],
                                        data[9], data[10], data[11]))



read_data()

