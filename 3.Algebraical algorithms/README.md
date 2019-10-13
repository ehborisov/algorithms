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


### 2. Exponentiation

Package `exponentiation` contains implementations of exponentiaton algorithms for two integer numbers.

File `exponentiation_algorithms_comparison.py` contains a benchmark of various implementations.
(1000000 invocations on random integers from [1, 1e6] in [1, 1e2]-th power)

|Naive|Power of 2 with multiplication|Squaring|Built-in
|:-----:|:-----:|:-----:|:-----:|
|7.098 s|5.212 s|5.043 s|3.499 s|


### 3. Primes search

Package `primes_search` contains implementations of number of primes calculation for up to a given number.

File `primes_comparison.py` contains a benchmark of various implementations.
(time of work on n=100000 in one invocation)

|Naive|Naive with caching|Eratosthenes sieve|
|:-----:|:-----:|:-----:|
|30.711 s|0.06 s|0.017 s|


### 4. Fibonacci

Package `fibonacci` contains implementations of Fibonacci numbers calculation.

File `fibonacci_comparison.py` contains a benchmark of various implementations.
(time of work on n=100000 invocation to compute 1000-th Fibonacci number)

|Recursive|Iterative|Binet|Matrix|
|:-----:|:-----:|:-----:|:-----:|
|\>5m|73.004 s|12.283 s|40.517 s|


to run tests invoke `tox`