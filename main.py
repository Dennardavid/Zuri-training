#importing random
import random

#list of options
options = ["r","p","s"]

#function for user input
def choose():
    user_input = input("Pick an option, r=rock, p=paper, s=scissors :\n")
    user_input = user_input.lower()
    if user_input not in options:
        print("Please select from the valid options, r=rock, p=paper, s=scissors :\n")
        user_input = choose()
    return user_input

#loop to perform comparison
while True:
    #calling user input function
    user_input = choose()
    #generating computer input
    computer_input = random.choice(options)

    #displaying choices made
    print("Players choice(", user_input,")")
    print("Computers choice(",computer_input,")")

    #comparing inputs from user and computer for Rock
    if user_input == "r":
        if computer_input == "r":
            print("You tied")
            pass
        if computer_input == "p":
            print("computer wins")
            break
        if computer_input == "s":
            print("Player wins")
            break
    
    #comparing inputs from user and computer for Paper
    if user_input == "p":
        if computer_input == "p":
            print("You tied")
            pass
        if computer_input == "r":
            print("Player wins")
            break
        if computer_input == "s":
            print("Computer wins")
            break

    #comparing inputs from user and computer for Scissors
    if user_input == "s":
        if computer_input == "s":
            print("You tied")
            pass
        if computer_input == "p":
            print("Player wins")
            break
        if computer_input == "r":
            print("Computer wins")
            break