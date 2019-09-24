package com.ehborisov.algorithms.data_structures.dynamic_array.test;

import org.junit.Test;
import com.ehborisov.algorithms.data_structures.dynamic_array.MatrixArray;
import static org.junit.Assert.assertEquals;

public class MatrixArrayTest {

    @Test
    public void matrixArrayAddElements(){
        MatrixArray<String> array = new MatrixArray<>(2);
        for(int i = 0; i < 4; i++)
            array.add(i + "");
        assertEquals(4, array.size());
    }

    @Test
    public void matrixArrayAddIndexedElement(){
        MatrixArray<String> array = new MatrixArray<>(2);
        for(int i = 0; i < 4; i++)
            array.add(i + "");
        array.add("4", 2);
        assertEquals(5, array.size());
        assertEquals("4", array.get(2));
    }

    @Test
    public void matrixArrayRemoveElement(){
        MatrixArray<String> array = new MatrixArray<>(2);
        for(int i = 0; i < 8; i++)
            array.add(i + "");
        String e = array.remove(0);
        assertEquals("0", e);
        assertEquals(7, array.size());
        assertEquals("4", array.get(3));
    }
}
