package com.ehborisov.algorithms.data_structures.dynamic_array;

import com.google.common.base.Stopwatch;

import java.lang.reflect.InvocationTargetException;
import java.util.Arrays;
import java.util.List;
import java.util.Random;

public class ArraysComparison {

    public static void main(String[] args) throws NoSuchMethodException,
            InstantiationException, IllegalAccessException, InvocationTargetException {
        List<Class<? extends IArray>> arrays = Arrays.asList(
                SingleArray.class,
                VectorArray.class,
                FactorArray.class,
                MatrixArray.class,
                ArrayListWrapper.class
        );

        int[] getAndAddData = new int[] {100000, 1000000, 10000000};

        int[] byIndexData = new int[] {1000, 10000, 100000};

        for (int i = 0; i < 5; i++) {
            for(int j = 0; j < 3; j++) {
                    IArray array = arrays.get(i).getConstructor().newInstance();
                    int count = getAndAddData[j];
                    ArraysComparison.addValues(array, count);

                    array = arrays.get(i).getConstructor().newInstance();
                    count = getAndAddData[j];
                    ArraysComparison.getValues(array, count);

                    array = arrays.get(i).getConstructor().newInstance();
                    count = byIndexData[j];
                    ArraysComparison.addValuesIndexed(array, count);

                    array = arrays.get(i).getConstructor().newInstance();
                    count = byIndexData[j];
                    ArraysComparison.removeValuesIndexed(array, count);
                }
        }
    }

    static void addValues(IArray<String> array, int count) {
        Stopwatch timer = new Stopwatch().start();
        for(int j = 0; j < count; j++)
            array.add(j + "");
        System.out.println("Add test: " + array + " " + count + " " + timer.stop());
    }

    static void addValuesIndexed(IArray<String> array, int count) {
        Random random = new Random();
        array.add("");
        Stopwatch timer = new Stopwatch().start();
        for(int j = 0; j < count; j++) {
            timer.stop();
            int index = random.nextInt(array.size() > 1 ? array.size() - 1 : 1);
            timer.start();
            array.add(j + "", index);
        }
        System.out.println("Add indexed test: " + array + " " + count + " " + timer.stop());
    }

    static void removeValuesIndexed(IArray<String> array, int count) {
        Random random = new Random();
        for(int j = 0; j < count; j++)
            array.add(j + "");
        Stopwatch timer = new Stopwatch().start();
        for(int j = 0; j < count; j++){
            timer.stop();
            int index = random.nextInt(array.size() > 1 ? array.size() - 1 : 1);
            timer.start();
            array.remove(index);
        }
        System.out.println("Remove test: " + array + " " + count + " " + timer.stop());
    }

    static void getValues(IArray<String> array, int count) {
        Random random = new Random();
        for(int j = 0; j < count; j++)
            array.add(j + "");
        Stopwatch timer = new Stopwatch().start();
        for(int j = 0; j < count; j++){
            timer.stop();
            int index = random.nextInt(array.size() > 1 ? array.size() - 1 : 1);
            timer.start();
            array.get(index);
        }
        System.out.println("Get test: " + array + " " + count + " " + timer.stop());
    }
}
