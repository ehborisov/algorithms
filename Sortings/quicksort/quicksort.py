from sort_commons import C, swap
from typing import List, Callable
from random import randint
from insertion import insertion


def default_partition(arr: List[C], begin: int, end: int) -> int:
    pivot = arr[end]
    i = begin
    for j in range(begin, end):
        if arr[j] <= pivot:
            swap(arr, i, j)
            i += 1
    swap(arr, i, end)
    return i


def random_partition(arr: List[C], begin: int, end: int) -> int:
    pivot = randint(begin, end)
    swap(arr, pivot, end)
    return default_partition(arr, begin, end)


def _quicksort(arr: List[C], begin: int, end: int, partition_strategy: Callable):
    if begin < end:
        pivot = partition_strategy(arr, begin, end)
        _quicksort(arr, begin, pivot-1, partition_strategy)
        _quicksort(arr, pivot + 1, end, partition_strategy)


def _quicksort_with_insertion(arr: List[C], begin: int, end: int, partition_strategy: Callable,
                              insertion_threshold: int=None):
    if insertion_threshold is not None and end - begin <= insertion_threshold:
        insertion.insertion_sort(arr, begin, end)
    elif begin < end:
        pivot = partition_strategy(arr, begin, end)
        _quicksort(arr, begin, pivot-1, partition_strategy)
        _quicksort(arr, pivot + 1, end, partition_strategy)


def quicksort(arr: List[C], partition_strategy: Callable = default_partition) -> List[C]:
    _quicksort(arr, 0, len(arr) - 1, partition_strategy)
    return arr


def quicksort_with_insertion(arr: List[C], partition_strategy: Callable = default_partition) -> List[C]:
    _quicksort_with_insertion(arr, 0, len(arr) - 1, partition_strategy)
    return arr
