# A list of types of coffee that can be bought on a menu
menu = ["Americano", "Mocha", "Latte", "Capuccino", "Macchiato", "Espresso"]

# Dictionary showing the price to buy one of each of the coffees on the menu
price = {"Americano": 3.03, "Mocha": 3.84, "Latte": 3.36, "Capuccino": 2.25, "Macchiato": 4.17, "Espresso": 1.95}
# Dictionary showing the stock of each coffee types that the café has available to sell
stock = {"Americano": 120, "Mocha": 160, "Latte": 240, "Capuccino": 200, "Macchiato": 360, "Espresso": 180}

# The variable to store the total value of coffee to sell is initialised to zero
total_stock = 0
# Loops through the menu and takes the price and stock value of each iteration of the menu list
for key in menu:
    # The total amount of money that the café can make if all items are sold by multiplying the price of one cup by the
    # total stock of that coffee type
    item_value = price[key] * stock[key]
    print(f"The total value for {key} is : £{price[key]} * {stock[key]} = £\
{item_value:.2f}")
    # the total stock is cumulatively increased by adding the item_value totals together to give how much value there
    # is in their total stock
    total_stock = total_stock + item_value
print(f"The total stock value the cafe has is £{total_stock:.2f}")