from Day_14.sampath.current_account import CurrentAccount
from sampath.savings import SavingsAccount
from sampath.user import User
from sampath.account import Account


# user1 = User() ---> Directly import our packages

users = []
accounts = []

def find_user(nic):
    for user in users:
        if user.get_nic() == nic:
            return user
    return None

def list_account():
    if not accounts:
        print("No Accounts created yet.")
    for account in accounts:
        print(f"Account number: {account.get_account_no()} - {account.get_balance()}")

def find_account(account_no):
    for account in accounts:
        if account.get_account_no() == account_no:
            return account
    return None

def cheque_ids():
    cheques = []
    for account in accounts:
        if isinstance(account, CurrentAccount):
            cheques.extend(account.get_cheques())
    for cheque_id in cheques:
        print(cheque_id)

while True:
    print(
        """
        ********************************************
        1.) PRESS 1 TO CREATE A USER
        2.) PRESS 2 TO VIEW CREATED USERS
        3.) PRESS 3 TO CREATE A SAVINGS ACCOUNT
        4.) PRESS 4 TO CREATE A CURRENT ACCOUNT
        5.) PRESS 5 TO LIST ACCOUNTS
        6.) PRESS 6 TO DEPOSIT AMOUNT
        7.) PRESS 7 TO WITHDRAW AMOUNT
        8.) PRESS 8 TO LIST ALL CHEQUE IDS
        ********************************************
        """
    )

    try:
        choice = int(input("Enter user choice: "))
    except ValueError:
        print("Invalid input. Enter a number.")
        continue
    print("****************************************************")
    if choice == 1:
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        nic = input("Enter your NIC number: ")
        user_obj = User(nic, age, name)
        users.append(user_obj)
        #print(users) # [<sampath.user.User object at 0x00000208F9906F90>]
        #print(user_obj) # user values - User name - 23232 - User age - 23 - Nic - sasa

    elif choice == 2:
        if not users:
            print("No users created yet.")
        for user in users:
            print(f"user Nic: {user.get_nic()} - user Name: {user.get_name()} - user Age: {user.get_age()}")

    elif choice == 3:
        account_no = input("Enter Account number: ")
        balance = float(input("Enter Account balance: "))
        branch = input("Enter branch: ")
        atm_card_number = input("Enter card number: ")
        nic = input("Enter NIC number: ")
        user = find_user(nic)

        if user:
            account_obj = SavingsAccount(account_no, balance, branch, user, atm_card_number)
            accounts.append(account_obj)
            print("Account created successfully!")
        else:
            print("No user found with that NIC.")

    elif choice == 4:
        account_no = input("Enter Account number: ")
        balance = float(input("Enter Account balance: "))
        branch = input("Enter branch: ")
        cheque_id = input("Enter Cheque ID: ")
        nic = input("Enter NIC number: ")
        user = find_user(nic)

        if user:
            account_obj = CurrentAccount(account_no, balance, branch, user, [cheque_id])
            accounts.append(account_obj)
            print("Account created successfully!")
        else:
            print("No user found with that NIC.")

    elif choice == 5:
        list_account()


    elif choice == 6:
        account_no = input("Enter Account number: ")  # keep string
        account = find_account(account_no)
        if account:
            deposit_amount = float(input("Enter deposit Amount: "))
            if deposit_amount > 0:
                account.deposit(deposit_amount)
                print(f"Deposited: {deposit_amount}")
            else:
                print("Deposit amount must be greater than zero.")
        else:
            print("Account not found.")

    elif choice == 7:
        account_no = int(input("Enter Account number: "))
        account = find_account(account_no)
        print(isinstance(account, SavingsAccount))
        if account:
            withdraw_amount = float(input("Enter deposit Amount: "))
            if withdraw_amount > 0:
                account.withdraw(withdraw_amount)
                print(f"withdraw: {withdraw_amount}")
            else:
                print("Withdraw amount must be greater than zero.")
        else:
            print("Account not found.")

    elif choice == 8:
        cheque_ids()


