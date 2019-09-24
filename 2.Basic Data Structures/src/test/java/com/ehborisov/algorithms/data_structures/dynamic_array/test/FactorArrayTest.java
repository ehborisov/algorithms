package com.ehborisov.algorithms.data_structures.dynamic_array.test;

import com.ehborisov.algorithms.data_structures.dynamic_array.FactorArray;
import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class FactorArrayTest {

    @Test
    public void factorArrayAddElements(){
        FactorArray<String> array = new FactorArray<>(50, 2);
        for(int i = 0; i<12; i++)
            array.add(i + "");
        assertEquals(12, array.size());
        assertEquals("11", array.get(11));
    }

    @Test
    public void factorArrayAddIndexedElement(){
        FactorArray<String> array = new FactorArray<>(50, 2);
        for(int i = 0; i<4; i++)
            array.add(i + "");
        array.add("4", 2);
        assertEquals(5, array.size());
        assertEquals("4", array.get(2));
    }

    @Test
    public void factorArrayRemoveElement(){
        FactorArray<String> array = new FactorArray<>();
        for(int i = 0; i<8; i++)
            array.add(i + "");
        String e0 = array.remove(0);
        String e2 = array.remove(1);
        String e4 = array.remove(2);
        String e7 = array.remove(4);
        assertEquals("0", e0);
        assertEquals("2", e2);
        assertEquals("4", e4);
        assertEquals("7", e7);
        assertEquals(4, array.size());
        assertEquals("1", array.get(0));
    }
}