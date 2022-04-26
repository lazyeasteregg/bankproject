#from time import strftime, localtime

class BankAccount:
    def __init__(self, name, accountnumber, initialBalance = 0):
        self.name = name
        self.accountnum = accountnumber
        self.balance = initialBalance
        self.acctlog = []
        self.openacct = None
#        self.tstamp = strftime("%Y %b %d %H-%M-%S", localtime())

#    def tslog(self):
#        tx = tuple([self.balance, self.tstamp])
#        self.txlog[self.accountnum] = tx

    def customer(self):
        self.openacct = BankAccount(self.name, self.accountnum, self.balance)
        self.acctlog.append((self.name, self.balance))

#        return "Name: {} \t\tAccount: {} \t\tBalance: ${}".format(self.name, self.accountnum, self.balance)


    def deposit(self, accountnumber, amount):
        self.accountnum = accountnumber
        self.balance += amount
        self.acctlog.append((self.name, self.balance))
#        self.acctlog[self.accountnum] = (self.name, self.balance)


    def withdrawal(self, accountnumber, amount):
        self.accountnum = accountnumber
        self.balance -= amount
        self.acctlog.append((self.name, self.balance))
#        self.acctlog[self.accountnum] = (self.name, self.balance)


# this works!
#user1 = BankAccount("john", 87324, 9831)
#user2 = BankAccount("frank", 1234, 20)

#user1.customer()
#user2.customer()
#print(user1.acctlog[87324])
#if user1.name in user1.acctlog[87324]:
#    print("got it")
# print(user2.txlog[1234])
# # so, tslog has to run before txlog
# #
# user1.deposit(87324, 10000)
# #print(user1.txlog)
# user2.deposit(1234, 10000)
# #print(user2.txlog)
# user1.withdrawal(87324, 3000)
# user2.withdrawal(1234, 3000)
# print(user1.txlog)
# #print(user2.txlog)
