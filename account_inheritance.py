# Import the SavingsAccount and CD classes from the Accounts.py file.
# ADD YOUR CODE HERE
from Accounts import SavingsAccount, CD

# Prompt the user to set the savings balance and interest rate.
# ADD YOUR CODE HERE
savings = float(input("What is the Saving ammout:"))
interest = float(input("what is the interest rate:"))

# Create an instance of the `SavingsAccount` class that sets the users savings account balance and interest.
# ADD YOUR CODE HERE
savings_data = SavingsAccount(savings, interest)


# Prompt the user to set the CD balance, interest rate, and months for the CD.
# ADD YOUR CODE HERE
CD_balance = float(input("What is the CD balance:"))
CD_interest = float(input("what is the interest rate:"))
months = float(input("what is the number of months:"))

# Create an instance of the `CD` class that sets the users cd account balance, interest, and length of months.
# ADD YOUR CODE HERE
cd_data = CD(CD_balance, CD_interest, months)

# Display the savings account data.
print('Here are the details of the savings account.')
print("The balance is: $", format(savings_data.get_balance(), ',.2f'))
print("APR Interest Rate is: ", format(savings_data.get_interest(), ',.2f'),"%")

# Display the CD account data.
print('Here are the details of the CD account.')
print("The balance is: $", format(cd_data.get_balance(), ',.2f'))
print("APR Interest Rate is:", format(cd_data.get_interest(), ',.2f'),'%')
print(f"Length of CD is: {cd_data.get_months()} months.")
