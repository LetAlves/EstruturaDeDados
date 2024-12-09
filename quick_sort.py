def quick_sort(arr, low, high, pivot_strategy="last"):
    """
    Implementa o Quick Sort usando diferentes estratégias de pivô.
    """
    if low < high:
        pi = partition(arr, low, high, pivot_strategy)
        quick_sort(arr, low, pi - 1, pivot_strategy)
        quick_sort(arr, pi + 1, high, pivot_strategy)

def partition(arr, low, high, pivot_strategy):
    if pivot_strategy == "first":
        pivot = arr[low]
    elif pivot_strategy == "middle":
        pivot = arr[(low + high) // 2]
    else:
        pivot = arr[high]
    pivot_index = low if pivot_strategy == "first" else (low + high) // 2 if pivot_strategy == "middle" else high

    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Testando Quick Sort com diferentes estratégias de pivô
arr = [10, 7, 8, 9, 1, 5]
quick_sort(arr, 0, len(arr) - 1, pivot_strategy="last")
print("Quick Sort (último pivô):", arr)  # Saída: [1, 5, 7, 8, 9, 10]
