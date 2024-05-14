'''
def adding(a, b):
    total = a + b
    description = "Total: "
    return description + str(total)


def multiply(num1 = 6, num2 = 5):
    total = num1 * num2
    print(f"{num1} * {num2} = {total}")


multiply_test = multiply()

multiply_test = multiply(1)

multiply_test = multiply(2, 7)

multiply_test = multiply(num2 = 8, num1 = 7)


# add_one(3)
# result = add_one(3)
# print(result)


x = 2
y = 3

'''

# Example 1

def add_one(x):
    y = x + 1
    return y

# Example 2

print("Example 2: ")
num = 10
print("10 plus 1 is equal to: " + str(add_one(num)) + ".")

# Example 3

print("\nExample 3: ")
num = add_one(4)
print("4 plus 1 is equal to: " + str(num) + ".")

# Example 4

print("\nExample 4: ")


def power(base, exponent):
    result = base ** exponent
    return (result)


print(power(3, 5))

# ************ Example 5 ************


def double_this_number(number):
        y = number * 2 # Multiples the number by 2.
        return y
digit = 8

print(double_this_number(digit))

# ************ Example 6 ************
def return_first_letter_word(word):
        y = word[0]
        return y
sentence = "Hello, world"
char = return_first_letter_word(sentence)
print(char)

# ************ Example 7 ************
def put_number_in_list(num):
        newList = []
        newList.append(num)
        return newList

while True:
    num_choice = int(input("Choose a number: "))
    num_store = put_number_in_list(num_choice)
    again = input("Choose another number?").lower()
    if again == "yes":
        continue
    elif again == "no":
        print(num_store)
        break

# ************ Example 8 ************
def put_number_in_list_if_big(num):
        newList = []
        if num >100:
                newList.append(num)
        return newList # Be careful! This could return an empty list.

c = put_number_in_list_if_big(num_choice)
print(c)

# ************ Example 9 ************
def compute_sum_of_two_numbers(num1, num2):
        y = num1+num2
        return y

num_one = 10
num_two = 20
answer = compute_sum_of_two_numbers(num_one, num_two)
print(answer)

# ************ Example 10 ************
def takes_no_parameters():
        y = "This function takes no parameters as input, but that means its functionality is limited...."
        return y


# As you can see from the examples above, you can pretty much do anything you want in a function.
# You can create new data structures, use conditionals etc.
# We can call the input variable anything we want. It's just a name we give it
# so we know how to refer to it within the function.
# As seen in the second to last example, we can have multiple input parameters too.
# There's no limit on them, as long as you can keep track of what's what!
# In the last example, we have a function that takes no input parameters.
# This is also possible, but it means the user who calls the function has limited
# interaction with the function - they can't supply any input!
# In the case of some functions - imagine a function that returned the current time
# i.e. - getTime() - it makes sense  why such a function would not
# need input parameters (unless you had a more complex function like get_time(timezone)
# which returned the time for a specific timezone the calling user provides!)
## Values passed into the function through the 'function's parameters'
# (variables e.g. num1 and num2 above) will be referenced with those variable names.
# Think of it as copying in the values from the input parameter values when
# 'calling' the function to these 'function parameters'.


# While the above functions may not seem useful, this is because they are simple.
# You can have functions with hundreds of lines that do complex tasks.
# However it is often very useful to define functions that do one specific task
# with a few lines of codes as opposed to a complicated function that does many
# tasks with hundreds of lines of code, # i.e. break up a complicated function
# into many simpler functions so that it is # easier to understand the function's
# role and find errors!


# =========== Functions Without Return Statements ===========
# Functions do not need to have a return statement

# ************ Example 11 ************
print("\nExample 11:")
def print_word(word):
        print(word)

# The function above just prints out something, it doesn't have a return statement.
# That's okay, but it means that if you make a call like:

y  = print_word("abc")


# y will store the special value 'None'.
# This is not a string or any other data type, so it will cause an error when trying to do other things with it.
# Be careful that your functions return values, if that's what you need them to do.


# ************ Example 12 ************
print("\nExample 12:")
# We can call the function multiple times in a loop:

num = 10
# This loop runs 10 times, and each time, 1 is added to the value of 10.
# So after the first iteration it will be 11, the second iteration computes
# 11 + 1 = 12, etc... until 20.
for i in range(10):
    num = add_one(num)
print(num)


# =========== Scope ===========
# Scope is what we call a program’s ability to find and use variables in a program.
# The rule of thumb is that a function is covered in one-way glass:
# it can see out, but no one can see in.
# This means that a function can call variables that are outside the function,
# but the rest of the code cannot call variables that are defined within the function.

# *********** Example 13 ****************
print("\nExample 13:")
j = 5

def do_something():
    # Output -> 5
    print(j)

do_something()

# Output -> 5
print(j)

# The above function can see outside and so fetches j from outside the function.
# Let's see what happens when this goes wrong.

# *********** Example 14 ****************
j = 5

def do_something():
    j = 7     # Output if j was printed from inside this function would be 7

print(j) # Prints 5

do_something()
print(j)