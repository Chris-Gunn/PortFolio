# Reads in a word as an input, 'un' is then added to the word and is returned as an output
def add_prefix_un(word):
    un_word = "un" + word
    return un_word


# Reads in a word with 'ness' as a suffix as an input, returns the word without the 'ness'
def remove_suffix_ness(longword):
    # Removes the 'ness'
    remove_ness = longword.replace('ness', '')
    # if the last character of the word with the 'ness' removed has an 'i', replaces it with a 'y'
    if remove_ness[-1] == 'i':
        new_word = remove_ness.replace('i', 'y')
    else:
        new_word = remove_ness
    return new_word


# Takes a predetermined prefix and adds it to a list of words
def add_prefix(prefix, words):
    # Empty list for the words with both the prefix and suffix combined to go into
    combined_word = []

    # For loop to read through the word list
    for word in words:
        # If the word doesn't start with the prefix, add the suffix to the prefix
        if not word.startswith(prefix):
            combined_word.append(f'{prefix}{word}')
        # Else the prefix is just added to the list
        else:
            combined_word.append(word)
    result = ' :: '.join(combined_word)
    return result


def adjective_to_verb(sentence, index):
    # Splits the sentence up into a string of single words
    split_sentence = sentence.split()
    # Adds 'en' to the word at the index position in the list
    split_sentence[index] = split_sentence[index] + 'en'
    return split_sentence[index]


happy = add_prefix_un("happy")
print(happy)

manageable = add_prefix_un("manageable")
print(manageable)

heaviness = remove_suffix_ness("heaviness")
print(heaviness)

sadness = remove_suffix_ness('sadness')
print(sadness)

bright = adjective_to_verb('I need to make that bright', -1)
print(bright)

dark = adjective_to_verb('It got dark as the sun set.', 2)
print(dark)


en_words = ['en', 'close', 'joy', 'lighten']
en = 'en'
output_en = add_prefix(en, en_words)
print(output_en)

pre_words = ['pre', 'serve', 'dispose', 'position']
pre = 'pre'
output_pre = add_prefix(pre, pre_words)
print(output_pre)

auto_words = ['auto', 'didatic', 'graph', 'mate']
auto = 'auto'
output_auto = add_prefix(auto, auto_words)
print(output_auto)

inter_words = ['inter', 'twine', 'connected', 'dependent']
inter = 'inter'
output_inter = add_prefix(inter, inter_words)
print(output_inter)
