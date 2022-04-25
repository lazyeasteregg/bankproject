from time import strftime, localtime

class Bank:
    txlog = {}
    def __init__(self, name, accountnumber, initialBalance = 0):
        self.name = name
        self.accountnum = accountnumber
        self.balance = initialBalance
        self.tstamp = strftime("%Y %b %d %H-%M-%S", localtime())

#    def open_acct(self):
#        return "name: {} \t account: {} \t balance: ${} \t date: {}".format(self.name, self.accountnum, self.balance, self.tstamp)

    def tslog(self):
        tx = tuple([self.balance, self.tstamp])
        self.txlog[self.accountnum] = tx

    def customer(self):
        return "Name: {} \t\tAccount: {} \t\tBalance: ${}".format(self.name, self.accountnum, self.balance)

    def deposit(self, accountnumber, amount):
        self.accountnum = accountnumber
        self.balance += amount
        self.tslog()

    def withdrawal(self, accountnumber, amount):
        self.accountnum = accountnumber
        self.balance -= amount
        self.tslog()

# this works!
#user1 = Bank("john", 87324, 9831)
#user1.tslog()
#print(user1.txlog[87324])
# so, tslog has to run before txlog
#
#user1.deposit(87324, 10000)
#print(user1.txlog)
#user1.withdrawal(87324, 3000)
#print(user1.txlog)
#print(user1.visitor())
