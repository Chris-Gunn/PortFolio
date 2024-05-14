def plane_cost(city_flight):
    ticket_cost = 0  # Default value
    if city_flight in ("paris", "p", "par"):
        ticket_cost = 43
    elif city_flight in ("berlin", "b", "ber"):
        ticket_cost = 60
    elif city_flight in ("milan", "m", "mil"):
        ticket_cost = 54
    elif city_flight in ("new york", "n", "ny"):
        ticket_cost = 612
    elif city_flight in ("tokyo", "t", "tok"):
        ticket_cost = 1843
    return ticket_cost


def hotel_cost(hotel_nights, hotel_star):
    night_cost = 0
    if hotel_star == 1:
        night_cost = 40
    elif hotel_star == 2:
        night_cost = 60
    elif hotel_star == 3:
        night_cost = 80
    elif hotel_star == 4:
        night_cost = 100
    elif hotel_star == 5:
        night_cost = 120
    hotel_price = night_cost * hotel_nights
    return hotel_price


def car_rental(car_days, car_make):
    rental_cost = 0
    if car_make in ("ford", "f", "for"):
        rental_cost = 50 * car_days
    elif car_make in ("volkswagen", "v", "vol"):
        rental_cost = 75 * car_days
    elif car_make in ("jaguar", "j", "jag"):
        rental_cost = 100 * car_days
    elif car_make in ("mercedes", "m", "mer"):
        rental_cost = 150 * car_days
    elif car_make in ("ferrari", "f", "fer"):
        rental_cost = 300 * car_days
    return rental_cost


def holiday_cost(hotel, plane, car):
    holiday = hotel + plane + car
    return holiday


city_flight = input("Where are you flying to? Please select from the menu:\n"
                    "Paris\n"
                    "Berlin\n"
                    "Milan\n"
                    "New York\n"
                    "Tokyo\n").lower()

hotel_star = int(input("What hotel package would you like? Choose your star rating (1-5): "))

hotel_nights = int(input("How many nights do you wish to stay at your hotel?: "))

car_make = input("What car would you like to hire? \n"
                 "Select from the available cars:\n"
                 "Ford \n"
                 "Volkswagen \n"
                 "Jaguar \n"
                 "Mercedes \n"
                 "Ferrari\n").lower()

car_days = int(input("For how many days do you wish to hire the rental car?: "))


plane = plane_cost(city_flight)
print(f"Your flight ticket will cost: £{plane}")

hotel = hotel_cost(hotel_nights, hotel_star)
print(f"Your stay at your hotel will cost: £{hotel}")

car = car_rental(car_days, car_make)
print(f"Your car rental will cost: £{car}")

total = holiday_cost(hotel, plane, car)
print(f"Your total cost for your holiday will be: £{total}")

