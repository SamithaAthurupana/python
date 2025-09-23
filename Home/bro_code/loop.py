'''num = int(input("Enter number between 1 to 10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter number between 1 to 10: "))

print(f"your number is {num}")
'''

#python compound interest calculator
'''
principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the principle amount: $"))
    if principle <= 0:
        print("Principle can't be less than or equal to zero")
    else:
        break

while True:
    rate = float(input("Enter the interest rate: "))
    if rate <= 0:
        print("rate can't be less than or equal to zero")
    else:
        break

while True:
    time = int(input("Enter the time: "))
    if time <= 0:
        print("time can't be less than or equal to zero")
    else:
        break

total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} year/s: ${total:.2f}")'''

# for loop = execute a block of code a fixed number of times.
#           you can iterate over a range, string, sequence, etc
'''
credit_card = "1234-5678-9012-3456"

for x in credit_card:
    print(x)
print(credit_card)'''

'''
for x in range(1, 21):
    if x == 13:
        break
    else:
        print(x)'''

'''
import time

my_time = int(input("Enter the time in seconds: "))
for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("Time's up")'''

# shopping cart application
foods = []
prices = []
total = 0

while True:
    food = input("enter any food to buy ( q to quite ): ").lower()
    if food == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)
print("-----Your Cart-----")

for food in foods:
    print(food, end=" ")
print()
for price in prices:
    total += price
print(f"You need to pay for the foods ${total} only")


























