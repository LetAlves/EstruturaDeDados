def bucket_sort(arr):
    """
    Implementa Bucket Sort para números no intervalo [0, 1).
    """
    n = len(arr)
    buckets = [[] for _ in range(n)]

    for num in arr:
        index = int(num * n)
        buckets[index].append(num)

    for bucket in buckets:
        bucket.sort()

    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(bucket)
    return sorted_array

# Testando Bucket Sort
arr = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12]
print(bucket_sort(arr))  # Saída: [0.12, 0.17, 0.21, 0.26, 0.39, 0.72, 0.78, 0.94]
