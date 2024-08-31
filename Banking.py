# Import the BankAccount class from the BankAccount file.
# ADD YOUR CODE HERE
from bankaccount import BankAccount

# Prompt the user to set the starting balance.
starting_balance = float(input('Enter your starting balance: '))

# Create an instance of the `BankAccount` class that sets the users starting balance.
# ADD YOUR CODE HERE
savings = BankAccount(starting_balance)


# Prompt the user to deposit their paycheck.
pay = float(input('How much were you paid this week? '))
print('I will deposit $', format(pay, ',.2f'),'into your account.')

# Pass the users pay to the deposit method using the instance of the BankAccount class.
# ADD YOUR CODE HERE
#deposit = BankAccount.deposit(pay)
savings.deposit(pay)
# Display the balance and format the amount to two decimal places and thousands.
# ADD YOUR CODE HERE
#New_Balance = BankAccount.get_balance(starting_balance + deposit)
#print(f"the New Balance is ${New_Balance: , 2f}")
print(f"Your account balance ${savings.get_balance(): ,.2f}")
# Prompt the user to withdraw and amount.
cash = float(input('How much would you like to withdraw? '))
print('I will withdraw $', format(cash, ',.2f'),'from your account.')

# Pass the users amount they want to the withdraw method using the instance of the BankAccount class.
# ADD YOUR CODE HERE
savings.withdraw(cash)

# Display the balance and format the amount to two decimal places and thousands.
# ADD YOUR CODE HER
print(f"The new Balance after withdrawal is ${savings.get_balance(): ,.2f}")
