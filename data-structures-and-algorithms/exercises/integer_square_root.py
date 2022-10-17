# Write a function that takes a non-negative integer, k, and returns the largest integer whose square
# is less than or equal to the specified integer k.

# Your task is to return the largest integer whose square is less than or equal to the k
# from the function integer_square_root(k) given in the code widget below.
# The input parameter k is a non-negative integer. Make use of a binary search strategy in your solution.

# First solution, using bisect, sqrt and list comprehension (not very good time complexity)

import bisect
from math import sqrt


def integer_square_root(k):
    squares = [x ** 2 for x in range(0, 1000)]
    if k in squares:
        return int(sqrt(k))
    bisect.insort(squares, k)
    return int(sqrt(squares[squares.index(k) - 1]))

# Second solution uses built-in functions

from math import sqrt


def integer_square_root(k):
    y = sqrt(k)
    x = round(y)
    if x <= y:
        return x
    else:
        return x - 1

# Third solution with binary search

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while high >= low:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
    return mid - 1


def integer_square_root(k):
    squares = [x ** 2 for x in range(0, 100)]
    pos = binary_search(squares, k)
    return pos

# Educative solution

def integer_square_root(k):
    low = 0
    high = k

    while low <= high:
        mid = (low + high) // 2
        mid_squared = mid * mid

        if mid_squared <= k:
            low = mid + 1
        else:
            high = mid - 1
    return low - 1