from __future__ import annotations
from typing import List, Optional
from sort_commons import C, swap


class MinHeap(object):

    def __init__(self):
        self.storage = []
        self.size = 0

    @classmethod
    def build_min_heap(cls, arr: List[C]) -> MinHeap:
        a = cls()
        a.storage = arr
        a.size = len(arr)
        for i in reversed(range(0, len(arr)//2)):
            a.sift_down(i)
        return a

    def add(self, val: C) -> None:
        self.storage.append(val)
        self.size += 1
        self._percolate_up()

    def get_min(self) -> Optional[C]:
        if not self.storage:
            return None
        if len(self.storage) == 1:
            return self.storage.pop()
        m = self.storage[0]
        self.storage[0] = self.storage.pop()
        self.size -= 1
        self.sift_down()
        return m

    def _percolate_up(self) -> None:
        if self.size == 0:
            return
        i = self.size - 1
        while i != 0:
            parent = i // 2
            if self.storage[parent] > self.storage[i]:
                swap(self.storage, parent, i)
            else:
                break
            i = parent

    def sift_down(self, i=0) -> None:
        # Cormen 6.2-2
        last_index = self.size - 1
        while True:
            left_child = 2 * i + 1
            right_child = 2 * i + 2
            if left_child > last_index:
                return
            smallest = (left_child if right_child > last_index or
                        self.storage[left_child] < self.storage[right_child] else right_child)
            if self.storage[i] > self.storage[smallest]:
                swap(self.storage, i, smallest)
            i = smallest


class MaxHeap(object):

    def __init__(self):
        self.storage = []
        self.size = 0

    @classmethod
    def build_max_heap(cls, arr: List[C]) -> MaxHeap:
        a = cls()
        a.storage = arr
        a.size = len(arr)
        for i in reversed(range(0, len(arr)//2)):
            a.sift_down(i)
        return a

    def add(self, val: C) -> None:
        self.storage.append(val)
        self.size += 1
        self._percolate_up()

    def get_max(self) -> Optional[C]:
        if not self.storage:
            return None
        if len(self.storage) == 1:
            self.size -= 1
            return self.storage.pop()
        m = self.storage[0]
        self.storage[0] = self.storage.pop()
        self.size -= 1
        self.sift_down()
        return m

    def _percolate_up(self) -> None:
        if not self.storage:
            return
        i = self.size - 1
        while i > 0:
            parent = i // 2
            if self.storage[parent] < self.storage[i]:
                swap(self.storage, parent, i)
            else:
                break
            i = parent

    def sift_down(self, i=0) -> None:
        # Cormen 6.2-5
        last_index = self.size - 1
        while True:
            left_child = 2 * i + 1
            right_child = 2 * i + 2
            if left_child > last_index:
                return
            largest = (left_child if right_child > last_index or
                       self.storage[left_child] > self.storage[right_child] else right_child)
            if self.storage[i] < self.storage[largest]:
                swap(self.storage, i, largest)
            i = largest
