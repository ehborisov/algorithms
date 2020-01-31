Hashtable Data Structures
===========================

### 1. Open addressing hashtable

Package `com.ehborisov.algorithms.data_structures.hastable` contains several
implementations of the hashtable data structure.

Comparison tables of the benchmarking results (run `HashtableComparison.java` to replicate).

#### Put operation

|Elements|DoubleHashingHashtable|QuadraticProbingHashtable|SimpleMultiplicativeHashHashtable
|:-----:|:-----:|:-----:|:-----:|
|1000|2.563 ms|1.083 ms|1.697 ms
|10000|8.027 ms|6.216 ms|3.316 ms
|100000|26.58 ms|18.96 ms|18.05 ms
|1000000|358.0 ms|262.7 ms|284.7 ms

#### Delete operation

|Elements|DoubleHashingHashtable|QuadraticProbingHashtable|SimpleMultiplicativeHashHashtable
|:-----:|:-----:|:-----:|:-----:|
|1000|557.0 μs|279.5 μs|427.1 μs
|10000|4.039 ms|3.904 ms|2.665 ms
|100000|26.69 ms|50.45 ms|26.09 ms
|1000000|488.3 ms|313.0 ms|586.3 ms

#### Get operation

|Elements|DoubleHashingHashtable|QuadraticProbingHashtable|SimpleMultiplicativeHashHashtable
|:-----:|:-----:|:-----:|:-----:|
|1000|356.4 μs|189.6 μs|107.7 μs
|10000|2.350 ms|3.125 ms|1.520 ms
|100000|16.03 ms|32.80 ms|9.633 ms
|1000000|307.5 ms|251.9 ms|159.7 ms

