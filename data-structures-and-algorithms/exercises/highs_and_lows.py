# You must implement the count_low_high() function. Its parameter is a list of numbers.

# If a number is greater than 50 or divisible by 3, it will count as a high. If these conditions are not met, the number is considered a low.

# At the end of the function, you must return a list that contains the number of lows and highs, in that order.

# In case the list is empty, you may return None.

# My solution

def count_low_high(num_list):
    if len(num_list) == 0:
        return None
    else: # This else is useless.
        low = 0
        high = 0
        for num in num_list:
            if num % 3 == 0 or num > 50:
                high += 1
            else:
                low += 1
    return [low, high]    
  
# Educative has two solution
# First solution uses filter() and lambdas

def count_low_high(num_list):
    if (len(num_list)==0):
        return None
    high_list = list(filter(lambda n: n > 50 or n % 3 == 0, num_list))
    low_list = list(filter(lambda n: n <= 50 and not n % 3 == 0, num_list))
    return [len(low_list), len(high_list)]


# Second solution uses list comprehension (quite good)

def count_low_high(num_list):
    if (len(num_list)==0):
        return None
    high_list = len([n for n in num_list if n > 50 or n % 3 == 0])
    low_list = len([n for n in num_list if n <= 50 and not n % 3 == 0])
    return [low_list, high_list]



