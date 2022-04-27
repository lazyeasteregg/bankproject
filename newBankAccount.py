"""
Name: Stacy Chen
Date: 4/19/2022
Description: A simple banking application that illustrates object-oriented programming and exceptions
"""
from datetime import datetime

class BankAccount:
    def __init__(self, name, accountnumber, initialBalance = 0):
        """
        the init function is the Constructor
        :param name: the owner of the account
        :param accountnumber: the account number
        :param initialBalance: the starting balance. default is 0
        """
        self.name = name
        self.accountnum = accountnumber
        self.balance = initialBalance
        self.acctlog = []
        self.openacct = None


    def deposit(self, amount):
        """
        the deposit function
        :param amount: the amount you want to deposit
        :return:
        """
        self.balance += amount
        self.acctlog.append(("Deposit", amount, datetime.now()))


    def withdrawal(self, amount):
        """
        the withdrawal function
        :param amount: the amount you want to withdraw
        :return:
        """
        self.balance -= amount
        self.acctlog.append(("Withdrawal", amount, datetime.now()))


    def list_transactions(self):
        """
        the transaction log
        :return:
        """
        print("Transaction type\t Amount \t\t\t Date")
        for type_, value, ts in self.acctlog:
            print(f'{type_} \t\t\t${value:.02f} \t\t\t\t{ts.strftime("%Y %b %d, %H:%M:%S")}')
