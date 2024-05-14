''' # Number that the user chooses is initialised to zero
number = 0
# Sum of all the chosen numbers initialised to zero
total_sum = 0
# How many times the number is chosen before a '-1' is chosen
iterations = 0


while number >= 0:
    number = int(input("Please enter a number: "))
    if number == -1:
        break
    total_sum = total_sum + number
    iterations += 1

print(total_sum)
print(iterations)

average = total_sum/iterations
print(average)
'''

# Number that the user chooses is initialised to zero
number = 0
# Boolean to check if a negative is chosen
negative = False
# Sum of all the chosen numbers initialised to zero
total_sum = 0
# How many times the number is chosen before a '-1' is chosen
iterations = 0

# While the negative variable remains false
while not negative:
    # The user is asked to input a number
    number = int(input("Please enter a number: "))
    # if the number becomes negative, the loop is exited
    if number < 0:
        break
    # if the number remains positive, the numbers the user inputs is accumulated together
    total_sum = total_sum + number
    # The number of times the user inputs a number before a negative is chosen
    iterations += 1
# If a negative is chosen and the loop is broken, negative is set to true and ends the while loop
negative = True
# Prints the accumulated number choices
print(total_sum)
# Prints the amount of times a number is chosen before a negative
print(iterations)

average = total_sum/iterations
print(average)