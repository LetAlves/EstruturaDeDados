def merge_sort_strings(arr):
    """
    Modifica o Merge Sort para ordenar strings em ordem alfabética.
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort_strings(left)
        merge_sort_strings(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr

# Testando Merge Sort em strings
words = ["banana", "apple", "grape", "orange"]
print(merge_sort_strings(words))  # Saída: ['apple', 'banana', 'grape', 'orange']