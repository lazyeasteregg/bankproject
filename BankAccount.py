from time import strftime, localtime
class Account:
    """ Constructor """
    def __init__(self, name, account_number, initialBalance=0):
         self.trans = "Created"
         self.myname = name
         self.account_num = account_number
         self.balance = initialBalance
         self.txlog = []

    def deposit(self, account_num, value):
        self.balance += value
#        self.account_number = account_number
        time = strftime("%Y %b %d %H-%M-%S", localtime())
        trans = "Deposit"
        self.txlog = (trans, self.balance, time)

    def showlog(self):
        for i in self.txlog:
            print(i)

    def withdraw(self, account_number, value, time):
        self.initialBalance -= value
        self.account_number = account_number
        self.time = time
        self.trans = "Withdrawal"

#    def transactions(self):
#        self.txlog[self.account_num] = (Account.deposit.trans, self.balance, Account.deposit.time)

class Accounts:
    def __init__(self):
        self.by_name = {}
        self.by_number = {}
        self.status = False
        self.presence = False

    def get_by_name(self, name):
        return self.by_name(name)

    def get_by_number(self, number):
        name = self.by_number(number)
        if name is None:
            return
        return self.get_by_name(name)

    def present(self, number):
        if number in self.by_number:
            self.presence = True
        else:
            print("You haven't added this account yet")

    def check(self, name, number):
        if number in self.by_number:
             print("You already have an account with the number:", number)
        else:
            self.by_number[number] = name
            self.status = True

#    def __str__(self):

