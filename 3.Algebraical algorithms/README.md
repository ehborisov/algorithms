Algebraical Algorithms
===========================

### 1. Greatest Common Divisor

Package `euclid` contains implementations of [Euclidean Algorithm](https://en.wikipedia.org/wiki/Euclidean_algorithm)
for greatest common divisor.

File `euclid_algorithm_comparison.py` contains a benchmark of various implementations.
(1000000 invocations on random integers from [1, 1e10])

|Subtraction-based|Division-based|Binary-recursive|
|:-----:|:-----:|:-----:|
|34.138 s|4.315 s|22.550 s|


to run tests use `tox`