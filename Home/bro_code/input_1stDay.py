'''name = input("What is your name: ")
print(f"Hello {name}")

age = int(input("How old are you? :"))
print(f"I am {age}")'''

# Exercise rectangle area Calc
'''
length = int(input("Enter the length of rectangle: "))
width = int(input("Enter the width of rectangle: "))
area = (length * width) ** 2
print(f"rectangle area is: {area}cm")'''

# exercise shopping cart
'''
item = input("Which item you want to buy: ")
price = float(input(f"Enter the price of {item}: $"))
quantity = int(input(f"How many {item} you want? : "))

total = price * quantity
print(f"Full price is: ${total}")'''

# Madlibs game
# word game where you create a story
# by filling in blanks with random

adjective1 = input("Enter an adjective (description): ")
noun1 = input("Enter a noun (person, place, thing): ")
adjective2 = input("Enter an adjective (description): ")
verb1 = input("Enter a verb ending with 'ing': ")
adjective3 = input("Enter an adjective (description): ")
print("---------------------------------------------")

print(f"Today I went to a {adjective1} zoo.")
print(f"In an Exhibit, i was saw a {noun1}")
print(f"{noun1} was {adjective2} and {verb1}")
print(f"I was {adjective3}!")

