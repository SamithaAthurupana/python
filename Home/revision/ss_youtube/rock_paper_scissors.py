import random

user_wins = 0
computer_win = 0
options = ["rock","paper","scissors"]

while True:
    user_input = input("Type rock/paper/scissors or quite to q: ").lower().strip()
    if user_input == "q":
        break

    if user_input not in options:
        continue
    random_number = random.randint(0,2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("you won!")
        user_wins += 1
        continue
    elif user_input == "paper" and computer_pick == "rock":
        print("you won!")
        user_wins += 1
        continue
    elif user_input == "scissors" and computer_pick == "paper":
        print("you won!")
        user_wins += 1
        continue
    elif user_input == computer_pick:
        print("both you are tie!")
        continue
    else:
        print("computer won!")
        computer_win += 1
        continue

print(f"you won", user_wins," times")
print(f"computer won", computer_win,"times")
print("Thank you for playing")