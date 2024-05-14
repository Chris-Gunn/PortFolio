# Mines are represented with a 'm'
# normal spots are represented with a '-'
field = [['-', 'm', '-', '-', '-', '-'],
         ['m', '-', '-', '-', '-', '-'],
         ['-', '-', '-', 'm', 'm', '-'],
         ['-', '-', 'm', '-', '-', '-'],
         ['-', 'm', '-', '-', '-', '-']
         ]

final_field = []

for row in range(len(field)):

    for col in range(len(field[row])):

        if field[row][col] == 'm':
            print(f"Position, row: {row} col: {col}")
            print("This is a mine")
            final_field[row][col] = 'm'

        elif field[row][col] == '-':
            print(f"Position, row: {row} col: {col}")
            print("This is not a mine")
            final_field[row][col] = '-'

print(final_field)
