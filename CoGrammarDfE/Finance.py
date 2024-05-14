import math

while True:
    print("""
investment - to calculate the amount of interest you'll earn on your investment
bond       - to calculate the amount you'll have to pay on a home loan
""")

    program = input("Enter either 'investment' or 'bond' from the menu above to proceed or type quit or end to exit: \n").lower()
    print(program)

    if program == "investment":

        # amount, years, interest rate
        # P = The amount deposited
        deposit = float(input("Please enter the amount you would like to deposit: "))

        # r = rate of interest (%) usre shouldn't add the % symbol to input
        percentage = float(input("Please enter the rate of interest (exclude % symbol): "))/100
        print(percentage)

        # t = amount of years of investment
        years = float(input("Please enter the years for investment: "))

        interest = input("Which type of interest would you prefer? 'Simple' or 'Compound'? \n").lower()

        if interest == 'simple':
            payout = deposit * (1 + (percentage * years))
            print(payout)
            continue
        elif interest == 'compound':
            print("Compound interest")
            continue
        else:
            print("Invalid selection")
            continue

    elif program == 'bond':

        P = float(input("Enter the present value of your house: "))

        r = float(input("Please enter the rate of interest (exclude the % symbol): "))/100
        r = r/12

        t = int(input("Please enter the amount of months planned for repayment: "))

        print("Calculate bond")
        continue

    elif program == 'quit':
        print("Exiting. . .")
        break

    else:
        print("Invalid selection")
        continue
