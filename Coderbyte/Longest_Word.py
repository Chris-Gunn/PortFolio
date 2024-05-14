def LongestWord(sen):
    x = sen.split()
    longest_word = ""
    max_length = 0

    for word in x:
        count = 0
        for char in word:
            if char.isalpha():
                count += 1
        if count > max_length:
            max_length = count
            longest_word = word
    return longest_word, max_length


# keep this function call here
print(LongestWord(input("Please enter in your sentence: ")))