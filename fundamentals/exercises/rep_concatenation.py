# In this exercise, you must implement the rep_cat function. You are given two integers, x and y, as arguments. 
# You must convert them into strings. The string value of x must be repeated 10 times and the string value of y must be repeated 5 times.
# At the end, y will be concatenated to x and the resulting string must returned.

# My solution

def rep_cat(x, y):
    return str(x) * 10 + str(y) * 5

# Educative solution was exactly the same
