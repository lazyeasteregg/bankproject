from time import strftime, localtime

class Bank:
    def __init__(self, name, accountnumber, initialBalance = 0):
        self.name = name
        self.accountnum = accountnumber
        self.balance = initialBalance
        self.txlog = {}
        self.tstamp = strftime("%Y %b %d %H-%M-%S", localtime())

    def open_acct(self):
        return "name: {} \t account: {} \t balance: ${} \t date: {}".format(self.name, self.accountnum, self.balance, self.tstamp)

    def tslog(self):
        tx = tuple([self.balance, self.tstamp])
        self.txlog[self.accountnum] = {self.name, tx}

    def visitor(self):
        return "{} {} {}".format(self.name, self.accountnum, self.balance)


user1 = Bank("john", 87324, 9831)

#print(user1.open_acct())
print(user1.tslog())