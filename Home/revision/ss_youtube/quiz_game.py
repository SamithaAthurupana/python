print("Welcome to quiz game")

playing = input("Do you want to play? ").lower().strip()

if playing not in "yes":
    quit()
print("Okay, lets play :)")

score = 0

answer = input("What does CPU stand for: ").lower().strip()
if answer in "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for: ").lower().strip()
if answer in "graphic processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for: ").lower().strip()
if answer in "random access unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print(f"your score is: {score}")