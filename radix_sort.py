def counting_sort_for_radix(arr, exp):
    """
    Subfunção do Radix Sort para ordenar com base no dígito significativo (exp).
    """
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for num in arr:
        index = (num // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    """
    Implementa o Radix Sort para números inteiros.
    """
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10
    return arr

# Testando Radix Sort
arr = [170, 45, 75, 90, 802, 24, 2, 66]
print(radix_sort(arr))  # Saída: [2, 24, 45, 66, 75, 90, 170, 802]
