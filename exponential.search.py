def exponential_search(arr, target):
    """
    Implementa Exponential Search em uma lista ordenada.
    Combina Jump Search para expandir o intervalo e Binary Search no intervalo reduzido.
    """
    if arr[0] == target:
        return 0

    n = len(arr)
    bound = 1

    # Expande o intervalo exponencialmente
    while bound < n and arr[bound] < target:
        bound *= 2

    # Realiza busca binária no intervalo encontrado
    low = bound // 2
    high = min(bound, n - 1)
    return binary_search(arr[low:high + 1], target) + low

# Testando Exponential Search
sorted_list = [2, 4, 6, 8, 10, 12, 14, 16, 18]
print(exponential_search(sorted_list, 10))  # Saída: 4
print(exponential_search(sorted_list, 20))  # Saída: -1

#Exponential Search usa a expansão exponencial para encontrar rapidamente o intervalo onde o elemento pode 
#estar. Depois, aplica a busca binária para localizar o índice.