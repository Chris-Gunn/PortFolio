# The variable 'sentence' is the initial string to be manipulated
sentence = "I am an absolute legend! Do you agree?"

'''
The variable 'letter' is an empty string for the manipulated 'sentence' string,
where every other LETTER is capitalised and stored.
'''
letter = ""

'''
The variable 'word' is an empty string for the manipulated 'sentence' string,
where every other WORD is capitalised and stored.
'''
word = ""
# Counter to count the character position of 'sentence'
count_char = 0

# Counter to count the word position of 'sentence'
count_word = 0

# set all characters of 'sentence' to lowercase
sentence = sentence.lower()
sentence_no_space = sentence.replace(" ", "")
print(sentence_no_space)

# for loop counting up to the number of characters in 'sentence'
for count_char in range(len(sentence_no_space)):
    # Checks if the count is an even number
    if count_char % 2 == 0:
        # if it is even, the count_char is capitalised and added to the 'letter' variable
        letter += (sentence_no_space[count_char]).upper()
        # Checks if the count is an odd number
    elif count_char % 2 == 1:
        # if it is odd, the count_char remains lowercase and is added to the 'letter' variable
        letter += (sentence_no_space[count_char])
# print out the 'letter' variable with the stored characters
print(letter)
print("")

# split the sentence into a list
sentence_list = sentence.split()

# for loop counting up to the number of words in 'sentence'
for count_word in range(len(sentence_list)):
    # Checks if the count is an even number
    if count_word % 2 == 0:
        # if it is even, the word in the list at that position is capitalised
        sentence_list[count_word] = (sentence_list[count_word]).upper()
    # checks if the count is an odd number
    elif count_word % 2 == 1:
        # print(sentence[count_word])
        # if it is odd, the word remains lowercase at that position
        sentence_list[count_word] = (sentence_list[count_word])

# Join the list back together into a sentence
word = " ".join(sentence_list)
# print out the resulting sentence
print(word)
