def largest(sen):
    words = sen.split()
    max_length = 0
    for word in words:
        count = len(word)
        if count > max_length:
            max_length = count
    return max_length

sentence = "I have royally fucked up"
print(largest(sentence))
