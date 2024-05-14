names = ["Hello", 1, 8.6, True]

two_d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(type(two_d))

idx_a = two_d[0]
idx_b = two_d[1][2]

# print(idx_a)
# print(idx_b)
'''
for row in two_d:  # Gets into the little brother lists
    print(f"Row: {row}")

    for col in row:  # Pulls the values out of little brother lists
        print(f"col: {col}")
'''

scores = [
    [81.9, 64.7, 50.0, 61.1],
    [72.2, 33.6, 44.8, 70.2],
    [66.8, 75.1, 80.2, 49.9],
    [80.5, 56.7, 48.8, 60.9]
]

for count, row in enumerate(scores, start=1):
    print(f"Term: {count}")

    for col in row:
        print(f"Grade: {col}")