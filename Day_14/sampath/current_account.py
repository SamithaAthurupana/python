from account import Account

class CurrentAccount(Account):
    def __init__(self, account_no, balance, branch, user, check_id):
        Account.__init__(self, account_no, balance, branch, user)
        self.__check_id = check_id

    def set_cheques(self, check_id):
        self.__check_id = check_id

    def get_cheques(self):
        return self.__check_id
