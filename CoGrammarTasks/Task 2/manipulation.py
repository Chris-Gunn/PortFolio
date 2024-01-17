# Request the user to input a str_manip
# Store the user input in a string named 'str_manip'

str_manip = input("Please enter a sentence: ")

# Calculate and display the length of the variable
print(len(str_manip))

# Find the last letter of the str_manip
end_of_line_char = str_manip[-1]
print(end_of_line_char)

# Replace every occurrence of that letter in the str_manip with '@'
str_manip_replace = str_manip.replace(end_of_line_char,'@')
print(str_manip_replace)

# Print the user sentence in reverse order
str_manip_reverse = str_manip[::-1]
print(str_manip_reverse)

# Print the last three characters of the backward sentence
str_manip_reverse_three = str_manip_reverse[0:3]
print(str_manip_reverse_three)

# Concatenate the first three and last two characters of the sentence.Then print the result
str_manip_five_letter = str_manip[0:3] + str_manip[-2:]
print(str_manip_five_letter)
