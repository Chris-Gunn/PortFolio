def hotel_cost(num_nights, night_cost, hotel):
    if hotel == 1:
        night_cost = 40
    elif hotel == 2:
        night_cost = 60
    elif hotel == 3:
        night_cost = 80
    elif hotel == 4:
        night_cost = 100
    elif hotel == 5:
        night_cost = 120
    total_cost = night_cost * num_nights
    return total_cost


def plane_cost(city_flight, ticket_cost):
    if city_flight == "Paris":
        ticket_cost = 43
    elif city_flight == "Berlin":
        ticket_cost = 60
    elif city_flight == "Milan":
        ticket_cost = 54
    elif city_flight == "Florida":
        ticket_cost = 612
    elif city_flight == "Sydney":
        ticket_cost = 1843
    return ticket_cost


def car_rental(rental_days, rental_cost, car_make):

    if car_make == "ford":
        rental_cost = 50 * rental_days
    elif car_make == "volkswagen":
        rental_cost = 75 * rental_days
    elif car_make == "mercedes":
        rental_cost = 100 * rental_days
    elif car_make == "ferrari":
        rental_cost = 300 * rental_days
    print("Your total rental cost is: " + str(rental_cost))
    return rental_cost


def holiday_cost(stay, plane, car):
    holiday = stay + plane + car
    print(f"The total cost of the holiday is £{holiday}")


night_cost = 0
ticket_cost = 0
rental_cost = 0

city_flight = input("Where are you flying to? \n"
                    "Select from the available destinations:\n"
                    "Paris, Berlin, Milan, Florida, Sydney\n")

num_nights = int(input("How many nights do you wish to stay at your hotel?: "))

hotel = input("What hotel package would you like? Choose your star rating (1-5): ")

rental_days = int(input("For how many days do you wish to hire the rental car?: "))

car_make = input("What car would you like to hire? \n "
                "Select from the available cars:\n"
                "Ford, Volkswagen, Mercedes, Ferrari\n").lower()

car = car_rental(rental_days, rental_cost, car_make)
print(f"Car: {car}")

plane = plane_cost(city_flight, ticket_cost)
print(f"Plane: {plane}")

stay = hotel_cost(num_nights, night_cost, hotel)
print(f"Hotel: {stay}")

holiday_cost(stay, plane, car)

