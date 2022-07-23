# In this coding exercise, you are required to use the stack data structure to convert integer values to their binary equivalent.

# My solution

from stack import Stack


def stack_to_string(stack):
    string = ""
    while not stack.is_empty():
        string += str(stack.pop())
    return string


def convert_int_to_bin(dec_num):
    stack = Stack()
    while dec_num != 0:
        stack.push(dec_num % 2)
        dec_num //= 2
    return stack_to_string(stack)


# Educative solution was better as it works for 0. Mine doesn't... And if the input is negative, Educative solution does nothing and mine goes into a loop.

def convert_int_to_bin(dec_num):
    
    if dec_num == 0:
        return 0
    
    s = Stack()

    while dec_num > 0:
        remainder = dec_num % 2
        s.push(remainder)
        dec_num = dec_num // 2

    bin_num = ""
    while not s.is_empty():
        bin_num += str(s.pop())

    return bin_num

print(convert_int_to_bin(56))
print(convert_int_to_bin(2))
print(convert_int_to_bin(32))
print(convert_int_to_bin(10))

print(int(convert_int_to_bin(56),2)==56)

# This last line will print True if convert_int_to_bin(56) returns the correct binary equivalent for 56. We convert the returned value from 
# convert_int_to_bin(56) to an integer value by specifying base 2 of the returned value. 
# It will convert to 56 if it’s equal to 56 in binary format. Otherwise, the statement will print False if we get some number other than 56.
