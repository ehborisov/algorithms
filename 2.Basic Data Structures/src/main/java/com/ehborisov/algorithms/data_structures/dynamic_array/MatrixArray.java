package com.ehborisov.algorithms.data_structures.dynamic_array;

public class MatrixArray<T> implements IArray<T> {

    private int size;
    private int vector;
    private IArray<IArray<T>> array;

    public MatrixArray(int vector) {
        this.vector = vector;
        array = new SingleArray<>();
        size = 0;
    }

    public MatrixArray() {
        this(100);
    }

    @Override
    public int size() {
        return size;
    }

    @Override
    public void add(T item) {
        if (size == array.size() * vector)
            array.add(new VectorArray<T>(vector));
        array.get(size / vector).add(item);
        size ++;
    }

    @Override
    public void add(T item, int index) {
        if(index > size()-1)
            throw new IllegalArgumentException("Index is out of the array bounds");
        int arrayIndex = index / vector;
        int lastRowIndex = array.size() - 1;
        int injectAt = index % vector;
        IArray<IArray<T>> newBaseArray = new SingleArray<>();
        for(int i = 0; i < arrayIndex; i++)
            newBaseArray.add(array.get(i));
        // It's pretty ugly, but I assume we cannot modify given data structures
        // to expose underlying arrays.
        for(int i = arrayIndex; i <= lastRowIndex; i++){
            IArray<T> newRow = new VectorArray<>(vector);
            int endIndex = (i == lastRowIndex) && (size() % vector != 0) ? size() % vector : vector - 1;
            boolean hasOverflow = endIndex == vector - 1;
            for(int j = 0; j < injectAt; j++)
                newRow.add(array.get(i).get(j));
            newRow.add(item);
            for(int j = injectAt; j < (hasOverflow ? endIndex : endIndex + 1); j++)
                newRow.add(array.get(i).get(j));
            item = hasOverflow ? array.get(i).get(endIndex) : null;
            injectAt = 0;
            newBaseArray.add(newRow);
        }
        if (item != null){
            IArray<T> newRow = new VectorArray<>(vector);
            newRow.add(item);
            newBaseArray.add(newRow);
        }
        size++;
        array = newBaseArray;
    }

    @Override
    public T remove(int index) {
        if(index > size()-1)
            throw new IllegalArgumentException("Index is out of the array bounds");
        int arrayIndex = index / vector;
        int lastRowIndex = array.size() - 1;
        int removeIndex = index % vector;
        IArray<IArray<T>> newBaseArray = new SingleArray<>();
        for(int i = 0; i < arrayIndex; i++)
            newBaseArray.add(array.get(i));
        T element = get(index);
        for(int i = arrayIndex; i <= lastRowIndex; i++) {
            if (i == lastRowIndex && size() % vector == 1) {
                break;
            }
            T shiftedItem = i == lastRowIndex ? null : array.get(i+1).get(0);
            IArray<T> newRow = new VectorArray<>(vector);
            int endIndex = i == lastRowIndex && size() % vector != 0 ? (size()-1) % vector : vector - 1;
            for(int j = 0; j <= endIndex; j++)
                if(j != removeIndex)
                    newRow.add(array.get(i).get(j));
            if (shiftedItem != null)
                newRow.add(shiftedItem);
            removeIndex = 0;
            newBaseArray.add(newRow);
        }
        size--;
        array = newBaseArray;
        return element;
    }

    @Override
    public T get(int index) {
        return array.get(index / vector).get(index % vector);
    }
}
