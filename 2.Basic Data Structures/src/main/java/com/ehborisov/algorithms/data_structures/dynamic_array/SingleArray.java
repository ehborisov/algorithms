package com.ehborisov.algorithms.data_structures.dynamic_array;

public class SingleArray<T> implements IArray<T> {

    private Object[] array;

    public SingleArray () {
        array = new Object[0];
    }

    @Override
    public int size() {
        return array.length;
    }

    @Override
    public void add(T item) {
        resize();
        array[size() - 1] = item;
    }

    @Override
    public void add(T item, int index) {
        if(index > array.length -1)
            throw new IllegalArgumentException("Index is out of the array bounds");
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
        Object[] newArray = new Object[size() + 1];
        System.arraycopy(array, 0, newArray, 0, size());
        array = newArray;
    }

    @Override
    public T remove(int index) {
        if(index > array.length - 1)
            throw new IllegalArgumentException("Index is out of the array bounds");
        T value = get(index);
        Object[] newArray = new Object[size() - 1];
        System.arraycopy(array, 0, newArray, 0, index);
        if(index < newArray.length)
            System.arraycopy(array, index+1, newArray, index, array.length - index - 1);
        array = newArray;
        return value;
    }
}
