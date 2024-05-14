'''    t = [1, 1, 0, 0, 0, 1, 0]
v = [0]*len(t)
free = [0]*len(t)
#print(free)
count = 0
x = 0



for number in range(len(t)):
    if t[number] == 1:
        count += 1
        for numbers in range(len(t)):
            if t[numbers] == 1:
                t[numbers] = 0
            if t[numbers] == 0:
                t[numbers] = 1
    print(count)
    print(t)'''



"""for numbers in range(len(t)):
   if t[numbers] == 1:
       v[numbers] = 0
   if t[numbers] == 0:
       v[numbers] = 1"""

#print(v)



'''for i in range(len(t)):
    print(t)
    if t[i] == 1:
        count += 1
    print(count)'''


'''for i in range(len(t)):
    if t[cell] == 1:
        v[]
    for cell in range(len(t)):
        if t[cell] == 1:
            v[cell] = 0
        elif t[cell] == 0:
            v[cell] = 1

    print(v)'''

'''t = [1, 1, 0, 0, 0, 1, 0]
v = [0] * len(t)  # Assuming v is initialized as a list of zeros with the same length as t

for cell in range(len(t)):
    if t[cell] == 1:
        v[cell] = 0
    elif t[cell] == 0:
        v[cell] = 1

print(v)'''

#keeps the array the same. The number required for an open cell is changed
def freed_prisoners(inputarray):
    current_open_value = 1      #an open cell is initiated as a 1
    saved_prisoners = 0         #number of saved prisoners is initiated as 0
    for i in range(0, len(inputarray)):             #for the amount of cells in the prison
        if inputarray[i] == current_open_value:    #if the array at element i is equal to an open cell
            saved_prisoners += 1                    #the number of saved prisoners goes up by 1
            current_open_value = int(not(current_open_value)) #if cell open, array is flipped
    return saved_prisoners


print(freed_prisoners([1, 1, 0, 0, 0, 1, 0])) # 4
print(freed_prisoners([1, 1, 1]))  # 1
print(freed_prisoners([0, 0, 0]))  # 0
print(freed_prisoners([0, 1, 1, 1]))  # 1
print(freed_prisoners([1, 1, 0, 0]))  # 2
