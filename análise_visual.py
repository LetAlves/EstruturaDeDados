import matplotlib.pyplot as plt

def merge_sort_visual(arr, plot_steps=False):
    """
    Modifica o Merge Sort para visualizar as etapas da ordenação.
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort_visual(left, plot_steps)
        merge_sort_visual(right, plot_steps)

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

        # Plot progress if needed
        if plot_steps:
            plt.plot(arr, marker='o')
            plt.title(f'State of Array: {arr}')
            plt.show()
    return arr

# Teste visual
arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort_visual(arr, plot_steps=True)
