import random

game = ("r", "p", "s")
emojis = {"r": "rock", "p": "paper","s": "scissor"}
while True:
    user_input = input("rock, paper, scissors? (r/p/s) : ").strip().lower()
    if user_input not in game:
        print("Invalid Input")
        continue
    computer_choice = random.choice(game)
    print(f"computer choice: {computer_choice}\nyour choice: {user_input}")

    if user_input == computer_choice:
        print("Tie!")
    elif (
        (user_input == "r" and computer_choice == "s") or
        (user_input == "s" and computer_choice == "p") or
        (user_input == "p" and computer_choice == "r")):
        print("you win!")
    else:
        print("you lose")

    should_continue =  input("Continue? (y/n): ").lower()
    if should_continue == "n":
        break





