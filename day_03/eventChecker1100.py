#ticket price Rs:1000, more than height 1.2,
#age less than 18 discount 20%
#age grater than 60 50%

height = float(input("Enter your height: "))
ticketPrice = 1000
if height < 1.2:
    print("You can't enter.")
    exit()
else:
    discount = 0
    age = int(input("Enter your Age: "))
    if age < 18:
        discount = ticketPrice - 0.2
        print(f"You need to pay:, {ticketPrice - discount}")
    elif age > 60:
        discount = ticketPrice - 0.5
        print(f"You need to pay:, {ticketPrice - discount}")
    else:
        print(f"Ticket price is:, {ticketPrice}")

'''FULL_PRICE = 1000
height = float(input("Enter your height in meters: "))

if height < 1.2:
    print("Sorry, you can't enter due to height restrictions.")
else:
    age = int(input("Enter your age: "))
    if age < 18:
        price = FULL_PRICE * 0.2
    elif age > 60:
        price = FULL_PRICE * 0.5
    else:
        price = FULL_PRICE
    print(f"Your ticket price is: {price:.2f}")'''