# Store four values of different types into four separate variables
num1 = 99.23
num2 = 23
num3 = 150
string1 = "100"

# Print the current value and type of 'num1' using the format method
print("num1 = {}.".format(num1))
print("num1: {}.".format(type(num1)))
# Convert 'num1' into an integer
num1 = int(num1)
# Print the new type of 'num1'
print("num1 converted: {}.".format(type(num1)))
print("")

# Print the current value and type of 'num2' using the format method
print("num2 = {}.".format(num2))
print("num2: {}.".format(type(num2)))
# Convert 'num2' into a float
num2 = float(num2)
# Print the new type of 'num2'
print("num2 converted: {}.".format(type(num2)))
print("")

# Print the current value and type of 'num3' using the format method
print("num3 = {}.".format(num3))
print("num3: {}.".format(type(num3)))
# Convert 'num3' into a string
num3 = str(num3)
# Print the new type of 'num3'
print("num3 converted: {}.".format(type(num3)))
print("")

# Print the current value and type of 'string1' using the format method
print("string1 = {}.".format(string1))
print("string1: {}.".format(type(string1)))
# Convert 'string1' into an integer
string1 = int(string1)
# Print the new type of 'string1'
print("string1 converted: {}.".format(type(string1)))
print("")
