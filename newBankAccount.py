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
        print("Transaction type\t Amount \t\t\t Date")
        for type_, value, ts in self.acctlog:
            print(f'{type_} \t\t\t${value:.02f} \t\t\t\t{ts.strftime("%Y %b %d, %H:%M:%S")}')
