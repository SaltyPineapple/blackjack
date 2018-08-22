import random
import math
from time import sleep

deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10,
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10,
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10,
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]

playerHand = []
dealerHand = []


def dealer():
    while sum(dealerHand) < 17:
        dealerHand.append(deck.pop())


def choice():
    choose = input("Hit? [Y / N]")
    if choose == "y":
        playerHand.append(deck.pop())
        print(playerHand)
        if sum(playerHand) < 21:
            choice()
    else:
        return "n"


def hand():
    random.shuffle(deck)
    playerHand.append(deck.pop())
    dealerHand.append(deck.pop())
    playerHand.append(deck.pop())
    dealerHand.append(deck.pop())
    print(playerHand)
    if choice() == "n":
        return


def game():
    print("Hello welcome to blackjack! Starting cash is $20")
    cash = 20
    play = True
    while(play):
        wager = int(input("You have $" + str(cash) + ". How much would you like to wager?"))
        hand()
        dealer()
        print("Dealer:" + str(dealerHand))
        print("Player:" + str(playerHand))
        if (sum(playerHand) == 21) & (sum(dealerHand) != 21):
            print("BLACKJACK!")
            cash = wager + cash
        elif (sum(dealerHand) == 21) & (sum(playerHand) == 21):
            print("DEALER BLACKJACK!")
        elif sum(playerHand) > 21:
            print("BUST!")
            cash = cash - wager
        elif (sum(dealerHand) > 21) & (sum(playerHand) < 21):
            print("DEALER BUST!")
            cash = cash + wager
        elif (sum(playerHand) > sum(dealerHand)) & (sum(playerHand) < 21):
            print("YOU WON!")
            cash = cash + wager
        elif (sum(playerHand) < sum(dealerHand)) & (sum(dealerHand) < 21):
            print("YOU LOST!")
            cash = cash - wager
        again = input("want to play another hand? [y / n]")
        if again == "n":
            play = False
        else:
            playerHand.clear()
            dealerHand.clear()
    print("Thanks for playing! You ended with $" + str(cash))


game()








