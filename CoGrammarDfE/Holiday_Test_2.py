'''
Function that takes the city which the user would like to go to as an input and outputs the cost of the flight ticket
depending on where they were going.
'''
def plane_cost(city_flight):
    ticket_cost = 0  # ticket_cost variable is initialised to 0
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


'''
Function that takes the star rating of the hotel which the user would like to stay as an input, and outputs the price
of the stay by multiplying the number of nights of the stay by the cost per night related to the star rating.
'''
def hotel_cost(hotel_nights, hotel_star):
    night_cost = 0 # night_cost variable initialised to 0
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


'''
Function that takes the number of days which the user would like to hire a car and the make of the car as an input, 
and outputs the total rental cost of the car by multiplying the number of days they'd like the car by the cost per day
related to the make of the car.
'''
def car_rental(car_days, car_make):
    rental_cost = 0 # rental_cost variable initialised to 0
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

'''
Function that takes the costs from the flight, hotel and car rental and sums them together to get the total cost of the 
holiday
'''
def holiday_cost(hotel, plane, car):
    holiday = hotel + plane + car
    return holiday


print("Welcome to the Package Holiday Planner\n"
      "")

# User input to choose where they are going
while True:
    city_flight = input("Where are you flying to? Please select from the menu:\n"
                        "Paris\n"
                        "Berlin\n"
                        "Milan\n"
                        "New York\n"
                        "Tokyo\n").lower()
# if the user inputs one of the below strings, the choice is validated and breaks out of the loop
    if city_flight in ("paris", "p", "par", "berlin", "b", "ber", "milan", "m", "mil", "new york", "n", "ny", "tokyo",
                       "t", "tok"):
        break
# If one of the strings isn't typed by the user, it is invalid and will have to try again until it is a valid choice
    else:
        print("This is an invalid selection. Please choose again.\n")

# User input to choose what quality of hotel they would like
while True:
    # If a number between 1 and 5 is chosen, stores the star rating and breaks out of the loop
    try:
        hotel_star = int(input("What hotel package would you like? Choose your star rating (1-5): "))
        if hotel_star in range(1, 6):
            break
        else:
            print("This is not an available star rating. Please choose again.\n")
    # If a number wasn't chosen, it loops back and the user has to enter a number again
    except ValueError:
        print("You haven't entered a valid number. Please choose again.\n")

# User input to choose how long they would like to stay at the hotel
while True:
    try:
        hotel_nights = int(input("How many nights do you wish to stay at your hotel?: "))
        break
    # If a number wasn't chosen, it loops back and the user has to enter a number again
    except ValueError:
        print("You haven't entered a valid number. Please choose again.\n")


# User input to choose what make of car they would like
while True:
    car_make = input("What car would you like to hire? \n"
                     "Select from the available cars:\n"
                     "Ford \n"
                     "Volkswagen \n"
                     "Jaguar \n"
                     "Mercedes \n"
                     "Ferrari\n").lower()

    # if the user inputs one of the below strings, the choice is validated and breaks out of the loop
    if car_make in ("ford", "f", "for", "volkswagen", "v", "vol", "jaguar", "j", "jag", "mercedes", "m", "mer",
                    "ferrari", "f", "fer"):
        break
    # If one of the strings isn't typed by the user, it is invalid and will have to try again until it is a valid choice
    else:
        print("This is an invalid selection. Please choose again.\n")

# User input to choose how long they'd like the rental car
while True:
    try:
        car_days = int(input("For how many days do you wish to hire the rental car?: "))
        break
    # If a number wasn't chosen, it loops back and the user has to enter a number again
    except ValueError:
        print("You haven't entered a valid number of days. Please choose again.\n")

# plane_cost function called and stored as the variable plane
plane = plane_cost(city_flight)
print("")
print(f"Your flight ticket will cost: £{plane}")

# hotel_cost function called and stored as the variable hotel
hotel = hotel_cost(hotel_nights, hotel_star)
print(f"Your stay at your hotel will cost: £{hotel}")

# car_rental function called and stored as the variable car
car = car_rental(car_days, car_make)
print(f"Your car rental will cost: £{car}")

# holiday_cost function called and stored as the variable total
total = holiday_cost(hotel, plane, car)
print(f"Your total cost for your holiday will be: £{total}")

