# You must implement the check_sum() function which takes in a list and returns True if the sum of two numbers in the list is zero.
# If no such pair exists, return False.

# My solution

def check_sum(num_list):
    for n1 in num_list:
        for n2 in num_list:
            if n1 + n2 == 0:
                return True
    return False
    
# Educative solution

def check_sum(num_list):
    for first_num in range(len(num_list)):
        for second_num in range(first_num + 1, len(num_list)):
            if num_list[first_num] + num_list[second_num] == 0:
                return True
    return False


