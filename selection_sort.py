def selection_sort(arr):
    """
    Implementa Selection Sort, mostrando iterações.
    """
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(f"Iteração {i + 1}: {arr}")
    return arr

# Testando Selection Sort
arr = [64, 25, 12, 22, 11]
print("Ordenado:", selection_sort(arr))

#Selection Sort funciona melhor em listas pequenas devido ao número fixo de comparações.