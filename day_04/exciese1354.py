'''i = 0
while i < 100:
    i += 1

    if i == 30:
        break
    print(i, end=" ")
print("program exit")

i = 0
while i < 100:
    i += 1

    if i == 30:
        continue
    print(i, end=" ")
print("program exit")'''
""""""
#Simple ATM machine: use enter pin, has validate pin is correct and proceed..
#if pin is correct show the menu (amount = 5000, pin = 0000)
#options: check balance, deposit money, withdraw money, exit
#user should be able to perform these activities until he decided to exit the program
import time
amount = 5000
pin = 0000

userPin = (input("Enter your pin number: "))
if userPin != pin:
    print("Your pin address is wrong")
    exit()

else:
    print("""_______________
    Hello We are ABC Bank PLC 
                ___________""")

    print("1. Check balance")
    print("2. Deposit money")
    print("3. Check balance")
    print("4. withdraw money")
    print("5. Exit")

    menuNum = int(input("Enter your menu option: "))
    while True:

        if menuNum == 1:
            time.sleep(10)
            print(f"Your balance is {amount}")
            menuNum = int(input("Enter your menu option: "))

        elif menuNum == 2:
            print(f"Here is the deposit money menu. your balance is: {amount}")
            menuNum = int(input("Enter your menu option: "))
        elif menuNum == 3:
            print(f"Here is the Check balance menu. your balance is: {amount}")
            menuNum = int(input("Enter your menu option: "))
        elif menuNum == 4:
            print(f"Here is the withdraw money menu. your balance is: {amount}")
            withdrawNum = int(input("How much If you want to withdraw: "))
            if withdrawNum >=5000:
                print(f"Your balance has only: {amount}")
            else:
                print("Here is your money. Thank you")
            menuNum = int(input("Enter your menu option: "))
        elif menuNum == 5:
            print(f"Here is the exit menu. Enter the any number more than 5")
            menuNum = int(input("Enter your menu option: "))
        else:
            break
        print("You have already exit menu")

exit()






