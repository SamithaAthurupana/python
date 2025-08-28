from sampath.savings import SavingsAccount
from sampath.user import User
from sampath.account import Account
# user1 = User() ---> Directly import our packages

'''user_01 = User("1234567890V", 34, "sadun")
print(user_01.get_nic())

account_01 = Account("22345678902", 3000, "moratuwa", user_01)
print(account_01.get_user().get_name())
# account object ---> user object           this is composition 
print(account_01.get_account_no())

'''

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
        1.) Press 1 to create an user account
        2.) Press 2 to view created Accounts
        2.) Press 2 to create an Account
        
        """
    )



    choice = int(input("Enter user choice: "))

    if choice == 1:
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        nic = input("Enter your nic number: ")
        user_obj = User(nic, age, name) # create a object User Constructor
        users.append(user_obj)
        #print(users) # [<sampath.user.User object at 0x00000208F9906F90>]
        #print(user_obj) # user values - User name - 23232 - User age - 23 - Nic - sasa

    if choice == 2:
        for user in users:
            print(user.get_nic())

    if choice == 3:
        account_no = int(input("Enter Account number: "))
        balance = float(input("Enter Account balance:  "))
        branch = input("Enter branch: ")
        atm_card_number = int(input("Enter card number: "))
        nic = int(input("Enter nic number: "))
        user = find_user(nic)

        if user:
            account_obj = SavingsAccount(account_no, balance, branch, user, atm_card_number)
            accounts.append(account_obj)


