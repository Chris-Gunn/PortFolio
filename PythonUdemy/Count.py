#Create a variable to store the given string
#Convert the given string to lowercase
quote = ("You can have data without information, but you cannot have information without data.").lower()


#Create a list containing every lowercase letter of the English alphabet
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
#for every letter in the alphabet list:
#Create a variable to store the frequency of each letter in the string and assign it an initial value of zero
alphabet_freq = {}
for letter in alphabet:
  alphabet_freq[letter] = 0

#for every letter in the given string:
#if the letter in the string is the same as the letter in the alphabet list
#increase the value of the frequency variable by one.
for character in quote:
  if character in alphabet:
    alphabet_freq[character] += 1

#if the value of the frequency variable does not equal zero:
#print the letter in the alphabet list followed by a colon and the value of the frequency variable
for letter,counter in alphabet_freq.items():
  if not alphabet_freq[letter] == 0:
    print(f"{letter}: {counter}")
