# The line numbers referenced in error comments refer to the original task file

# This example program is meant to demonstrate errors.

# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "Lion"
animal_type = "cub"
number_of_teeth = 16

full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth"

print(full_spec)


"""
Error 1 - Syntax Error - Line 5: 'Lion' is not defined. It should be in quotation marks to make it a string.

Error 2 - Syntax Error - Line 11: Missing parentheses for the print statement around full_spec

Error 3 - Logical Error - Line 9: full_spec runs but with the variable names 'animal','number_of_teeth' and 
'animal_type' in brackets rather than the variable value. Missing f-string to put the values in.

Error 4 - Logical Error - Line 9: The variables 'number_of_teeth' and 'animal_type' are the wrong way round


Code before - 
animal = Lion
animal_type = "cub"
number_of_teeth = 16

full_spec = "This is a {animal}. It is a {number_of_teeth} and it has {animal_type} teeth"

print full_spec

"""