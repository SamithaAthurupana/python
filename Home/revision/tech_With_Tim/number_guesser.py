import random

random_number = random.randint(0,11)
print(random_number)

while True:
    user_guess = input("type a number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("please enter a number next time.")
    if user_guess == random_number:
        print("wow")
        break
    else:
        print("your choice is incorrect")





