package com.ehborisov.algorithms.data_structures.hashtable;

import org.apache.commons.math3.primes.Primes;


public class DoubleHashingHashtable extends AbstractOpenAddressingHashtable {

    private int prime;
    private Object[] storage;

    public DoubleHashingHashtable(int size){
        super(size);
        this.prime = Primes.nextPrime(size);
        if(this.prime >= Integer.MAX_VALUE){
            throw new IllegalArgumentException(
                    String.format("Cannot initialize hashtable, the desired size is too large %d", size));
        }
        this.size = this.prime;
        this.storage = new Object[this.size];
    }

    private int second_hash(Object key) {
        return 1 + Math.abs(key.hashCode()) % (this.prime - 1);
    }

    @Override
    int hash(Object key, int i) {
        return Math.abs(key.hashCode() % this.prime + i * second_hash(key)) % this.prime;
    }
}
