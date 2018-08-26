import random
import math
from time import sleep

"""
===========================================
                TO DO
        1. Sum face cards correctly
        2. Reset the deck each hand
        3. Correct Aces Functionality
        
===========================================
"""


deck = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K",
        "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K",
        "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K",
        "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]


playerHand = []
dealerHand = []


def dealPrint(string):
    for letter in string:
        print(letter, end=" ")
        sleep(.6)


def Sum(inside):
    count = -1
    for x in inside:
        count += 1
        if (x == "J") or (x == "Q") or (x == "K"):
            inside[count] = 10
        if x == "A":
            inside[count] = 1
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
        if choose == "n":
            return "n"
        else:
            print("This was a yes or no question...")
            choice()


def hand():
    random.shuffle(deck)
    playerHand.append(deck.pop())
    dealerHand.append(deck.pop())
    playerHand.append(deck.pop())
    dealerHand.append(deck.pop())
    print("\nPlayer: ", end="")
    dealPrint(playerHand)
    print("\nDealer: ", end="")
    dealPrint(dealerHand)

    if choice() == "n":
        return


def game():
    print("Hello welcome to blackjack! Starting cash is $20")
    cash = 20
    play = True
    while play:
        isvalid = True
        while isvalid:
            try:
                wager = int(input("You have $" + str(cash) + ". How much would you like to wager?"))
                isvalid = False
            except:
                print("We don't mess around with fake currency...")

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
        elif (Sum(playerHand) > 21) & (Sum(dealerHand) > 21):
            print("DOUBLE BUST!")
            print("You get your wager back")
            cash = cash
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
        check = True
        while check:
            again = input("Want to play another hand or run with your money? [y / n]")

            if again == "n":
                play = False
                check = False
            else:
                if again == "y":
                    playerHand.clear()
                    dealerHand.clear()
                    check = False
                else:
                    print("Sorry I didn't catch that")

    print("Thanks for playing! You left with $" + str(cash))


game()








