A = [1, 2, 3, 5, 8, 11, 22, 1923, 33456]


# Pego o elemento do meio
# Checo se é menor que o alvo
#   Se sim, elimino a parte esquerda do vetor
#   Se não:
#       Se for maior, elimino a parte direita do vetor
#       Se for igual, retorna elemento

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
    return False


