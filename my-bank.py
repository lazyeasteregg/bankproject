from newBankAccount import BankAccount
from time import strftime, localtime

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


def picky(account_dictionary):
    transactions = []
    user_choice = 0
    while user_choice != 6:
        try:
            user_choice = show_options()
            print("You entered: ", user_choice, "\n")
        except (RuntimeError, TypeError, NameError):
            print("Please try again. Enter an integer between 1 and 6\n")
        if user_choice == 1:
            owner = input("Enter the owner's name: ")
            acctnum = int(input("Enter the account number: "))
            initialbal = float(input("Enter the initial balance: $ "))
            #try:
            account = BankAccount(owner, acctnum, initialbal)
            if acctnum in account_dictionary:
                print("Account Number: ", acctnum, "already exists")
            else:
                account.customer()
                account_dictionary[acctnum] = account
            #except:
                #print("something didn't work")
    # this elif statement catches when the user enters 2, (Deposit)
        elif user_choice == 2:
            acctnum = int(input("Enter the account number: "))
            value = float(input("Enter the deposit amount: $ "))
            timestamp = strftime("%Y %b %d %H-%M-%S", localtime())
            if acctnum in account_dictionary:
                account.deposit(acctnum, value)
#                transactions.append(tuple(("Deposit" + "\t\t$" + str(value) + "\t\t" + str(timestamp))))
            else:
                print("You need to open an account first")

    # this elif statement catches when the user enters 3, (Withdrawal)
        elif user_choice == 3:
            print(account_dictionary)
            for i, j in account_dictionary.items():
                print(i, " : ",  j)
    # this elif statement catches when the user enters 4, (show balance)
        elif user_choice == 4:
            pass
    # this elif statement catches when the user enters 5, (show transactions)
        elif user_choice == 5:
            acctnum = int(input("Enter the account number: "))
            print(transactions)
        else:
            print("Thank you for using my bank application.\n")

picky({})
