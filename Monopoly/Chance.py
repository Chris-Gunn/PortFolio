import random
No_Users = 2
Get_Out_Of_Jail_Free_Cards = 1
user_1_jail = 0
Houses = 4
Hotels = 2
user_1 = 2000
user_2 = 2000
user_1_pos = 7

def advance_to_go():
    global user_1
    global user_1_pos
    user_1 = user_1 + 200
    user_1_pos = 0
    print("Advance to Go (Collect £200)")
    print(user_1)
    print(user_1_pos)
    return user_1

#advance_to_go()

def Advance_to_Trafalgar():
    global user_1_pos
    user_1_pos = 24
    print("Advance to Trafalgar Square. If you pass Go, collect £200")
    print(user_1_pos)
    return user_1_pos

#Advance_to_Trafalgar()

def Advance_to_Mayfair():
    global user_1_pos
    user_1_pos = 39
    print("Advance to Mayfair. If you pass Go, collect £200")
    print(user_1_pos)
    return user_1_pos

#Advance_to_Mayfair()

def Advance_to_Pall_Mall():
    global user_1_pos
    user_1_pos = 11
    print("Advance to Pall Mall. If you pass Go, collect £200")
    print(user_1_pos)
    return user_1_pos

#Advance_to_Pall_Mall()

def Advance_to_Station():
    global user_1_pos
    if user_1_pos == 7:
        user_1_pos = 15
        print("You have landed on Marylebone Station")
    elif user_1_pos == 22:
        user_1_pos = 25
        print("You have landed on Fenchurch St. Station")
    elif user_1_pos == 36:
        user_1_pos = 5
        print("You have landed on Kings Cross Station")
    return user_1_pos

#Advance_to_Station()

def Advance_to_Utility():
    global user_1_pos
    if user_1_pos == 22:
        user_1_pos = 28
        print("You have landed on Water Works")
    elif user_1_pos == 7 or 36:
        user_1_pos = 12
        print("You have landed on Electric Company")
    return user_1_pos

#Advance_to_Utility()


def Bank_Divedend():
    global user_1
    user_1 = user_1 + 50
    print("Bank pays you dividend of £50")
    print(user_1)
    return user_1

#Bank_Divedend()

def Get_Out_Of_Jail():
    global user_1_pos
    global dice_roll
    global dice_roll_2
    dice_roll = random.randint(1,6)
    dice_roll_2 = random.randint(1, 6)
    roll_result = dice_roll + dice_roll_2
    user_1_pos = user_1_pos + (roll_result)
    print("Roll is: " + str(dice_roll))
    print("Roll is: " + str(dice_roll_2))
    print("Roll is: " + str(roll_result))
    return user_1_pos
    return dice_roll
    return dice_roll_2

#Get_Out_Of_Jail()

def Get_Out_Of_Jail_Free():
    global user_1_jail
    user_1_jail = user_1_jail + Get_Out_Of_Jail_Free_Cards
    print("You have received a Get Out Of Jail Free Card")
    print(user_1_jail)
    return user_1_jail

#Get_Out_Of_Jail_Free()

def Go_Back_Three_Spaces():
    global user_1_pos
    user_1_pos = user_1_pos - 3
    print("Go Back Three Spaces.")
    print(user_1_pos)
    return user_1_pos

#Go_Back_Three_Spaces()


def Go_To_Jail():
    global user_1_pos
    user_1_pos = 30
    print("Go To Jail. Go directly to Jail, do not pass Go, do not collect £200.")
    print(user_1_pos)
    return user_1_pos

#Go_To_Jail()


def Make_General_Repairs():
    global user_1
    user_1 = user_1 - (Houses*25) - (Hotels*100)
    print("Make general repairs on all your property. For each house pay £25. For each hotel pay £100")
    print(user_1)
    return user_1

#Make_General_Repairs()


def Speeding_Fine():
    global user_1
    user_1 = user_1 - 15
    print("Speeding fine, £15.")
    print(user_1)
    return user_1

#Speeding_Fine()


