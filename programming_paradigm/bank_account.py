class BankAccount:  # A simple bank account class to demonstrate object-oriented programming principles
    def __init__(self, account_balance=0):
        self.account_balance = account_balance # Initialize the account with a account_balance of 0

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
        else:
            raise ValueError("Deposit amount must be positive") # Ensure that the deposit amount is positive

    def withdraw(self, amount):
        if amount > 0 and amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self, ):
        return self.account_balance
          # Display the account balance in the specified currency, defaulting to USD

