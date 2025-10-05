from day_14.sampath.account import Account


class CurrentAccount(Account):
    def __init__(self, account_no, balance, branch, user, check_id):
        Account.__init__(self, account_no, balance, branch, user)
        self.__check_id = check_id

    def set_cheques(self, check_id):
        self.__check_id = check_id

    def get_cheques(self):
        return self.__check_id

    def set_cheque_ids(self, cheque_ids):
        self.__check_id = cheque_ids

    def get_cheque_ids(self):
        return self.__check_id
