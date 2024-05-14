# Variable containing an empty string to put the asterisks into
pattern = ""

# A for loop that counts up and stops at 10 as the output requires 9 lines
for asterisk in range(0, 10):
    # If the asterisk count is less than five, the pattern string adds an asterisk
    if asterisk < 5:
        pattern += "*"
        print(pattern)
        '''
    If the asterisk count is greater than five, the last asterisk in the string
    is removed every time there is a count up
        '''
    else:
        pattern = pattern[:-1]
        print(pattern)
