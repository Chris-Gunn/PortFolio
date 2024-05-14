'''
\n creates a new line
\" adds a " in the string
'''

print("Hello \n\"bob\"")

'''
A double '\' allows you to write a backslash in a string.
'''
print("The escape sequence \\n creates a new line in a print statement")


number_builder = ""
i = 0

while i <= 50:
    if i % 2 == 0:
        number_builder += str(i) + " "
    i += 1
print(number_builder)


number_builder = []
i = 0

while i <= 50:
    if i % 2 == 0:
        number_builder.append(str(i))
    i += 1
print(" ".join(number_builder))


name = "Chris"

print("Hello, {}!".format(name))

print(f"Hello, {name}!")
