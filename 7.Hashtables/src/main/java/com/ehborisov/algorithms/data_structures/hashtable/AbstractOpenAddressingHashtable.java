/***
 * An abstract hashtable class that is backed by an array. Since array index cannot grow larger than Integer.MAX_VALUE,
 * modifying a bit the original multiplicative hash, that assumes unsigned ints. Table is of a fixed size,
 * no grow/shrink logic is implemented.
 *
 * Follows 11.3.2 of CLRS
 */
package com.ehborisov.algorithms.data_structures.hashtable;

import com.google.common.math.IntMath;
import java.math.RoundingMode;

enum SpecialSymbols {
    DELETED
}

public abstract class AbstractOpenAddressingHashtable {

    private static final int A = (int) ((Math.sqrt(5) - 1)/2 * IntMath.pow(2, 30));

    protected Object[] storage;
    int size;

    int p;
    public AbstractOpenAddressingHashtable(int size) {
        //round it up to the nearest power of 2
        this.p = IntMath.log2(size, RoundingMode.CEILING);
        if(this.p >= 31){
            throw new IllegalArgumentException(
                    String.format("Cannot initialize hashtable, the desired size is too large %d", size));
        }
        this.size = IntMath.pow(2, this.p);
        this.storage = new Object[this.size];
    }

    public void put(Object key) {
        int i = 0;
        do {
            int j = this.hash(key, i);
            if(this.storage[j] == null || this.storage[j] == SpecialSymbols.DELETED){
                storage[j] = key;
                return;
            } else {
                i++;
            }
        } while (i != this.size);
        throw new RuntimeException("Hashtable overflow.");
    }

    public void delete(Object key) {
        int i = 0;
        int j;
        do {
            j = this.hash(key, i);
            if(this.storage[j] == key) {
                storage[j] = SpecialSymbols.DELETED;
                return;
            } else {
                i++;
            }
        } while (i != this.size || storage[j] == null);
    }

    public Object get(Object key) {
        int i = 0;
        int j;
        do {
            j = this.hash(key, i);
            if(this.storage[j] != null && this.storage[j] != SpecialSymbols.DELETED) {
                return storage[j];
            } else {
                i++;
            }
        } while (i != this.size || storage[j] == null || storage[j] == SpecialSymbols.DELETED);
        return null;
    }

    int multiplicative_hash(Object key) {
        // see https://stackoverflow.com/questions/11871245/knuth-multiplicative-hash
        int object_hash = key.hashCode();  // since it's just an example for strings and numerics, that'll suffice.
        return (A * object_hash) >>> (32 - this.p);
    }

    abstract int hash(Object key, int i);
}
