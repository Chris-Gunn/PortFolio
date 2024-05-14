# Request the user to enter three different numbers
number1 = int(input("Please enter a number: "))
number2 = int(input("Please enter another number: "))
number3 = int(input("Please enter one more number: "))

# Calculate and print the sum of all the numbers
calc1 = number1 + number2 + number3
print(calc1)

# Calculate the first number minus the second number
calc2 = number1 - number2
print(calc2)

# Calculate the third number multiplied by the first number
calc3 = number3 * number1
print(calc3)

# Calculate the sum of all three numbers divided by the third number
# The sum is already calculated

calc4 = calc1 / number3
print(calc4)