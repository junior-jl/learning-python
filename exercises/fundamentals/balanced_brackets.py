# Given a string containing only square brackets, [], you must check whether the brackets are balanced or not.
# The brackets are said to be balanced if, for every opening bracket, there is a closing bracket.

# You will write your code in the check_balance() function, which returns True if the brackets are balanced and False if they are not.

# For an empty string, the function will return True.

# For the sake of simplicity, you can assume that the string will not contain any other characters.

# My solution

def check_balance(brackets):  # The argument is a string
    count = 0
    for i in brackets:
        if i == '[':
            count += 1
        elif i == ']':
            count -= 1
        if count < 0:
            break
    return count == 0
  
# Educative solution

def check_balance(brackets):
    check = 0
    for bracket in brackets:
        if bracket == '[':
            check += 1

        elif bracket == ']':
            check -= 1

        if check < 0:
            break

    return check == 0
