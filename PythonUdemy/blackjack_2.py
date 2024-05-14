import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
money = 2000


def starting_hand(card):
    player_card_1 = random.choice(card)
    player_card_2 = random.choice(card)
    player_cards = player_card_1 + player_card_2
    return player_card_1, player_card_2, player_cards


def dealer_hand(card):
    dealer_card_1 = random.choice(card)
    dealer_card_2 = random.choice(card)
    dealer_cards = dealer_card_1 + dealer_card_2
    return dealer_card_1, dealer_card_2, dealer_cards


def draw_card(card):
    player_card = random.choice(card)
    return player_card


player = starting_hand(cards)
# print("Player: ", player)
dealer = dealer_hand(cards)
# print("Dealer: ", dealer)
dealer_1 = dealer[0]
dealer_2 = "X"

# print("Player Card 1: ", player[0], "Player Card 2: ", player[1])
# print("Player Cards: ", player[2])
# print("Dealer Card 1: ", dealer[0], "Dealer Card 2: ", dealer_2)

while True:
    play = input("Would you like to play blackjack? Press either y or n: ")
    if play == "y":
        player = starting_hand(cards)
        print("Player Card 1: ", player[0], "Player Card 2: ", player[1])
        print("Player Cards: ", player[2])
        while True:
            twist = input("Would you like to draw another card? Press either y or n: ")
            if twist == "y":
                new_card = draw_card(cards)
                player[2] = player[2] + new_card
                print(f"New Card: {new_card}")
                print(f"New Total: {player[2]}")
                if player[2] > 21:
                    break

                twist = input("Would you like to draw another card? Press either y or n: ")
                if twist == "y":
                    new_card = draw_card(cards)
                    player[2] = player[2] + new_card
                    print(f"New Card: {new_card}")
                    print(f"New Total: {player[2]}")
                    if player[2] > 21:
                        break

                elif twist == "n":
                    if new_card[0] > dealer[2]:
                        print("Dealer Card 1: ", dealer[0], "Dealer Card 2: ", dealer[1], "Dealer Total: ", dealer[2])
                        print("you win!")
                        break
                    else:
                        print("Dealer Card 1: ", dealer[0], "Dealer Card 2: ", dealer[1], "Dealer Total: ", dealer[2])
                        print("You lose!")
                        break

                if player[2] > 21:
                    print("You lose!")
                    break
            elif twist == "n":
                if new_card[0] > dealer[2]:
                    print("Dealer Card 1: ", dealer[0], "Dealer Card 2: ", dealer[1], "Dealer Total: ", dealer[2])
                    print("you win!")
                    break
                else:
                    print("Dealer Card 1: ", dealer[0], "Dealer Card 2: ", dealer[1], "Dealer Total: ", dealer[2])
                    print("You lose!")
                    break

    elif play == "n":
        print("Thanks for playing!")
        break
    else:
        print("That is an invalid choice. Please choose again!")
        continue






