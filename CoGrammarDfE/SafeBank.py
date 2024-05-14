'''
for row in range(3):
    for col in range(3):

        print(f"Cell {row} {col}")

for number in range(10):
    if number == 5:
        break
    if number % 2 == 0:
        continue
    print(number)


two_dee = [['John', 'Terry', 'Andy'],['Jimmy', 'Johnny', 'Joe']]  # Outer bracket = big sibling, inner bracket = little sibling

for row in two_dee:
    print(row)
    for col in row:
        print(col)
'''

