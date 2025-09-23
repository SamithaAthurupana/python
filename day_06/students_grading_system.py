'''
get 5 subjects mark
identify sub, average
give the grade 75- A, 50 - C , less than 35 - fail,
'''
#class example
'''import time

subjects_marks = []

input("Did you participate exam? ( Enter yes/no  ) ")
print(" 1. Maths: \n"
      " 2. Science: \n"
      " 3. Buddhist: \n"
      " 4. Sinhala: \n"
      " 5. Health: \n")

for i in range(5):
    user_input = int(input(f"{i+1}. enter the subjects marks: "))
    subjects_marks.append(user_input)

print(subjects_marks)
sum_subject = sum(subjects_marks)
print(f"full marks of student: {sum_subject}")
average = sum_subject/5 #sum(marks) // len(marks)
print(f"Average of student: {average}")

print("Now print your grade.. wait second..")
time.sleep(9)
if average > 75:
    print("Grade is A")
elif average > 50:
    print("You are pass")
else:
    print("you are fail")'''

#chtgpt example
import time

subjects = ["Maths", "Science", "Buddhist", "Sinhala", "Health"]
subjects_marks = []

participation = input("Did you participate in the exam? (yes/no): ").strip().lower()

if participation != "yes":
    print("You didn't participate in the exam.")
else:
    print("\nEnter your marks for the following subjects:")
    for subject in subjects:
        while True:
            try:
                mark = int(input(f"- {subject}: "))
                if 0 <= mark <= 100:
                    subjects_marks.append(mark)
                    break
                else:
                    print("Please enter a valid mark between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

    print("\nYour marks:", subjects_marks)

    total = sum(subjects_marks)
    average = total / len(subjects_marks)

    print(f"\nTotal Marks: {total}")
    print(f"Average Marks: {average:.2f}")

    print("\nCalculating grade...", end="")
    time.sleep(2)  # reduced wait for better UX
    print(" Done!\n")

    if average > 75:
        print("🎉 Grade: A")
    elif average > 50:
        print("🙂 You passed!")
    else:
        print("😞 You failed. Better luck next time.")
