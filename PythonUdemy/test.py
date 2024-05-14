from Day_15_Menu import MENU, resources

profit = 0


def process_coins():
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    total = round(total, 2)
    return total


def money_sufficient(coins, selected_drink, menu):
    if coins >= menu[selected_drink]["cost"]:
        return True
    else:
        return False


def make_coffee(choice, resource):
    if choice.lower() == "latte":
        resource["water"] -= 50
        resource["milk"] -= 100
        resource["coffee"] -= 30
    # Add more conditions for other types of coffee if needed
    else:
        print("Sorry, we don't have that option.")
    print("Remaining resources:", resource)

money = process_coins()
drink = input("What would you like? (Espresso/Latte/Cappuccino): ").lower()

sufficient = money_sufficient(money, drink, MENU)
print(sufficient)
# quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01


# Example usage
make_coffee("latte", resources)










# is_on = True
#
# while is_on:
#     prompt = input("What would you like? ( (espresso/latte/cappuccino): ")
#     if prompt == "report":
#         print(resources)
#     elif prompt == "espresso":
#         print("espresso")
#     elif prompt == "latte":
#         print("latte")
#     elif prompt == "cappuccino":
#         print("cappuccino")





