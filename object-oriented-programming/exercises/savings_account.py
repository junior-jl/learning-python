# In this challenge, you will implement a banking account using the concepts of inheritance.
# Implement the basic structure of a parent class, Account, and a child class, SavingsAccount.
# Implement properties as instance variables, and set them to None or 0.
# Account has the following properties:
# title
# balance
# SavingsAccount has the following properties:
# interestRate
# Create an initializer for Account class. The order of parameters should be the following, where Mark is the title, and 5000 is the account balance:
# Account("Mark", 5000)
# Implement properties as instance variables, and set them to None or 0.
# Create an initializer for the SavingsAccount class using the initializer of the Account class in the order below:
# Account("Mark", 5000, 5)

# My solution

class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance


class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate
        

# Educative solution is the same.
