"""
Quick Sort Algorithm.

It works by choosing a value called pivot value.
using which we split the list to be sorted in 2 parts.
First part values are smaller than pivot element.
Second part values are greater than pivot element.
The two parts are further sorted using quick sort in similar manner.
Until the partitions of length 1 or 0 are left.

"""


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


# Example usage:
ary = [10, 7, 8, 2, 1, 5]
n = len(ary)
quick_sort(ary, 0, n - 1)
print("Sorted array:", ary)
