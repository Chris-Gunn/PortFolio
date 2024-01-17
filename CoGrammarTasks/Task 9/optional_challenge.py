# Compilation error 1
# The fuction has an IndentationError which causes it to fail
def error_Test():
print("This function should fail!")

error_test()

# Compilation error 2
# The if statement is missing a colon producing a Syntax Error
age = int(input("Please enter your age: "))

if age >= 21
    print("You are allowed to drink anywhere now! Woo!!!")

# Runtime error
# The for loop range goes beyond the size of the list and produces an IndexError
name_list = ["Chris", "Becky", "Aidan", "James", "Rachel", "David"]
new_list = []
for name in range(7):
    new_list.append(name_list[name])
print(new_list)

# Logical error
'''
The code compiles with no errors. However, the calculation calculates the division
first but there should have been a bracket around all the variables before dividing to find
the average. 
average = (maths + science + english + drama + PE) / 5
'''
maths = 80
science = 75
english = 62
drama = 45
PE = 59

average = maths + science + english + drama + PE / 5
print(average)

