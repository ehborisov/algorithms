Sortings
===========================

### 1. Insertion sort and Shell sort

Package `insertion` contains a simple implementation of the Insertion sort

Package `shell` contains an implementation of the Shell sort

File `shell_and_insertion_comparison.py` contains various benchmarks of
Shell and Insertion sort of arrays of different lengths, various degrees
of pre-ordering and different gap-sequences for Shell sort.
(see [Gap sequences](https://en.wikipedia.org/wiki/Shellsort))

For the results see `sort_comparison.csv`

TODO: create visualization.

### 2. Heapsort

Module `heapsort/heap.py` contains min and max heap implementations backed by an array. 
Module `heapsort/heapsort.py` contains heapsort implementation based on the max heap.

to run tests execute `python -m unittest discover -v`

TODO: priority queue, heap element deletion