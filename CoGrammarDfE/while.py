# Number that the user chooses is initialised to zero
number = 0
# Boolean to check if a '-1' is chosen
minus_one = False
# Sum of all the chosen numbers initialised to zero
total_sum = 0
# How many times the number is chosen before a '-1' is chosen
iterations = 0

# While the minus_one variable remains false
while not minus_one:
    # The user is asked to input a number
    number = int(input("Please enter a number: "))
    # if the number becomes minus_one, the loop is exited
    if number == -1:
        break
    # if the number is not a -1, the numbers the user inputs is accumulated together
    total_sum = total_sum + number
    # The number of times the user inputs a number before a -1 is chosen
    iterations += 1
# If a '-1' is chosen and the loop is broken, minus_one is set to true and ends the while loop
minus_one = True
# Prints the accumulated number choices
print(total_sum)
# Prints the amount of times a number is chosen before a '-1'
print(iterations)

# Average divides the total accumulated numbers by the number of choices
average = total_sum/iterations
print(average)
