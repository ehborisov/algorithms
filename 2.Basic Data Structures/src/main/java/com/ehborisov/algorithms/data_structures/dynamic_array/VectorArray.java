package com.ehborisov.algorithms.data_structures.dynamic_array;

public class VectorArray<T> implements IArray<T> {

    private Object[] array;
    private int vector;
    private int size;

    public VectorArray(int vector) {
        this.vector = vector;
        array = new Object[0];
        size = 0;
    }

    public VectorArray() {
        this(100);
    }

    @Override
    public int size() {
        return size;
    }

    @Override
    public void add(T item) {
        if (size() == array.length)
            resize();
        array[size] = item;
        size++;
    }

    @Override
    public void add(T item, int index) {
        if(index > size - 1)
            throw new IllegalArgumentException("Index is out of the array bounds");
        if (size() == array.length)
            resize();
        System.arraycopy(array, index, array, index + 1, array.length - 1 - index);
        array[index] = item;
    }

    @Override
    @SuppressWarnings("unchecked")
    public T get(int index) {
        return (T)array[index];
    }

    private void resize() {
        Object[] newArray = new Object[array.length + vector];
        System.arraycopy(array, 0, newArray, 0, array.length);
        array = newArray;
    }

    @Override
    public T remove(int index) {
        if(index > size - 1)
            throw new IllegalArgumentException("Index is out of the array bounds");
        T value = get(index);
        Object[] newArray = new Object[array.length - size + 1 == vector ? array.length - vector : array.length];
        System.arraycopy(array, 0, newArray, 0, index);
        if(index < newArray.length)
            System.arraycopy(array, index+1, newArray, index, size() - index - 1);
        size--;
        array = newArray;
        return value;
    }
}
