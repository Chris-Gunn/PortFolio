#print()
size = 3
print("Identity matrix")
for row in range(0, size):
    for col in range(0, size):

        # Here end is used to stay in same line
        if (row == col):
            print("1 ", end=" ")
        else:
            print("0 ", end=" ")

    print(row[0:2])
    print(col)





#print()


