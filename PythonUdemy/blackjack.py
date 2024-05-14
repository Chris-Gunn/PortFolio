import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def draw_card(cards):
    new_card = random.choice(cards)
    return new_card

while True:
    play = input("Would you like to play blackjack? Press either y or n: ")
    if play == "y":
        player_card_1 = random.choice(cards)
        player_card_2 = random.choice(cards)

        player_cards = player_card_1 + player_card_2
        print(f"Card 1: {player_card_1}\n"
              f"Card 2: {player_card_2}\n"
              f"{player_card_1 + player_card_2}")
        twist = input("Would you like to draw another card? Press either y or n: ")
        if twist == "y":
            card_draw = random.choice(cards)
            print(f"New: {card_draw}")

    elif play == "n":
        print("Thanks for playing!")
        break
    else:
        print("That is an invalid choice. Please choose again!")
        continue
