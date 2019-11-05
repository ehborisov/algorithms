def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i+1):
            if arr[i] < arr[j]:
                swap(j, i, arr)
    return arr


def swap(i, j, arr):
    arr[i] += arr[j]
    arr[j] = arr[i] - arr[j]
    arr[i] -= arr[j]
