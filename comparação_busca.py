import time

def compare_search_algorithms(arr, target):
    start = time.time()
    binary_search(arr, target)
    print("Binary Search:", time.time() - start)

    start = time.time()
    interpolation_search(arr, target)
    print("Interpolation Search:", time.time() - start)

    start = time.time()
    jump_search(arr, target)
    print("Jump Search:", time.time() - start)

    start = time.time()
    exponential_search(arr, target)
    print("Exponential Search:", time.time() - start)

# Testando comparações
arr = list(range(1, 1000000))
compare_search_algorithms(arr, 999999)
