def interpolation_search(arr, target):
    """
    Busca por interpolação em uma lista ordenada.
    """
    low, high = 0, len(arr) - 1
    while low <= high and arr[low] <= target <= arr[high]:
        pos = low + ((target - arr[low]) * (high - low) // (arr[high] - arr[low]))
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    return -1

# Teste em lista ordenada com intervalos uniformes
uniform_list = [10, 20, 30, 40, 50, 60]
print(interpolation_search(uniform_list, 40))  # Saída: 3

# Teste em lista não uniforme
non_uniform_list = [1, 10, 50, 100, 500, 1000]
print(interpolation_search(non_uniform_list, 500))  # Saída: 4

# O Interpolation Search é mais eficiente em listas com distribuição uniforme, pois faz estimativas baseadas 
#na posição esperada, enquanto a Busca Binária sempre divide ao meio.