# In this exercise, you have to implement a calculator that can perform addition, subtraction, multiplication, and division.

# My solution

class Calculator:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2
    
    def subtract(self):
        return self.num2 - self.num1

    def multiply(self):
        return self.num1 * self.num2
    
    def divide(self):
        return self.num2 / self.num1
      
# Educative solution is exactly the same
