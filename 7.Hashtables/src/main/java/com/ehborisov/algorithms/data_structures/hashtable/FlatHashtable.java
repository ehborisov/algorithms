/**
 Based on Robin Hood hashing original paper https://cs.uwaterloo.ca/research/tr/1986/CS-86-14.pdf
 this table does not implement augmenting values storage and behaves effectively like a set for the sake of
 simplicity.
 */
package com.ehborisov.algorithms.data_structures.hashtable;

import com.sun.istack.internal.NotNull;
import java.util.Optional;

public class FlatHashtable extends LinearProbingHashtable {

    private int[] counters;
    private int countersSize;
    private int shortestProbe = 0;
    private int longestProbe = 0;
    private int totalcost = 0;
    private int m = 0;

    public FlatHashtable(int size) {
        super(size);
        this.countersSize = (int) (1.15 * Math.log((double) this.size) + 2.5); // ~ 1.15 ln(n) + 2.5 (see page 56)
        this.counters = new int[this.countersSize];
        this.counters[0] = this.size;

    }

    public void put(@NotNull Object key) {
        if(this.m == this.size) throw new RuntimeException("Hashtable overflow");
        int probePosition = this.shortestProbe;
        int location;
        int recordPosition;
        Object k = key;
        while (k != null && k != SpecialSymbols.DELETED) {
            probePosition++;
            location = this.hash(k, probePosition);
            this.totalcost++;
            recordPosition = Optional.ofNullable(this.findPosition(location)).orElse(0);
            if (probePosition > recordPosition) {
                Object tmp = this.storage[location];
                this.storage[location] = k;
                k = tmp;
                this.counters[probePosition % this.countersSize]++;
                if(this.counters[recordPosition % this.countersSize] > 0){
                    this.counters[recordPosition % this.countersSize]--;
                }
                this.longestProbe = longestProbe > probePosition ? longestProbe : probePosition;
                probePosition = (k == null) ? recordPosition : probePosition;
            }
        }
        while (this.counters[this.shortestProbe % this.countersSize] == 0) this.shortestProbe++;
        this.m++;
    }

    public Object get(Object key) {
        Integer probePosition = this.findPosition(key);
        return (probePosition != null) ? this.storage[this.hash(key, probePosition)] : null;
    }

    private Integer findPosition(Object key){
        int downPosition = (this.m != 0) ? this.totalcost / this.m : 0; // mean position
        int upPosition = downPosition + 1;
        int downLocation;
        int upLocation;
        while (downPosition >= shortestProbe && upPosition <= longestProbe) {
            downLocation = this.hash(key, downPosition);
            if(this.storage[downLocation] == key) return downPosition;
            upLocation = this.hash(key, upPosition);
            if(this.storage[upLocation] == key) return upLocation;
            downPosition--;
            upPosition++;
        }
        while (downPosition >= shortestProbe){
            downLocation = this.hash(key, downPosition);
            if(this.storage[downLocation] == key) return downPosition;
            downPosition--;
        }
        while (upPosition <= longestProbe) {
            upLocation = this.hash(key, upPosition);
            if(this.storage[upLocation] == key) return upPosition;
            upPosition++;
        }
        return null;
    }
}
