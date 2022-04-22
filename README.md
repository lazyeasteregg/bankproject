# bankproject requirements

PROGRAMMING PROJ. #4: Banking Application OOP & Exceptions

Purpose:
Develop a program using what you learn so far.
Apply object-oriented programming in your solution.
Learn how to use exceptions

Description:

Re-write your project 1 using OO design.  You need to create 2 files:
Your main program is defined in “my-bank.py”.  It provides the menu as shown in sample run below. When the user chooses “1. Open Account”, it asks the user for input and create a BankAccount object.  Other options should invoke methods of the BankAccount object.  The main program must keep track of all accounts using a dictionary with account number as the key and BankAccount object as the value.
If an account number does not exist for deposit, withdraw, or show balance, etc… your program should print an error message and should not crash.
Your new class BankAccount must be defined in the file BankAccount.py, it must define the following methods:
__init__(name, initialBalance=0): the constructor takes a name, account number and an initial balance amount and initialize its internal data fields.
deposit (amount): this method takes a deposit amount and update the balance.  If the amount is negative, the method should throw an exception and should not update the balance.  This method needs to save each transaction to show later.
withdraw (amount): this method takes a withdrawal amount and update the balance.  If the amount is greater than the balance, the method should throw an exception.  This method needs to save each transaction to show later.
showBalance(): this method prints the name and current balance.
showTransactions(): this method should show all transactions as output in the sample run below.



Requirements:
You need to have at least 1 function.
The main program must invoke methods of the BankAccount object to make deposit, withdraw, show transactions and show balance.
You can define your own exceptions or utilize exception library.  Make sure you choose the appropriate one.

Hints:
Displaying the menu can be coded as a function.
Use string concatenation to store transactions.
You can keep track of transactions using list of tuple.
Use “\n” to put new line in your string
Use “\t” to put tab key in your string. 
Use datetime.now() to get current time


Sample run:

D:\>python my-bank.py

Welcome to my small bank

Please choose 1 of the following options:
  1. Open an account
  2. Deposit
  3. Withdraw
  4. Show balance
  5. Show transactions
  6. Exit

Enter your option: -1

Invalid selection. Please try it again.

Please choose 1 of the following options:
  1. Open an account
  2. Deposit
  3. Withdraw
  4. Show balance
  5. Show transactions
  6. Exit

Enter your option: 1
Enter the owner’s name: Alexa Amazon
Enter initial balance: $1000
Enter account number: 6543


Please choose 1 of the following options:
  1. Open an account
  2. Deposit
  3. Withdraw
  4. Show balance
  5. Show transactions
  6. Exit

Enter your option: 1
Enter the owner’s name: Siri Apple
Enter initial balance: $500
Enter account number: 1234


Please choose 1 of the following options:
  1. Open an account
  2. Deposit
  3. Withdraw
  4. Show balance
  5. Show transactions
  6. Exit


Enter your option: 2
Enter account number to deposit: 1234
Enter deposit amount: $ 50.00

Please choose 1 of the following options:
  1. Open an account
  2. Deposit
  3. Withdraw
  4. Show balance
  5. Show transactions
  6. Exit

Enter your option: 4
Enter account number to show balace: 1234

Account Owner     Balance
Siri Apple        $550.

Please choose 1 of the following options:
  1. Open an account
  2. Deposit
  3. Withdraw
  4. Show balance
  5. Show transactions
  6. Exit

Enter your option: 3
Enter account number to withdraw: 6543
Enter withdraw amount: $ 100.00

Please choose 1 of the following options:
  1. Open an account
  2. Deposit
  3. Withdraw
  4. Show balance
  5. Show transactions
  6. Exit

Enter your option: 4
Enter account number to show balace: 6543

Account Owner     Balance
Alexa Amazon      $900.00


Please choose 1 of the following options:
  1. Open an account
  2. Deposit
  3. Withdraw
  4. Show balance
  5. Show transactions
  6. Exit


Enter your option: 5
Enter account number to show transactions: 1234


Transaction type   Amount    Date/Time
Deposit            $50.00    2021 Apr 20 16:17:04 


Please choose 1 of the following options:
  1. Open an account
  2. Deposit
  3. Withdraw
  4. Show balance
  5. Show transactions
  6. Exit


Enter your option: 6

Thank you for using my bank application.



