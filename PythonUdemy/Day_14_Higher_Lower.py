from Day_14_Art import logo, vs
from Day_14_Game_Data import data
import random


def people(people_data):
    # Takes a random person from the data list
    p1 = data[random.randint(0, len(data) - 1)]
    # removes that person so they cannot be compared with itself
    data.remove(p1)
    # Takes a different random person from the data list
    p2 = data[random.randint(0, len(data) - 1)]
    return p1, p2


def comparison(p1, p2, guess):
    if guess == 1 and p1['follower_count'] > p2['follower_count']:
        return True
    elif guess == 1 and p1['follower_count'] < p2['follower_count']:
        return False
    elif guess == 2 and p1['follower_count'] < p2['follower_count']:
        return True
    elif guess == 2 and p1['follower_count'] > p2['follower_count']:
        return False


print(logo)
print(" ")
print("Welcome to the higher or lower game!")

score = 0
person_1, person_2 = people(data)
while True:

    print("")
    print("")
    print("")
    print(f"{person_1['name']}: {person_1['follower_count']}")
    print(vs)
    print(person_2['name'])

    guess = int(input(f"Who has the higher number of followers on instagram? Press 1 for first person, 2 for second: "))

    if comparison(person_1, person_2, guess):
        print("You're right!")
        person_1 = person_2
        person_2 = random.choice(data)
        score += 1
        print(f"you're current score is: {score}")
    else:
        print("You're wrong!")
        print(f"{person_1['name']} has: {person_1['follower_count']}\n"
              f"{person_2['name']} has: {person_2['follower_count']}")
        print(f"You're final score is: {score}")
        break
