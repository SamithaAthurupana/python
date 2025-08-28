# python bank

def show_balance(balance):
    print(f"Your balance is ${balance:.2f}")

def deposit():
    amount = float(input("Enter a amount to be deposit: $"))

    if amount < 0:
        print("that's not a valid amount!")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter a amount to be withdrawn: $"))

    if amount > balance:
        print("Insufficient funds")
        return 0
    elif amount < 0:
        print("amount must be grater than 0")
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("""
              =======BANKING PROGRAM=========
              1.) PRESS 1 TO SHOW BALANCE
              2.) PRESS 2 TO DEPOSIT
              3.) PRESS 3 TO WITHDRAW
              4.) PRESS 4 FOR EXIT
              ===============================
        """)
        choice = int(input("Enter your choice: "))

        if choice == 1:
            show_balance(balance)
        elif choice == 2:
            balance += deposit()
        elif choice == 3:
            balance -= withdraw(balance)
        elif choice == 4:

            is_running = False
        else:
            print("That is not valid choice!")

    print("Thank you! have a nice day!")


if __name__ == '__main__':
    main()