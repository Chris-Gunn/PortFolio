import copy
'''

string_list = ["John", "Mary", "Harry"]
print(string_list)

pet_list = ["cat", "dog", "hamster", "goldfish", "parrot"]
print(pet_list[0])

num_list = [1, 4, 2, 7, 5, 9]
print(num_list[1:2])

name_list = ["James", "Molly", "Chris", "Peter", "Kim"]
name_list[4] = "Tom"
print(name_list)

new_list = [34, 35, 75, "Coffee", 98.8]
new_list.append("Tea")
print(new_list)

char_list = ['P', 'y', 't', 'h', 'o', 'n']
del char_list[3]
print(char_list)

new_list.extend(name_list)
print(new_list)

new_list.insert(1, "Kim")
print(new_list)

# Nested lists

a = [1, 2, 3]
b = [4, 9, 8]
c = [a, b, 'tea', 16]

print(c)
c.remove(b)
print(c)

a = [1, 2, 3]
b = a[:]
b[1] = 10

print(a)
print(b)
'''

# Copy

a = [[1, 2, 3],[4, 5, 6]]
b = a[:]
c = copy.deepcopy(a)
b[0][1] = 10
# c[1][1] = 2
print(a)
print(b)
print(c)

# List Comprehension

num_list = ['1', '5', '8', '14', '25', '31']
new_num_list_ints = [int(element) for element in num_list]
print(new_num_list_ints)
by_two_num_list = [int(element) * 2 for element in num_list]
print(by_two_num_list)

# Dictionaries

int_key_dict = {1: 'apple',
                2: 'banana',
                3: 'orange'}

print(int_key_dict)

int_key_list = [(1, 'apple'), (2, 'banana'), (3, 'orange')]
int_key_dict_2 = dict(int_key_list)
print(int_key_dict_2)

print(int_key_dict_2[1])

profile_dict = {'name': 'Chris',
                'surname': 'Gunn',
                'age': 28,
                'cell': '+447415170861'}

print(profile_dict['surname'])
print(profile_dict.get('cell'))

keys = profile_dict.keys()
values = profile_dict.values()

print(keys)
print(values)
