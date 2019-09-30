package com.ehborisov.algorithms.data_structures.sparse_array.test;

import org.junit.Test;
import com.ehborisov.algorithms.data_structures.sparse_array.SparseArray;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNull;

public class SparseArrayTest {
    @Test
    public void sparseArrayInitialize(){
        SparseArray<String> array = new SparseArray<>(new String[][] {
                {"1", null},
                {null, null},
                {null, "2"}
        });
        assertEquals(2, array.getElementsCount());
        assertEquals("1", array.get(0,0));
        assertEquals("2", array.get(2,1));
    }

    @Test
    public void sparseArraySetIndexed(){
        SparseArray<String> array = new SparseArray<>(new String[][] {
                {"1", null, null},
                {null, null, "2"},
                {null, "3", null}
        });
        assertEquals(3, array.getElementsCount());
        array.set("4", 1, 1);
        assertEquals(4, array.getElementsCount());
        assertEquals("4", array.get(1,1));
    }

    @Test
    public void sparseArraySetExisting(){
        SparseArray<String> array = new SparseArray<>(new String[][] {
                {"1", null, null},
                {null, null, "2"},
                {null, "3", null}
        });
        assertEquals(3, array.getElementsCount());
        array.set("4", 1, 2);
        assertEquals(3, array.getElementsCount());
        assertEquals("4", array.get(1,2));
    }

    @Test
    public void sparseArrayAddNewRow(){
        SparseArray<String> array = new SparseArray<>(new String[][] {
                {"1", null, null},
                {null, null, "2"},
                {null, "3", null}
        });
        assertEquals(3, array.getElementsCount());
        array.add("4");
        assertEquals(4, array.getElementsCount());
        assertEquals("4", array.get(3,0));
    }

    @Test
    public void sparseArrayAddSameRow(){
        SparseArray<String> array = new SparseArray<>(new String[][] {
                {"1", null, null},
                {null, null, "2"},
                {null, "3", null}
        });
        assertEquals(3, array.getElementsCount());
        array.add("4");
        array.add(null);
        assertEquals(4, array.getElementsCount());
        assertNull(array.get(3, 1));
    }

    @Test
    public void sparseArrayDelete(){
        SparseArray<String> array = new SparseArray<>(new String[][] {
                {"1", null, null},
                {null, null, "2"},
                {null, "3", null}
        });
        array.delete(0, 0);
        assertEquals(2, array.getElementsCount());
        assertNull(array.get(0, 0));
        array.delete(2, 1);
        assertEquals(1, array.getElementsCount());
        assertNull(array.get(2, 1));
    }
}
