# Ask: roll the dice?
# If user enters y
#   Generate two random numbers
#   print them
# If user enters n
#   print thank you message
#   Terminate
# Else
#   Print invalid choice

import random

def roll_the_dice():
    while True:
        choice = input("roll the dice? (y/n): ").strip().lower()
        if choice == "y":
            num1 = random.randint(1, 6)
            num2 = random.randint(1, 6)
            print(f"your first random number is {num1:2f} and second one is {num2}")
        elif choice == "n":
            break
        else:
            print("invalid choice")

    print("Thank you")

def main():
    print("=======================================")
    print("roll the dice")
    print("=======================================")


main()
roll_the_dice()


