# Hangman in python
import random

words = ("apple", "orange", "banana", "coconut", "pineapple")

# dictionary of key:()
hangman_art = {0: ("   ",
                   "   ",
                   "   "),
               1: (" o ",
                   "   ",
                   "   "),
               2: (" o ",
                   " | ",
                   "   "),
               3: (" o ",
                   " | ",
                   "/| "),
               4: (" o ",
                   "/|\\",
                   "   "),
               5: (" o ",
                   "/|\\",
                   "/"),
               6: (" o ",
                   "/|\\",
                   "/ \\")}

def display_man(wrong_guess):
    print("*************************")
    for line in hangman_art[wrong_guess]:
        print(line)
    print("*************************")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guess_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        # display_answer(answer)
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input")
            continue

        guess_letters.add(guess)

        if guess in guess_letters:
            print(f"{guess} is already guessing")

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("You win!")
            is_running = False
        elif wrong_guesses >= len(hangman_art) -1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("you lose!")
            is_running = False

if __name__ == "__main__":
    main()

