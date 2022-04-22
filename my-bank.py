from BankAccount import Account, Accounts
from time import strftime, gmtime

def show_options():
    """
    Display all options and return user's choice
    :return: the user's choice
    """
    menu = """\t Welcome to My Small Banking App
              \t1. Open account
              \t2. Deposit 
              \t3. Withdraw
              \t4. Show balance
              \t5. Show transactions
              \t6. Exit \n Your choice: """
    try:
        valid_input = int(input(menu))
    except (ValueError, TypeError, NameError):
        print("Invalid input")
    return valid_input


def nicebal(x):
        """
        A formatting function to take an input and make it print with two decimal places
        :param x: X will be a float, in this program usually balance, withdrawal, or deposit
        :return:
        """
        twodecimals = "{:.2f}".format(x)
        return twodecimals

def txlog(account, balance):
    transactions = ()
    timestamp = strftime("%Y %b %d %H-%M-%S", gmtime())
    entry = list([timestamp, balance])
    transactions.add(account, entry)
    return transactions

def choosy():
    accounts = Accounts()
    user_choice = 0
    while user_choice != 6:
        try:
            user_choice = show_options()
            print("You entered: ", user_choice, "\n")
        except (RuntimeError, TypeError, NameError):
            print("Please try again. Enter an integer between 1 and 6\n")
        if user_choice == 1:
            owner = input("Enter the owner's name: ")
            user = owner
            acctnum = input("Enter the account number: ")
            initialbal = float(input("Enter the initial balance: $ "))
            #try:
            accounts.check(owner, acctnum)
            if accounts.status:
                user = Account(owner, acctnum, initialbal)

            else:
                print("Something's wrong with the Accounts")
            #except:
                #print("something didn't work")
    # this elif statement catches when the user enters 2, (Deposit)
        elif user_choice == 2:
            account_num = int(input("Enter the account number: "))
            value = float(input("Enter the deposit amount: $ "))
#            timestamp = strftime("%Y %b %d %H-%M-%S", gmtime())
            if accounts.status:
                user.deposit(account_num, value)

    # this elif statement catches when the user enters 3, (Withdrawal)
        elif user_choice == 3:
            pass
    # this elif statement catches when the user enters 4, (show balance)
        elif user_choice == 4:
            pass
    # this elif statement catches when the user enters 5, (show transactions)
        elif user_choice == 5:
            user.showlog()
        else:
            print("Thank you for using my bank application.\n")

choosy()

"""
problems with my program: 
- tx log has \n per entry, rather than one line 
- tx log doesn't distinguish between accounts 
- time stamp is in GMT; i need to print in PST (maybe fixed?)
- need to look at the course program from unit 3
- use a list of tuples for txlog: time and amount

"""