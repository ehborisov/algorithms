package com.ehborisov.algorithms.data_structures.hashtable;

import org.apache.commons.math3.primes.Primes;


public class DoubleHashingHashtable extends AbstractOpenAddressingHashtable {

    private Object[] storage;

    public DoubleHashingHashtable(int size){
        super(size);
        this.size = Primes.nextPrime(size); // can't be more than 2^31-1 in any case
        this.storage = new Object[this.size];
    }

    private int second_hash(Object key) {
        return 1 + Math.abs(key.hashCode()) % (this.size - 1);
    }

    @Override
    int hash(Object key, int i) {
        return Math.abs(key.hashCode() % this.size + i * second_hash(key)) % this.size;
    }
}
