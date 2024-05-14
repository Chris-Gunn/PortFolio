sequence = [3, 5, 9, 13, 54, 44, 67, 97, 12, 0]

for i in sequence:
    print(i)

for i in range(1,10):
    if i > 5:
        print(i)


num_list = [1, 2, 3, 4, 5]
found = False
num = int(input("Input a number from 1 to 10 and find out if it's in our list: "))
if num < 1 or num > 10:
    print("Number out of range")
else:
    for number in num_list:
        if num == number:
            found = True
            break

    print(f'List contains {num}: {found}')