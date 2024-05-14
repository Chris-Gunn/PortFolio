string = "Coffee"

# For every iteration of string, char takes on the value of the
# iteration.
# The number of iterations is dependent on the length of string
# (In characters)

#In this case, the first is 'C'
for char in string:
    print(char)
print("")
print("")

# When printing string, the iteration will print the entire string
# The amount of times is dependent on the length of 'string' in char
for char in string:
    print(string)
print("")
print("")
# This one will be the same as the previous but prints
# 'Hey, dude' the number of characters 'string' has
for char in string:
    print("Hey, dude!")


x = 10

for item in range(x):
    print(x)

x = 10

for item in range(x):
    print(item)

# Leap year

start_year = int(input("Enter the starting year: \n"))
end_year = int(input("Enter the ending year: \n"))
count_leap = 0

for leap in range(start_year, end_year):

    if leap % 4 == 0:
        print(f"{leap} is a leap year")
        count_leap += 1

    else:
        continue
print(f"There have been {count_leap} in this period of time")

"""    else:
        print(f"{leap} is not a leap year")
"""

table = int(input("Enter the number of the desired times table: "))

for times in range(1, 13):
    print(f"{table} times {times} is equal {table*times}")