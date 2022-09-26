import random
from select import select

while True:
    item = ["rock", "paper", "scissor"]

    computer = random.choice(item)
    player = input("Choice from rock, paper, or scissors?: ").lower()

    
    if player not in item:
        print("Invalid input \nChoice one from rock, paper or scissor: ")
    else:

        if player == computer:
            print("Computer: ", computer)
            print("Player: ", player)
            print("Result: Tie!!!")

        elif player == "rock":
            if computer == "paper":
                print("Computer: ", computer)
                print("Player: ", player)
                print("Result: Computer Win")
            if computer == "scissor":
                print("Computer: ", computer)
                print("Player: ", player)
                print("Result: You Win")

        elif player == "paper":
            if computer == "rock":
                print("Computer: ", computer)
                print("Player: ", player)
                print("Result: You Win")
            if computer == "scissor":
                print("Computer: ", computer)
                print("Player: ", player)
                print("Result: Computer Win")

        elif player == "scissor":
            if computer == "paper":
                print("Computer: ", computer)
                print("Player: ", player)
                print("Result: You Win")
            if computer == "rock":
                print("Computer: ", computer)
                print("Player: ", player)
                print("Result: Computer Win")

    play_again = input("Want to play again? (Y / N): ").lower()

    if play_again == "n":
        break

print("Game over!!!")



"""
import random
from select import select

while True:
    item = ["rock", "paper", "scissor"]

    computer = random.choice(item)
    player = None

    while player not in item:
        player = input("Choice one from rock, paper or scissor: ").lower()

    if player == computer:
        print("Computer: ", computer)
        print("Player: ", player)
        print("Result: Tie!!!")

    elif player == "rock":
        if computer == "paper":
            print("Computer: ", computer)
            print("Player: ", player)
            print("Result: Computer Win")
        if computer == "scissor":
            print("Computer: ", computer)
            print("Player: ", player)
            print("Result: You Win")

    elif player == "paper":
        if computer == "rock":
            print("Computer: ", computer)
            print("Player: ", player)
            print("Result: You Win")
        if computer == "scissor":
            print("Computer: ", computer)
            print("Player: ", player)
            print("Result: Computer Win")

    elif player == "scissor":
        if computer == "paper":
            print("Computer: ", computer)
            print("Player: ", player)
            print("Result: You Win")
        if computer == "rock":
            print("Computer: ", computer)
            print("Player: ", player)
            print("Result: Computer Win")

    play_again = input(" Want to play again? (Y / N): ").lower()

    if play_again == "n":
        break

print("Game over!!!")

"""