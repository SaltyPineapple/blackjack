import random
import math
from time import sleep

deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


playerHand = []
dealerHand = []


def dealPrint(string):
    for letter in string:
        if letter == 1:
            letter = "A"
        if letter == 11:
            letter = "J"
        if letter == 12:
            letter = "Q"
        if letter == 13:
            letter = "K"
        print(letter, end=" ")
        sleep(.6)


def Sum(inside):
    for x in inside:
        if x > 10:
            x = 10
    return sum(inside)


def dealer():
    while Sum(dealerHand) < 17:
        dealerHand.append(deck.pop())


def choice():
    choose = input("\nHit? [Y / N]")
    if choose == "y":
        playerHand.append(deck.pop())
        print("\nPlayer:", end="")
        dealPrint(playerHand)
        if Sum(playerHand) < 21:
            choice()
    else:
        return "n"


def hand():
    random.shuffle(deck)
    playerHand.append(deck.pop())
    dealerHand.append(deck.pop())
    playerHand.append(deck.pop())
    dealerHand.append(deck.pop())
    print("\nPlayer:", end="")
    dealPrint(playerHand)
    print("\nDealer:", end="")
    dealPrint(dealerHand)

    if choice() == "n":
        return


def game():
    print("Hello welcome to blackjack! Starting cash is $20")
    cash = 20
    play = True
    while play:
        wager = int(input("You have $" + str(cash) + ". How much would you like to wager?"))
        hand()
        dealer()
        print("\nDealer:", end="")
        dealPrint(dealerHand)
        print("\nPlayer:", end="")
        dealPrint(playerHand)
        if (Sum(playerHand) == 21) & (Sum(dealerHand) != 21):
            print("\nBLACKJACK!")
            print("You got $" + str(wager))
            cash = wager + cash
        elif (Sum(dealerHand) == 21) & (Sum(playerHand) != 21):
            print("\nDEALER BLACKJACK!")
            print("You lost $" + str(wager))
            cash = cash - wager
        elif Sum(playerHand) > 21:
            print("\nBUST!")
            print("You lost $" + str(wager))
            cash = cash - wager
        elif (Sum(dealerHand) > 21) & (Sum(playerHand) < 21):
            print("\nDEALER BUST!")
            print("You got $" + str(wager))
            cash = cash + wager
        elif (Sum(playerHand) > Sum(dealerHand)) & (Sum(playerHand) < 21):
            print("\nYOU WON!")
            print("You got $" + str(wager))
            cash = cash + wager
        elif (Sum(playerHand) < Sum(dealerHand)) & (Sum(dealerHand) < 21):
            print("\nYOU LOST!")
            print("You lost $" + str(wager))
            cash = cash - wager
        elif Sum(playerHand) == Sum(dealerHand):
            print("\nTIE! You get your wager back")
            cash = cash
        again = input("want to play another hand? [y / n]")
        if again == "n":
            play = False
        else:
            playerHand.clear()
            dealerHand.clear()

    print("Thanks for playing! You ended with $" + str(cash))


game()








