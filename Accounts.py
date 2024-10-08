""" Create a SavingsAccount and CD class with methods"""

class SavingsAccount:
    """Creating a Savings Account class with parameters and methods"""
    def __init__(self, balance, interest): # ADD YOUR CODE HERE
        self.balance = balance
        self.interest = interest

        # ADD YOUR CODE HERE

    # This method gets the balance of the savings account.
    def get_balance(self):
        """Gets the balance for the savings account"""
        # ADD YOUR CODE HERE
        return self.balance

    # This method gets the interest rate of the savings account.
    def get_interest(self):
        """Gets the interest rate for the savings account"""
        # ADD YOUR CODE HERE
        return self.interest

class CD(SavingsAccount):
    """Creating a CD Account class with parameters and methods"""
    def __init__(self, balance, interest, months): # ADD YOUR CODE HERE
       # Call the parent class's __init__ method and pass the required arguments
        #SavingsAccount.__init__(self, balance, interest) 
        super().__init__(balance, interest)
        # ADD YOUR CODE HERE
        self.months = months

    # This method gets the length of months for the CD.
    def get_months(self):
        """Gets the length of the CD"""
        # ADD YOUR CODE HERE
        return self.months
