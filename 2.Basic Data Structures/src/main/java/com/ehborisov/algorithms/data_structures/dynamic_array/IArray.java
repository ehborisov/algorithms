package com.ehborisov.algorithms.data_structures.dynamic_array;

public interface IArray<T> {
    int size();
    void add(T item);
    T get(int index);
    void add(T item, int index);
    T remove(int index);
}
