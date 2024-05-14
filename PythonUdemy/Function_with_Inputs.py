def format_name(f_name, l_name):

    capital_first = f_name.capitalize()
    capital_last = l_name.capitalize()
    full_name = capital_first + " " + capital_last
    return full_name


first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")

name = format_name(first_name, last_name)
print(name)
