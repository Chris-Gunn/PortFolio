import random
No_Users = 2
user_1_money = 2000
user_2_money = 2000
Houses = 6
Hotels = 1
user_1_pos = 0
Get_Out_Of_Jail_Free_Cards = 1
user_1_jail = 0


def Advance_To_Go_Community():
    global user_1_money
    global user_1_pos
    user_1_money = user_1_money + 200
    user_1_pos = 0
    print("Advance to Go (Collect £200)")
    print(user_1_money)
    print(user_1_pos)
    return user_1_money
    return user_1_pos

#Advance_To_Go_Community()

def Bank_Error():
    global user_1_money
    user_1_money = user_1_money + 200
    print("Bank error in your favour. Collect £200")
    print(user_1_money)
    return user_1_money

#Bank_Error()

def DoctorFee():
    global user_1_money
    user_1_money = user_1_money - 50
    print("Doctors Fee. Pay £50")
    print(user_1_money)
    return user_1_money

#DoctorFee()

def Sale_Of_Stock():
    global user_1_money
    user_1_money = user_1_money + 50
    print("From sale of stock you get £50")
    print(user_1_money)
    return user_1_money

#Sale_Of_Stock()

def Get_Out_Of_Jail_Free_Community():
    global user_1_jail
    user_1_jail = user_1_jail + Get_Out_Of_Jail_Free_Cards
    print("You have received a Get Out Of Jail Free Card")
    print(user_1_jail)
    return user_1_jail

#Get_Out_Of_Jail_Free_Community()

def Get_Out_Of_Jail_Community():
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

#Get_Out_Of_Jail_Community()

def Go_To_Jail_Community():
    global user_1_pos
    user_1_pos = 30
    print("Go To Jail. Go directly to Jail, do not pass Go, do not collect £200.")
    print(user_1_pos)
    return user_1_pos

#Go_To_Jail_Community()

def Holiday_Fund_Matures():
    global user_1_money
    user_1_money = user_1_money + 100
    print("Holiday fund matures. Receive £100")
    print(user_1_money)
    return user_1_money

#Holiday_Fund_Matures()

def Tax_Refund():
    global user_1_money
    user_1_money = user_1_money + 20
    print("Income tax refund. Collect £20")
    print(user_1_money)
    return user_1_money

#Tax_Refund()

def Birthday():
    global user_1_money
    global user_2_money
    user_1_money = user_1_money + (10*(No_Users-1))
    user_2_money = user_2_money - 10
    print("It is your birthday. Collect £10 from every player")
    print(user_1_money)
    print(user_2_money)
    return user_1_money
    return user_2_money

#Birthday()

def Life_Insurance():
    global user_1_money
    user_1_money = user_1_money + 100
    print("Life insurance matures. Collect £100")
    print(user_1_money)
    return user_1_money

#Life_Insurance()

def Hospital_Fee():
    global user_1_money
    user_1_money = user_1_money - 100
    print("Pay hospital fees of £100")
    print(user_1_money)
    return user_1_money

#Hospital_Fee()

def School_Fee():
    global user_1_money
    user_1_money = user_1_money - 50
    print("Pay school fees of £50")
    print(user_1_money)
    return user_1_money

#School_Fee()

def Consultant_Fee():
    global user_1_money
    user_1_money = user_1_money + 25
    print("Receive £25 consultancy fee")
    print(user_1_money)
    return user_1_money

#Consultant_Fee()

def Street_Repairs():
    global user_1_money
    user_1_money = user_1_money - (Houses*40) - (Hotels*115)
    print("You are assessed for street repairs. £40 per house. £115 per hotel")
    print(user_1_money)
    return user_1_money

#Street_Repairs()

def Beauty_Contest():
    global user_1_money
    user_1_money = user_1_money + 10
    print("You have won second prize in a beauty contest. Collect £10")
    print(user_1_money)
    return user_1_money

#Beauty_Contest()

def Inheritance():
    global user_1_money
    user_1_money = user_1_money + 100
    print("You inherit £100")
    print(user_1_money)
    return user_1_money

#Inheritance()