import random

def compare_sort_algorithms():
    arr = [random.randint(0, 1000) for _ in range(1000)]

    start = time.time()
    shell_sort(arr[:], [5, 3, 1])
    print("Shell Sort:", time.time() - start)

    start = time.time()
    merge_sort(arr[:])
    print("Merge Sort:", time.time() - start)

    start = time.time()
    quick_sort(arr[:], 0, len(arr) - 1, pivot_strategy="last")
    print("Quick Sort:", time.time() - start)

    start = time.time()
    radix_sort(arr[:])
    print("Radix Sort:", time.time() - start)

# Testando comparação
compare_sort_algorithms()
