'''while True:
    print("stuck in a loop")'''
'''while True:
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
    exitProgram = input("Do you want to continue : Y/n: ")
    if exitProgram == "n":
        exit()'''

#when type number identify even or odd
'''oddNumber = 0
evenNumber = 0

while True:
    userNumber = int(input("Enter number: "))
    if userNumber % 2 == 0:
        print("Even")
    else:
        print("odd")
'''

oddNumber = 0
evenNumber = 0

number = float(input("Enter your number or -1 to end: "))
while number != -1:
    if number % 2 == 0:
        evenNumber = evenNumber + 1
    else:
        oddNumber = oddNumber + 1

    number = float(input("Enter your number or -1 to end: "))
print(f"Number of Even Numbers: {evenNumber}")
print(f"Number of odd Numbers: {oddNumber}")