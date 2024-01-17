# The line numbers refer to the original task file

# This example program is meant to demonstrate errors.

# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print("Welcome to the error program\n")

"""
Error 1 - Syntax Error - Line 5: Missing parentheses for the print statement around the 
string "Welcome to the error program"

Error 2 - Syntax Error - Line 6: The "\n" should be before the final quotation mark in the string and the print 
statement is unnecessary

Code before:

print "Welcome to the error program"
    print "\n"
"""


# Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "24"
age = int(age_Str)
print("I'm " + age_Str + " years old.")

"""
Error 3 - Syntax Error - Lines 9-11: The three lines are unnecessarily indented  

Error 4 - Syntax Error - Line 9: 'age_Str' is not defined. Only one '=' is required to define age_Str.

Error 5 - Syntax Error - Line 10: age_Str can't be converted to an integer as there are characters in the string.

Error 6 - Runtime Error - Line 11: TypeError - A string can't be concatenated to an integer, only string to string.
Used 'age_Str' instead of 'age' in the print statement

Error 7 - Logical Error - Line 11: No space before "years old" and after "I'm"

Code before:

    age_Str == "24 years old"
    age = int(age_Str)
    print("I'm" + age + "years old.")
"""

    # Variables declaring additional years and printing the total years of age
years_from_now = 3
total_years = age + years_from_now

print("The total number of years: " + str(total_years))

"""
Error 8 - Syntax Error - Lines 14-15: Unnecessary indentation

Error 9 - Runtime Error - Line 15: TypeError - age variable is an integer and can't be concatenated to 
'years_from_now' variable as it's a string.

Error 10 - Syntax Error - Line 17: Missing parentheses for the print statement around the string

Error 11 - Logical Error - Line 17: "answer_years" should be replaced by str(total_years) to give the total number of 
years as a string.

Code before:

    years_from_now = "3"
    total_years = age + years_from_now

print "The total number of years:" + "answer_years"
"""

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = (total_years * 12) + 6
print("In 3 years and 6 months, I'll be " + str(total_months) + " months old")

"""
Error 12 - Syntax Error - Line 20: The variable 'total' is undefined. It should be replaced with the variable 
'total_years'.

Error 13 - Syntax Error - Line 21: Missing parentheses for the print statement around the string

Error 14 - Runtime Error - Line 21: 'total_months' is an integer and can't be concatenated to a string

Error 15 - Logical Error - Lines 20-21: total_months is only the three years and doesn't include the extra six months

Code before:

total_months = total * 12
print "In 3 years and 6 months, I'll be " + total_months + " months old"
"""
#HINT, 330 months is the correct answer

