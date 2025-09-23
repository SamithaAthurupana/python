import random
import time

'''
questions = {
    "What is the capital of Argentina?": "buenos aires",
    "What is the capital of Armenia?": "yerevan",
    "What is the capital of Australia?": "canberra",
    "What is the capital of Austria": "vienna"
}
x = random.choice([x for x in questions.keys()])
print(x)

user_answer = input("Enter the answer: ").strip().lower()

if user_answer == questions[x]:
    print("correct...")
else:
    print("wrong..")'''

questions = {
    "1":{"question": "what is the color of sky? :", "answer": "blue"},
    "2":{"question": "what is the color of floar? :", "answer": "brown"},
    "3":{"question": "what is the color of tree? :", "answer": "green"},
}

print("Welcome C-clarke quiz")
print("======================")

while True:
    keys_list = [x for x in questions.keys()]
    questions_id = random.choice(keys_list)

    time.sleep(2)
    print("Enter answers..")

    user_answer = input(questions[questions_id]["question"]).lower().strip()

    if user_answer == (questions[questions_id]["answer"]):
        print("Your answer is correct...")
    else:
        print("your answer wrong")
print("======================")