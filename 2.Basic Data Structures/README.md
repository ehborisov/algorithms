Basic Data Structures
===========================

###1. Dynamic Array

Package `com.ehborisov.algorithms.data_structures.dynamic_array` contains various
implementations of the dynamic array data structure.

To execute tests run ` ./gradlew build test`

Comparison tables of the benchmarking results (run `ArraysComparison.java` to replicate).

`N/A` means this test has been skipped due to the input data generation
took too long.

####Add operation

|Elements|SingleArray|VectorArray|FactorArray|MatrixArray|java.util.ArrayList|
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|100000|2.278 s|30.49 ms|7.397 ms|45.52 ms|10.92 ms|
|1000000|6m 31s|3.099 s|33.64 ms|181.1 ms|24.58 ms|
|10000000|\> 5m|\> 5m|248.8 ms|6.415 s|288.0 ms|

####Get operation

|Elements|SingleArray|VectorArray|FactorArray|MatrixArray|java.util.ArrayList|
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|10000|2.703 ms|1.011 ms|2.538 ms|1.370 ms|1.888 ms|
|100000|5.419 ms|6.434 ms|5.876 ms|12.18 ms|8.117 ms|
|1000000|49.15 ms|41.94 ms|43.09 ms|126.6 ms|36.48 ms|
|10000000|N/A|N/A|364.4 ms|2.041 s|363.1 ms|

####Add by index operation

|Elements|SingleArray|VectorArray|FactorArray|MatrixArray|java.util.ArrayList|
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|1000|1.280 ms|396.6 μs|412.0 μs|11.75 ms|651.5 μs|
|10000|25.12 ms|1.623 ms|6.443 ms|183.0 ms|2.910 ms|
|100000|2.455 s|9.173 ms|338.5 ms|18.70 s|221.5 ms|

####Remove by index operation

|Elements|SingleArray|VectorArray|FactorArray|MatrixArray|ArrayList|
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|1000|1.534 ms|816.4 μs|1.182 s|15.07 ms|526.7 μs|
|10000|28.33 ms|21.47 ms|140.9 s|182.5 ms|3.210 ms|
|100000|1.655 s|1.667 s|>5m|22.02 s|224.7 ms|

1. Factor array has a comparable performance with `java.util.ArrayList` in all operations
except for element removal, because java implementation does not shrink the array.
2. Factor array is the most efficient implementation for add, get (constant) add by index operations
(linear) complexity.
3. Matrix array comes second in terms of efficiency, however with the order of growth greater than linear 
for add by index operation.

###2. Sparse Array
