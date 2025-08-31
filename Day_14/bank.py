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

while True:
    print(
        """
        ********************************************
        1.) Press 1 to create a User
        2.) Press 2 to view created Users
        3.) Press 3 to create an Savings Account
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
            print(user.get_nic())

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


