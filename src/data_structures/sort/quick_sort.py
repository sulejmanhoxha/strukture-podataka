def quick_sort(arr, low, high):
    if low < high:
        p = partion(arr, low, high)
        quick_sort(arr, low, p - 1)
        quick_sort(arr, p + 1, high)


def partion(arr, low, high):
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


arr = [38, 27, 43, 3, 9, 82, 10]
quick_sort(arr, 0, len(arr) - 1)
print(arr)
