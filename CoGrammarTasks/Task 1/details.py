# Request input from the user for their name
# Store input into variable called 'name'
name = input("Please enter your name: ")

# Request input from the user for their age
# Store input in a variable named age
age = input("Please enter your age: ")

# Request input from the user for their house number
# Store input in a variable named house_number
house_number = input("Please enter your house number: ")

# Request input from the user to say what city they are from
# Store input in a variable named city_name
city_name = input("Please enter your city name: ")

# Print out sentence containing all the inputs entered by the user
# String has format() method to put variables inside string placeholder "{}"
print("This is {}. He is {} years old and lives at {} {}.".format(name,age,house_number,city_name))