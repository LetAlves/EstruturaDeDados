def binary_search(arr, target):
    """
    Realiza busca binária em uma lista ordenada.
    Retorna o índice do elemento ou -1 se não encontrado.
    """
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Exemplo de uso:
sorted_list = [2, 4, 6, 8, 10, 12, 14]
print(binary_search(sorted_list, 8))  # Saída: 3
print(binary_search(sorted_list, 5))  # Saída: -1

#A busca binária funciona apenas em listas ordenadas, porque o algoritmo utiliza a ordenação 
#para reduzir o espaço de busca pela metade a cada iteração.

# Em uma lista desordenada, as comparações com mid não teriam sentido.

unsorted_list = [10, 2, 8, 4]
print(binary_search(unsorted_list, 8))  # Resultado incorreto.
