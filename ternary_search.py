def ternary_search(arr, low, high, target):
    """
    Implementa Ternary Search em uma lista ordenada.
    """
    if low > high:
        return -1

    mid1 = low + (high - low) // 3
    mid2 = high - (high - low) // 3

    if arr[mid1] == target:
        return mid1
    if arr[mid2] == target:
        return mid2

    if target < arr[mid1]:
        return ternary_search(arr, low, mid1 - 1, target)
    elif target > arr[mid2]:
        return ternary_search(arr, mid2 + 1, high, target)
    else:
        return ternary_search(arr, mid1 + 1, mid2 - 1, target)

# Testando Ternary Search
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(ternary_search(arr, 0, len(arr) - 1, 5))  # Saída: 4

#Embora menos eficiente em média, Ternary Search pode ser útil 
#em arquiteturas onde divisões em três partes são mais otimizadas.