# This example program is meant to demonstrate errors.

# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print("Welcome to the error program\n")
'''Syntax Error - The print statement requires parentheses around them. The second print statement isn't necessary
and the new line command '\n' should be at the end of the string'''

# Variables declaring the user's age, casting the str to an int, and printing the result
# Syntax error - The code had an unexpected indentation
age_Str == "24 years old" # Syntax error - age_Str is not defined.
age = int(age_Str) # Runtime error - A string can't be converted into an integer
print("I'm" + age + "years old.") # Logical error - No space after "I'm" and "years"

# Variables declaring additional years and printing the total years of age
years_from_now = "3"
total_years = age + years_from_now

print "The total number of years:" + "answer_years"

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = total * 12
print "In 3 years and 6 months, I'll be " + total_months + " months old"

#HINT, 330 months is the correct answer