# Write a function that determines the index of the smallest element of the cyclically shifted array.

# An array is “cyclically shifted” if it is possible to shift its entries cyclically so that it becomes sorted.

# The following list is an example of a cyclically shifted array:

# A = [4, 5, 6, 7, 1, 2, 3]

# Your task is to return the index of the smallest number in the list A (cyclically shifted array)
# from the function find(A) given in the code widget below.

def find(A):
    low = 0
    high = len(A) - 1
    while high > low:
        mid = (low + high) // 2
        if A[mid] > A[high]:
            low = mid + 1
        elif A[mid] < A[high]:
            high = mid

    return low


print(find([1, 2, 3, 4, 5, 6, 7]))
print(find([2, 3, 4, 5, 6, 7, 1]))
print(find([3, 4, 5, 6, 7, 1, 2]))
print(find([4, 5, 6, 7, 1, 2, 3]))
print(find([5, 6, 7, 1, 2, 3, 4]))
print(find([6, 7, 1, 2, 3, 4, 5]))
print(find([7, 1, 2, 3, 4, 5, 6]))


