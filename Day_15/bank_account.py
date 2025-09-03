class BankAccount:
    def __init__(self, owner:str, account_balance: float):
        self.__owner = owner
        self.__account_balance = account_balance

    def get_owner_infor(self):
        return self.__owner

    def get_account_balance(self):
        return self.__account_balance

acc = BankAccount("Kamal", 5000.0)
print(acc.get_owner_infor())      # Kamal
print(acc.get_account_balance())  # 5000.0
