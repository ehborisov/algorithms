package com.ehborisov.algorithms.data_structures.dynamic_array;

public class FactorArray<T> implements IArray<T> {

    private Object[] array;
    private int factor;
    private int size;

    public FactorArray(int factor, int initLength) {
        this.factor = factor;
        array = new Object[initLength];
        size = 0;
    }

    public FactorArray() {
        this(50, 10);
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
        if(index > array.length -1)
            throw new IllegalArgumentException("Index is out of the array bounds");
        if (size() == array.length)
            resize();
        System.arraycopy(array, index, array, index + 1, array.length - 1 - index);
        array[index] = item;
        size++;
    }

    @Override
    @SuppressWarnings("unchecked")
    public T get(int index) {
        if(index > size -1)
            throw new IllegalArgumentException("Index is out of the array bounds");
        return (T) array[index];
    }

    private void resize() {
        Object[] newArray = new Object[array.length + array.length * factor / 100];
        System.arraycopy(array, 0, newArray, 0, array.length);
        array = newArray;
    }

    @Override
    public T remove(int index) {
        if(index > size - 1)
            throw new IllegalArgumentException("Index is out of the array bounds");
        T value = get(index);
        Object[] newArray;
        if(size > 1 && ((array.length - size + 1) * 100/(size - 1) == factor)) {
            newArray = new Object[array.length * (2*factor/3*factor)];
        } else {
            newArray = new Object[array.length];
        }
        System.arraycopy(array, 0, newArray, 0, index);
        if(index < newArray.length)
            System.arraycopy(array, index+1, newArray, index, size() - index - 1);
        size--;
        array = newArray;
        return value;
    }
}