def Advance_to_Kings_Cross():
    global user_1_pos
    global user_1
    if user_1_pos > 5:
        user_1 = user_1 + 200
    user_1_pos = 5
    print("Advance to Kings Cross Station. If you pass Go, collect £200")
    print(user_1)
    print(user_1_pos)
    return user_1_pos

#Advance_to_Kings_Cross()


def Chairman_Of_The_Board():
    global user_1
    global user_2
    user_1 = user_1 - (50*(No_Users-1))
    user_2 = user_2 + 50
    print("You have been elected Chairman of the Board. Pay each player £50.")
    print(user_1)
    print(user_2)
    return user_1
    return user_2

#Chairman_Of_The_Board()

def Loan_Matures():
    global user_1
    user_1 = user_1 + 150
    print("Your building loan matures. Collect £150.")
    print(user_1)
    return user_1

#Loan_Matures()




#



#Advance_to_Trafalgar()

#print(user_1)

#Advance_to_Utility()




















import random

items = ["Advance to Go", "Advance to Mayfair", "Advance to Pall Mall", "Advance to the nearest Station",
         "Advance to Trafalgar Square", "Advance to Utility", "Bank Dividend", "Get out of jail free",
         "Go back three spaces", "Go to jail", "Make General Repairs", "Speeding Fine",
         "Advance to King's Cross Station", "Chairman of the Board", "Loan Matures"]

def remove_random_item():
    if not items:  # Check if the list is empty
        refill_items()  # Refill the list
    random_item = random.choice(items)
    if random_item == "Advance to Go":
        print("Advance to Go is gone")
    elif random_item == "Advance to Mayfair":
        print("Advance to Mayfair is gone")
    elif random_item == "Advance to Pall Mall":
        print("Advance to Pall Mall is gone")
    elif random_item == "Advance to the nearest Station":
        print("Advance to the nearest Station is gone")
    elif random_item == "Advance to Trafalgar Square":
        print("Advance to Trafalgar Square is gone")
    elif random_item == "Advance to Utility":
        print("Advance to Utility is gone")
    elif random_item == "Bank Dividend":
        print("Bank Dividend is gone")
    elif random_item == "Get out of jail free":
        print("Get out of jail free is gone")
    elif random_item == "Go back three spaces":
        print("Go back three spaces is gone")
    elif random_item == "Go to jail":
        print("-Go to jail is gone")
    elif random_item == "Make General Repairs":
        print("Make General Repairs is gone")
    elif random_item == "Speeding Fine":
        print("Speeding Fine is gone")
    elif random_item == "Advance to King's Cross Station":
        print("Advance to King's Cross Station is gone")
    elif random_item == "Chairman of the Board":
        print("Chairman of the Board is gone")
    elif random_item == "Loan Matures":
        print("Loan Matures is gone")
    items.remove(random_item)
    print("You have removed: " + random_item)
    return random_item


def refill_items():
    global items
    items = ["Advance to Go!", "Advance to Mayfair!", "Advance to Pall Mall!", "Advance to the nearest Station!",
             "Advance to Trafalgar Square!", "Advance to Utility", "Bank Dividend", "Get out of jail free",
             "Go back three spaces", "Go to jail", "Make General Repairs", "Speeding Fine",
             "Advance to King's Cross Station", "Chairman of the Board", "Loan Matures"]

# Example usage
print("Initial List:", items)

remove_random_item()

print("Updated List: ", items)

remove_random_item()

print("Updated List: ", items)

remove_random_item()

print("Updated List: ", items)

remove_random_item()

print("Updated List: ", items)

remove_random_item()

print("Updated List: ", items)

remove_random_item()

print("Updated List: ", items)

remove_random_item()

print("Updated List: ", items)

remove_random_item()

print("Updated List: ", items)

remove_random_item()

print("Updated List: ", items)

remove_random_item()

print("Updated List: ", items)

remove_random_item()

print("Updated List: ", items)

remove_random_item()

print("Updated List: ", items)

remove_random_item()

print("Updated List: ", items)

remove_random_item()

print("Updated List: ", items)

remove_random_item()

print("Updated List: ", items)

remove_random_item()

print("Updated List: ", items)