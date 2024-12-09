import math

def jump_search(arr, target):
    """
    Implementa Jump Search em uma lista ordenada.
    """
    n = len(arr)
    step = int(math.sqrt(n))  # Tamanho do salto ideal
    prev, curr = 0, 0

    while curr < n and arr[curr] < target:
        prev = curr
        curr += step

    for i in range(prev, min(curr, n)):
        if arr[i] == target:
            return i
    return -1

# Testando Jump Search
sorted_list = [2, 4, 6, 8, 10, 12, 14]
print(jump_search(sorted_list, 10))  # Saída: 4

#Jump Search funciona bem em listas grandes, quando é vantajoso pular blocos em vez de dividir pela metade.