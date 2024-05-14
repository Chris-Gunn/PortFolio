import random


def game(number, level):
    lives = level
    print(f"You have {lives} lives to find the number!")
    while lives > 0:
        guess = int(input("Please enter the number which you would like to guess: "))
        if guess < number:
            print("That is too low!")
            lives -= 1
            print(f"You have {lives} lives left!")
            print("Guess again!")
        elif guess > number:
            print("That is too high!")
            lives -= 1
            print(f"You have {lives} lives left!")
            print("Guess again!")
        else:
            print(f"That is the right answer, it was {number}!")
            break
         

print("Welcome to the guessing game!\n"
      "I'm thinking of a number between 1 and 100.\n")
difficulty = input("Choose your difficulty, type either 'easy' or 'hard': ")
random_number = random.choice(range(1, 100))


if difficulty == 'easy':
    game(random_number, 10)
elif difficulty == 'hard':
    game(random_number, 5)
