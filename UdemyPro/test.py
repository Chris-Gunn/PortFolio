'''size = 3
print()
print("Identity matrix")
for row in range(0, size):
    for col in range(0, size):

        # Here end is used to stay in same line
        if (row == col):
            print("1 ", end=" ")
        else:
            print("0 ", end=" ")
    print()'''


def run(size):
    print()
    print("Identity matrix")
    for row in range(0, size):
        for col in range(0, size):
            # Here end is used to stay in same line
            if (row == col):
                print("1 ", end=" ")
            else:
                print("0 ", end=" ")
        print()
def run_inverted(size):
    print()
    print("Inverted identity matrix")
    for row in range(0, size):
        for col in range(0, size):
            # Here end is used to stay in same line
            if (col == (size-row -1)):
                print("1 ", end=" ")
            else:
                print("0 ", end=" ")
        print()

size_of_matrix = int(input("What size would you like the matrix? \n"))
run(size_of_matrix)
run_inverted(size_of_matrix)