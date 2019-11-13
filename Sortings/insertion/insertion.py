def insertion_sort(arr, i=None, j=None):
    sort_from = i if i is not None else 0
    sort_to = j + 1 if j is not None else len(arr)
    for i in range(sort_from + 1, sort_to):
        for j in range(i+1):
            if arr[i] < arr[j]:
                swap(j, i, arr)
    return arr


def swap(i, j, arr):
    arr[i] += arr[j]
    arr[j] = arr[i] - arr[j]
    arr[i] -= arr[j]
