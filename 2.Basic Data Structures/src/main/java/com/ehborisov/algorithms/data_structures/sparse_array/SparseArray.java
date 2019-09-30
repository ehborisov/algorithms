package com.ehborisov.algorithms.data_structures.sparse_array;

import com.ehborisov.algorithms.data_structures.dynamic_array.FactorArray;

import java.util.Objects;


// based on compressed sparse row matrix specifications, see https://en.wikipedia.org/wiki/Sparse_matrix
public class SparseArray<T> {

    private FactorArray<T> entries;
    private FactorArray<Integer> row_pointers;
    private FactorArray<Integer> column_indices;
    // maintains the shape given by the initial matrix
    private int rows;
    private int columns;
    // pointer to the last known element in the last row, to maintain the append operation.
    private int last_element_pointer;

    public SparseArray(T[][] initialArray) {
        this.entries = new FactorArray<>();
        this.row_pointers = new FactorArray<>();
        this.column_indices = new FactorArray<>();

        // process the initial two-dimensional array
        this.rows = initialArray.length;
        this.columns = initialArray[0].length;
        int row_pointer = 0;
        row_pointers.add(row_pointer);
        for (T[] ts : initialArray) {
            for (int j = 0; j < ts.length; j++) {
                if (ts[j] != null) {
                    entries.add(ts[j]);
                    column_indices.add(j);
                    row_pointer++;
                }
            }
            row_pointers.add(row_pointer);
        }
        last_element_pointer = this.columns-1;
    }

    public int getElementsCount(){
        return entries.size();
    }

    private void checkDimensions(int i, int j){
        if(i > rows - 1 || j > columns - 1 || (i == rows - 1 && j > last_element_pointer) )
            throw new IllegalArgumentException("Given index is out of bounds");
    }

    public T get(int i, int j){
        checkDimensions(i, j);
        int row_start = row_pointers.get(i);
        int next_row = row_pointers.get(i+1);
        for(int k = row_start; k < next_row; k++){
            int col = column_indices.get(k);
            if(col == j){
                return entries.get(k);
            } else if (col > j) {
                return null;
            }
        }
        return null;
    }

    public T delete(int i, int j) {
        /*
         deletion of element does not shift the entire matrix, but just nullifies the cell.
         */
        checkDimensions(i, j);
        int row_start = row_pointers.get(i);
        int next_row = row_pointers.get(i + 1);
        for(int k = row_start; k < next_row; k++){
            int col = column_indices.get(k);
            if(col == j){
                T element = entries.remove(k);
                column_indices.remove(k);
                for(int m = i + 1; m < row_pointers.size(); m++) {
                    // this ugliness is due to the limitations of IArray interface
                    int t = row_pointers.remove(m);
                    row_pointers.add(t - 1, m);
                }
                return element;
            } else if (col > j) {
                return null;
            }
        }
        return null;
    }

    public void set(T value, int i, int j) {
        /*
         Sets the value in a single cell.
         */
        if(Objects.isNull(value)){
            // fall back to delete
            delete(i, j);
            return;
        }
        checkDimensions(i, j);
        int row_start = row_pointers.get(i);
        int next_row = row_pointers.get(i + 1);
        if(row_start == next_row){
            // process the case when we set the element on a previously empty row
            entries.add(value, row_start);
            column_indices.add(j, row_start);
        } else {
            Integer index_to_insert_at = null;
            for(int k = row_start; k < next_row; k++){
                int col = column_indices.get(k);
                if(col >= j) {
                    index_to_insert_at = k;
                    break;
                }
            }
            if(Objects.isNull(index_to_insert_at))
                index_to_insert_at = column_indices.get(next_row);
            entries.add(value, index_to_insert_at);
            if(column_indices.get(index_to_insert_at) == j) {
                entries.remove(index_to_insert_at + 1);
                return;
            } else {
                column_indices.add(j, index_to_insert_at);
            }
        }
        for(int k = i + 1; k < row_pointers.size(); k++){
            int p = row_pointers.remove(k);
            row_pointers.add(p + 1, k);
        }
    }

    public void add(T value) {
        /*
         Appends the value to the last row and expands the matrix if necessary.
         */
        boolean expandRow = last_element_pointer == columns - 1;
        if(expandRow){
            last_element_pointer = 0;
            rows++;
        } else {
            last_element_pointer++;
        }
        if(!Objects.isNull(value)){
            entries.add(value);
            column_indices.add(last_element_pointer);
            int row_pointer = expandRow ? row_pointers.get(row_pointers.size() - 1) :
                    row_pointers.remove(row_pointers.size() - 1);
            row_pointers.add(row_pointer +1);
        }
    }
}
