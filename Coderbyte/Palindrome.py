def palindrome(word):
    check_palindrome = word
    reverse_string = check_palindrome[::-1]
    if reverse_string == word:
        print("This is a palindrome")
    else:
        print("This is not a palindrome")
    return reverse_string

palindrome('racecar')
palindrome('Chrsitopher')
palindrome('saippuakivikauppias')
palindrome('wordsmith')