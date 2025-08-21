name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("you are one a dirty road, it has come to an end and you can go left or right. which way you need to go? ").lower()

if answer == "left":
    answer = input("you come to river, you can walk around it or swim across? ( type walk or swim) : ").lower()
    if answer == "swim":
        print("you swim across and were eaton by an alligator")
    elif answer == "walk":
        print("you walked for many miles, run out of water of and you lost the game.")
    else:
        print("Not a valid option. you lose.")
elif answer == "right":
    answer = input("You come to bridge, it looks wobbly, do you want to cross it or head back? ( cross/back ) : ").lower()
    if answer == "back":
        print("you swim across and were eaton by an alligator")
    elif answer == "cross":
        answer = input("you cross the bridge and meet a stranger. Do you talk to them (yes/no): ").lower()
        if answer == "yes":
            print("You talk to the stranger and they give you gold. you win")
        elif answer == "no":
            print("you ignore the stranger and they are offended and you lose.")
        else:
            print("Not a valid option. you lose.")
    else:
        print("Not a valid option. you lose.")
else:
    print("Not a valid option. you lose.")

print("Thank you for playing", name)