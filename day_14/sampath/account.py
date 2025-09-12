class Account:
    def __init__(self, account_no, balance, branch, user):
        self.__account_no = account_no
        self.__balance = balance
        self.__branch = branch
        self.__user = user

    def set_account_no(self, account_no):
        self.__account_no = account_no
    def get_account_no(self):
        return self.__account_no

    def set_balance(self, balance):
        self.__balance = balance
    def get_balance(self):
        return self.__balance

    def set_branch(self, branch):
        self.__branch = branch
    def get_branch(self):
        return self.__branch

    def set_user(self, user):
        self.__user = user
    def get_user(self):
        return self.__user

    def check_balance(self):
        print(f"Here is your current account balance ${self.__balance}")

    def deposit(self, deposit_amount):
        self.__balance = self.__balance() + deposit_amount

    def withdraw(self, withdraw_amount):
        self.__balance -= withdraw_amount

        # account1 = SampathBank(12344, 300, "horana")
        # print(account1.account_no) --->
        # we can access anything did we encapsulate some variables,
        # but we can use getters and setters

    '''def deposit(self, deposit_amount):
        self.set_balance(self.get_balance() + deposit_amount)'''
    # this is public method