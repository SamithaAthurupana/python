#take 5 words as input and
#create new list with words length greater than 3 characters

'''user_input_list = []

for i in range(5):
    user_input = input("Enter your word: ")
    if len(user_input) == 3:
        user_input_list.append(user_input)

print(user_input_list)'''
'''
word = []
for i in range(5):
    user_input = input("Enter your word: ")

    word.append(user_input)

words_less_than_3_character = [word for word in word if len(word) <= 3]

print(words_less_than_3_character)
'''
'''word = []
for i in range(5):
    user_input = input("Enter your word: ")

    word.append(user_input)

words_less_than_3_character = [word for word in word if len(word) >= 3]
first_character = [word[0]*2 for word in word]

print(words_less_than_3_character)
print(first_character)'''
'''
temps_per_day_for_month = [[0.0 for _ in range(3)] for _ in range(7)]


times_of_day = ["1st hour", "2nd hour", "3rd hour"]


print("Enter the temperature for each day and time of day:")

while True:
    print("\nWould you like to update a temperature? (yes/no)")
    choice = input(">> ").strip().lower()
    if choice == "no":
        break
    elif choice == "yes":
        try:
            day = int(input("Enter the day number (1-7): ")) - 1
            if not (0 <= day < 7):
                print(" Invalid day number.")
                continue

            print("Which time of day?")
            for i, label in enumerate(times_of_day):
                print(f"{i + 1}. {label}")
            time_index = int(input("Enter 1, 2, or 3: ")) - 1
            if not (0 <= time_index < 3):
                print(" Invalid time choice.")
                continue

            new_temp = float(input(f"Enter new temperature for Day {day + 1} {times_of_day[time_index]}: "))
            temps_per_day_for_month[day][time_index] = new_temp
            print("✅ Temperature updated.")

        except ValueError:
            print(" Invalid input. Please try again.")
    else:
        print(" Please answer 'yes' or 'no'.")


print("\n📊 Final Weekly Temperature Report:")
print("Day\tMorning\tAfternoon\tEvening")
for day_index, temps in enumerate(temps_per_day_for_month):
    print(f"{day_index + 1}\t" + "\t".join(f"{temp:.1f}" for temp in temps))'''