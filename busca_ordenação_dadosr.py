def bucket_sort_grades(grades):
    """
    Ordena notas de 0 a 100 usando Bucket Sort.
    """
    buckets = [[] for _ in range(10)]
    for grade in grades:
        index = grade // 10
        buckets[index].append(grade)

    for bucket in buckets:
        bucket.sort()

    sorted_grades = []
    for bucket in buckets:
        sorted_grades.extend(bucket)
    return sorted_grades

grades = [85, 92, 75, 63, 70, 88, 94]
print(bucket_sort_grades(grades))  # Saída: [63, 70, 75, 85, 88, 92, 94]

print(interpolation_search(grades, 75))  # Saída: índice da nota (após ordenar)
