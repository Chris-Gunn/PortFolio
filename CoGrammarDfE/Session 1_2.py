"""
forename = "Chris"
surname = "Gunn"

full_name = forename + " " + surname
print(full_name)

message = "batman"

message_len = len(message)
print(message_len)

message = "PyThOn Is FuN!"
new_message = message.upper()
print(new_message)
new_message = message.lower()
print(new_message)
new_message = message.capitalize()
print(new_message)

message = "****They've*taken*the*hobbits*to*Eisenguard!****"

message_strip = message.strip("*")
print(message_strip)

reference = "The-king-of-iron-fist"

new_ref = reference.split("-")
print(new_ref)

rejoin = " ".join(new_ref)
print(rejoin)

message = "Hey!You!Over!There!"

message_replace = message.replace("!"," ")
print(message_replace)

string = "Hello World"
idx = string[0 : : 2]
print(idx)
idx = string[0 : : -5]
print(idx)
"""














age_Str = "24 years old"
age = int(age_Str)