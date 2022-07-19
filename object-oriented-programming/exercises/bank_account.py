# In this challenge, we will be extending the previous challenge and implementing methods in the parent class and its corresponding child class.

# In the Account class, implement the getBalance() method that returns balance.
# In the Account class, implement the deposit(amount) method that adds amount to the balance. It does not return anything.
# In the Account class, implement the withdrawal(amount) method that subtracts the amount from the balance. It does not return anything.
# In the SavingsAccount class, implement an interestAmount() method that returns the interest amount of the current balance. Below is the 
# formula for calculating the interest amount:
# interest amount = (interest rate * balance) / 100

# My solution

class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance

    def withdrawal(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def getBalance(self):
        return self.balance


class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate

    def interestAmount(self):
        return (self.interestRate * self.balance) / 100

# Educative solution was basically the same.
# code to test - do not edit this
demo1 = SavingsAccount("Mark", 2000, 5)  # initializing a SavingsAccount object
