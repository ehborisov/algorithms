package com.ehborisov.algorithms.data_structures.hashtable;

public class LinearProbingHashtable extends AbstractOpenAddressingHashtable {

    public LinearProbingHashtable(int size){
        super(size);
    }

    @Override
    int hash(Object key, int i) {
        return (this.multiplicative_hash(key) + i) % this.size;
    }
}
