from Day_15_Menu import MENU, resources


def resources_sufficient(resource, menu):
    if resource["water"] < menu["ingredients"]["water"]:
        print(resource["water"], menu["ingredients"]["water"])
        return False
    else:
        print(resource["water"], menu["ingredients"]["water"])
        return True


def process_coins():
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    total = round(total, 2)
    return total


def transaction_successful(coins, price):
    if coins >= price:
        return True
    else:
        return False

def make_coffee(choice, resource):
    
# insert_coins = process_coins()
# print(insert_coins)
#
# ingredient = resources
#
# sufficient = resources_sufficient(resources, MENU["latte"])
# print(sufficient)

profit = 0

while True:
    prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if prompt == "report":
        print(resources)
    elif prompt == "latte":
        latte_sufficient = resources_sufficient(resources, MENU["latte"])
        if latte_sufficient:
            latte_coins = process_coins()
            if transaction_successful(latte_coins, MENU["latte"]["cost"]):


        # print(MENU["latte"])
    elif prompt == "cappuccino":
        print(MENU["cappuccino"])
    elif prompt == "espresso":
        print(MENU["espresso"])
    elif prompt == "off":
        break
    else:
        print("That is an invalid choice. Please choose again!")
        continue
