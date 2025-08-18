import random

game = ("r", "p", "s")
emojis = {"r": "rock", "p": "paper","s": "scissor"}

def user_input():
    while True:
        user_input = input("rock, paper, scissors? (r/p/s) : ").strip().lower()
        if user_input in game:
            return user_input
        else:
            print("Invalid Input")

def display_value(user_input,computer_choice):

    print(f"computer choice: {computer_choice}\nyour choice: {user_input}")

def determine_choice(user_input ,computer_choice):
    if user_input == computer_choice:
        print("Tie!")
    elif (
        (user_input == "r" and computer_choice == "s") or
        (user_input == "s" and computer_choice == "p") or
        (user_input == "p" and computer_choice == "r")):
        print("you win!")
    else:
        print("you lose")

def display_main():
    while True:
        user_input()
        computer_choice = random.choice(game)

        display_value(user_input,computer_choice)
        determine_choice(user_input,computer_choice)

        should_continue = input("Continue? (y/n): ").lower()
        if should_continue == "n":
            break

display_main()




