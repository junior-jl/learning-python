# In this challenge, you must implement the factorial() function. It takes an integer as a parameter and calculates its factorial.
# Python does have a built-in factorial function but you’ll be creating your own for practice.

# My solution

def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    elif n < 0:
        return -1
    else:
        return n * factorial(n - 1)

# Educative solution

def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1

    if n < 0:
        return -1
    # Recursive call
    return n * factorial(n - 1)

