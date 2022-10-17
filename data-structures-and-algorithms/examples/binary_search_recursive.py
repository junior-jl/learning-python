A = [1, 2, 3, 5, 8, 11, 22, 1923, 33456]


def binary_search_recursive(arr, target, low, high):
    if high < low:
        return False
    else:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binary_search_recursive(arr, target, mid + 1, high)
        else:
            return binary_search_recursive(arr, target, low, mid - 1)

