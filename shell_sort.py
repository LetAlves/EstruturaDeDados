def shell_sort(arr, gaps):
    """
    Implementa Shell Sort usando uma sequência de intervalos.
    """
    n = len(arr)
    for gap in gaps:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
    return arr

# Testando Shell Sort com diferentes sequências
arr = [34, 8, 64, 51, 32, 21]
print(shell_sort(arr[:], [5, 3, 1]))  # Sequência de Shell
print(shell_sort(arr[:], [4, 2, 1]))  # Sequência personalizada

#Escolher intervalos maiores no início reduz desordens globais, 
#enquanto intervalos menores no final refinem a ordenação.