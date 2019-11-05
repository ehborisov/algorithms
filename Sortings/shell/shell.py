def shell_sort(arr, gap_sequence):
    for gap in gap_sequence:
        for i in range(gap, len(arr)):
            tmp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > tmp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = tmp
    return arr
