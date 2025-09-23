# Generate random number
# Ask the user to make a guess
# If not a valid number
#   print an error
# If number < guess
#   Print too low
# If number > guess
#   Print too high
# Else
#   Print well done

'''import random

number1 = random.randint (1,100)
print(number1)

while True:
    guess = int(input("Enter your number (1 - 100) : "))
    if guess < number1:
        print("Our Guess is Too High")
    elif guess > number1:
        print("Our Guess is Too Low")
    elif guess == number1:
        print("congratulation you have entered correct number.. ")
        break
    elif guess == "":
        print("Enter valid number")
    else:
        print("Enter valid number")
'''

import random

number1 = random.randint (1,100)
print(number1)

while True:
    try:
        guess = int(input("Enter your number (1 - 100) : "))
        if guess < number1:
            print("Our Guess is Too High")
        elif guess > number1:
            print("Our Guess is Too Low")
        else:
            print("congratulation you have entered correct number.. ")
            break
    except ValueError: # when input is string came a value error
        print("Please enter a valid number")