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
        else:
            raise ValueError("Withdrawal amount must be positive and less than or equal to the account_balance") # Ensure that the withdrawal amount is positive and does not exceed the account_balance
            return False

    def display_balance(self, currency='USD'):
        return f"Current Balance: {self.account_balance} {currency}"
          # Display the account balance in the specified currency, defaulting to USD

