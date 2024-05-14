# Request user to name favourite restaurant
string_fav = input("What is your favourite restaurant?\n")
int_fav = int(input("What is your favourite number?\n"))

# Print out both inputs
print(string_fav)
# Prints out the type of the variable
print(type(string_fav))

print(int_fav)

# Convert variable to an integer
string_fav = int(string_fav)
print(string_fav)

# A string type with characters can't be converted into an int