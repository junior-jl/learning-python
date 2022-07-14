# As we saw earlier, the Fibonacci sequence is a series of numbers where every number is the sum of the two numbers before it. 
# The first two numbers are 0 and 1:

# 0 1 1 2 3 5 8 13
# You must write the fib() function which takes in a positive integer, n, and returns the n-th Fibonacci number. 
# However, instead of using recursion, your function must use any of the loops.

# My solution

def fib(n): 
    n1 = 0
    n2 = 1
    if n <= 0:
        return -1
    elif n == 1:
        return n1
    elif n == 2:
        return n2
    else:
        i = 3
        result = 0
        while (i <= n):
            result = n1 + n2
            n1 = n2
            n2 = result
            i += 1
        
        return result
            
# Educative solution

def fib(n):
    # The first and second values will always be fixed
    first = 0
    second = 1

    if n < 1:
        return -1

    if n == 1:
        return first

    if n == 2:
        return second

    count = 3  # Starting from 3 because we already know the first two values
    while count <= n:
        fib_n = first + second
        first = second
        second = fib_n
        count += 1  # Increment count in each iteration
    return fib_n
