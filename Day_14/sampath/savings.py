from account import Account

class SavingsAccount(Account):
    def __init__(self, account_no, balance, branch, user, atm_card_id):
        Account.__init__(self, account_no, balance, branch, user)
        self.atm_card_id = atm_card_id

    def check_balance(self):
        print(f"Checking balance of {self.atm_card_id} - has balance - {self.get_balance()}")
