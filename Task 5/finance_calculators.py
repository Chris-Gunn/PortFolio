import math

# A while loop that stays true until the user chooses to exit from the program menu
while True:
    print("""
investment - to calculate the amount of interest you'll earn on your investment
bond       - to calculate the amount you'll have to pay on a home loan
""")
    # The user chooses their preferred financial program
    program = input("Enter either 'investment' or 'bond' from the menu above to proceed or type quit or end to exit: \n").lower()
    # Prints out the users choice
    print(program)

    # Checks if the user has chosen to invest
    if program in ("investment", "invest", "i"):

        #  The 'deposit' variable stores the amount of money the user would like to invest in the program
        deposit = float(input("Please enter the amount you would like to deposit: "))

        # the 'rate' variable sets the percentage rate of interest for the user
        rate = float(input("Please enter the rate of interest you would like (exclude % symbol): "))/100
        print(rate)

        # The 'years' variable sets how long the investment will last for in years
        years = float(input("How many years do you plan on investing?: "))

        # The user chooses between simple and compound interest
        interest = input("Which type of interest would you prefer? 'Simple' or 'Compound'? ").lower()

        # Checks if the user chooses simple interest
        if interest in ('simple', 's'):
            '''
            Payout is the calculation of how much money the user will receive after the investment with 
            simple interest
            A (payout) = P (deposit) * (1 + r (rate) * t (years))
            '''
            payout = deposit * (1 + (rate * years))
            # prints the amount user will receive from simple interest
            print(payout)
            # User jumps back to the program choice input
            continue
        # Checks if the user chose compound interest
        elif interest in ('compound', 'c'):
            '''
            Payout is the calculation of how much money the user will receive after the investment with 
            compound interest
            A (payout) = P (deposit) * (1 + r (rate) )^ t (years)
            '''
            payout = deposit * math.pow((1 + rate), years)
            # Prints the amount user will receive from compound interest
            print(payout)
            # User jumps back to the program choice input
            continue
        else:
            print("Invalid selection")
            # User jumps back to the program choice input
            continue

    # Checks if the user has chosen to make a bond
    elif program in ('bond', 'b'):

        # the variable 'house_value' asks the user how much their house is worth
        house_value = float(input("What is the current value of the property?: "))

        # the variable 'interest_rate' asks the user what rate of interest they would like for the bond
        interest_rate = float(input("Please enter the rate of interest you would like? (exclude the % symbol): "))/100

        # the variable 'months' asks the user how long they would like to pay for the house with the chosen rate
        months = int(input("How many months would you like to repay the loan?: "))

        # Yearly rate interest calculated and broken into months
        interest_rate = interest_rate / 12
        # Formula to work out the loan repayment cost in months
        repayment = (interest_rate * house_value) / (1 - (1 + interest_rate) ** (-months))
        # Prints the cost to repay back the house
        print(repayment)
        # User jumps back to the program choice input
        continue

    # if the user chooses quit, they exit from choosing a financial program
    elif program in ('quit', 'q', 'end', 'e'):
        print("Exiting. . .")
        # breaks out of the loop and exits the program
        break

    else:
        # if the user fails to choose on of the possible program choices, it will come up as invalid
        print("Invalid selection")
        # User jumps back to the program choice input
        continue
