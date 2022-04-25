from newBankAccount import Bank

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


def picky():
    user_choice = 0
    while user_choice != 6:
        try:
            user_choice = show_options()
            print("You entered: ", user_choice, "\n")
        except (RuntimeError, TypeError, NameError):
            print("Please try again. Enter an integer between 1 and 6\n")
        if user_choice == 1:
            owner = input("Enter the owner's name: ")
            acctnum = input("Enter the account number: ")
            initialbal = float(input("Enter the initial balance: $ "))
            #try:
            myuser = Bank(owner, acctnum, initialbal)
            if myuser.txlog[acctnum]:
                print("Account Number: ", acctnum, "already exists")
            else:
                myuser.tslog()
            #except:
                #print("something didn't work")
    # this elif statement catches when the user enters 2, (Deposit)
        elif user_choice == 2:
            acctnum = int(input("Enter the account number: "))
            value = float(input("Enter the deposit amount: $ "))
            if acctnum in myuser.txlog[acctnum]:
                myuser.deposit(acctnum, value)
            else:
                print("You need to open an account first")

    # this elif statement catches when the user enters 3, (Withdrawal)
        elif user_choice == 3:
            pass
    # this elif statement catches when the user enters 4, (show balance)
        elif user_choice == 4:
            pass
    # this elif statement catches when the user enters 5, (show transactions)
        elif user_choice == 5:
            print(myuser.txlog())
        else:
            print("Thank you for using my bank application.\n")

picky()

"""
problems with my program: 
- tx log has \n per entry, rather than one line 
- tx log doesn't distinguish between accounts 
- time stamp is in GMT; i need to print in PST (maybe fixed?)
- need to look at the course program from unit 3
- use a list of tuples for txlog: time and amount

"""