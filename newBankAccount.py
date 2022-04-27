#from time import strftime, localtime
from datetime import datetime

class BankAccount:
    def __init__(self, name, accountnumber, initialBalance = 0):
        self.name = name
        self.accountnum = accountnumber
        self.balance = initialBalance
        self.acctlog = []
        self.openacct = None


    def deposit(self, amount):
        self.balance += amount
        self.acctlog.append(("Deposit", amount, datetime.now()))


    def withdrawal(self, amount):
        self.balance -= amount
        self.acctlog.append(("Withdrawal", amount, datetime.now()))

    def list_transactions(self):
        for type_, value, ts in self.transactions:
            print(f'{type_} ${value:.02f} {ts.strftime("%Y-%m-%d")}')
