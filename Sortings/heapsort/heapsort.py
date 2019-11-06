from heapsort.heap import MaxHeap, C, swap
from typing import List


def heapsort(arr: List[C]) -> List[C]:
    heap = MaxHeap.build_max_heap(arr)
    for i in reversed(range(1, heap.size)):
        swap(heap.storage, 0, i)
        heap.size -= 1
        heap.sift_down()
    return heap.storage
