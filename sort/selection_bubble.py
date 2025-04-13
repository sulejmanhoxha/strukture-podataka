def selection_sort(arr: list):
    for i in range(0, len(arr) - 1):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                # temp = arr[j]
                # arr[j] = arr[i]
                # arr[i] = temp
                # njisej si kta ma nelt
                arr[i], arr[j] = arr[j], arr[i]
    return arr


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


print([5, 1, 6, 2, 7, 8, 2])
# print(selection_sort([5, 1, 6, 2, 7, 8, 2]))
print(bubble_sort([5, 1, 6, 2, 7, 8, 2]))
