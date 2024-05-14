alphabet = alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                       't', 'u', 'v', 'w', 'x', 'y', 'z']
# initializing string
quote = "You can have data without information, but you cannot have information without data."

# using naive method to get count
# counting e
count = 0
n = 0

for i in quote:
    if i == alphabet[n]:
        count = count + 1
        print(alphabet[n])
    n += 1

# printing result
print("Count of e in GeeksforGeeks is : "
      + str(count))