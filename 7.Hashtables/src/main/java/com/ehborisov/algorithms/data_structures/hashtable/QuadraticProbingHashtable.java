package com.ehborisov.algorithms.data_structures.hashtable;

import com.google.common.math.IntMath;

public class QuadraticProbingHashtable extends AbstractOpenAddressingHashtable {

    private int c1;
    private int c2;

    public QuadraticProbingHashtable(int size, int c1, int c2){
        super(size);
        this.c1 = c1;
        this.c2 = c2;
    }

    @Override
    int hash(Object key, int i) {
        return Math.abs(this.multiplicative_hash(key) + this.c1 * i + this.c2 * IntMath.pow(i, 2)) % this.size;
    }
}
