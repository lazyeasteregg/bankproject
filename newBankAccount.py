from time import strftime, localtime

class Bank:
    def __init__(self, name, accountnumber, initialBalance = 0):
        self.name = name
        self.accountnum = accountnumber
        self.balance = initialBalance
        tstamp = strftime("%Y %b %d %H-%M-%S", localtime())
        self.openlog = {self.name, self.accountnum, self.balance, tstamp}

#    def open_acct(self):
#       tstamp = strftime("%Y %b %d %H-%M-%S", localtime())

user1 = Bank("john", 87324, 9831)
print(user1.openlog)
#print(user1.tstamp)