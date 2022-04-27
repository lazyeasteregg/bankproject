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


def picky(account_dictionary):
    user_choice = 0
    acctnum = None
    while user_choice != 6:
        try:
            user_choice = show_options()
            print("You entered: ", user_choice, "\n")
        except (RuntimeError, TypeError, NameError):
            print("Please try again. Enter an integer between 1 and 6\n")
        if user_choice == 1:
            acctnum = input("Enter the account number: ")
            if acctnum in account_dictionary:
                print("Account Number: ", acctnum, "already exists")
            else:
                owner = input("Enter the owner's name: ")
                try:
                    initialbal = float(input("Enter the initial balance: $ "))
                except:
                    print("please enter a number")
                account = BankAccount(owner, acctnum, initialbal)
                account_dictionary[acctnum] = account
    # this elif statement catches when the user enters 2, (Deposit)
        elif user_choice == 2:
            acctnum = input("Enter the account number: ")
            account = account_dictionary.get(acctnum)
            if account is None:
                raise Exception("Account number doesn't exist")
            else:
                try:
                    value = float(input("Enter the deposit amount: $ "))
                    if value < 0:
                        print("Please enter a positive number")
                    else:
                        account.deposit(value)
                except:
                    print("please enter a number")

    # this elif statement catches when the user enters 3, (Withdrawal)
        elif user_choice == 3:
            acctnum = input("Enter the account number: ")
            account = account_dictionary.get(acctnum)
            if account is None:
                raise Exception("Account number doesn't exist")
            else:
                value = float(input("Enter the withdrawal amount: $ "))
                if str(account.balance) < str(value):
                    print("You can't withdraw more than you have")
                elif str(value) < str(0):
                    print("You can't withdraw a negative amount")
                else:
                    account.withdrawal(value)

    # this elif statement catches when the user enters 4, (show balance)
        elif user_choice == 4:
            acctnum = input("Enter the account number: ")
            account = account_dictionary.get(acctnum)
            if account is None:
                raise Exception('does not exist')
            print(f'${account.balance:.02f}')
    # this elif statement catches when the user enters 5, (show transactions)
        elif user_choice == 5:
            acctnum = input("Enter the account number: ")
            account = account_dictionary.get(acctnum)
            if account is None:
                raise Exception('does not exist')
            else:
                account.list_transactions()

picky({})
