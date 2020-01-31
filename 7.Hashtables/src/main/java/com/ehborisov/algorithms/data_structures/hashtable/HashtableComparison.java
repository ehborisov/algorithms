package com.ehborisov.algorithms.data_structures.hashtable;

import com.google.common.base.Stopwatch;
import org.apache.commons.lang3.RandomStringUtils;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Random;

public class HashtableComparison {
    public static void main(String[] args) {

        int[] size_data = new int[] {1000, 10000, 100000, 1000000};
        Random random = new Random();
        int c1 = random.nextInt(1024);
        int c2 = random.nextInt(1024);

        for(int j = 0; j < 1; j++) {
            int size = size_data[j];
            System.out.println(String.format("Add test for DoubleHashingHashtable of size %d", size));
            DoubleHashingHashtable table = new DoubleHashingHashtable(size);
            HashtableComparison.addKeys(table, size, random);

            System.out.println(String.format("Delete test for DoubleHashingHashtable of size %d", size));
            table = new DoubleHashingHashtable(size);
            HashtableComparison.deleteKeys(table, size, random);

            System.out.println(String.format("Get test for DoubleHashingHashtable of size %d", size));
            table = new DoubleHashingHashtable(size);
            HashtableComparison.getKeys(table, size, random);

            System.out.println(String.format("Add test for QuadraticProbingHashtable of size %d", size));
            QuadraticProbingHashtable table2 = new QuadraticProbingHashtable(size, c1, c2);
            HashtableComparison.addKeys(table2, size, random);

            System.out.println(String.format("Delete test for QuadraticProbingHashtable of size %d", size));
            table2 = new QuadraticProbingHashtable(size, c1, c2);
            HashtableComparison.deleteKeys(table2, size, random);

            System.out.println(String.format("Get test for QuadraticProbingHashtable of size %d", size));
            table2 = new QuadraticProbingHashtable(size, c1, c2);
            HashtableComparison.getKeys(table2, size, random);

            System.out.println(String.format("Add test for LinearProbingHashtable of size %d", size));
            LinearProbingHashtable table3 = new LinearProbingHashtable(size);
            HashtableComparison.addKeys(table3, size, random);

            System.out.println(String.format("Delete test for LinearProbingHashtable of size %d", size));
            table3 = new LinearProbingHashtable(size);
            HashtableComparison.deleteKeys(table3, size, random);

            System.out.println(String.format("Get test for LinearProbingHashtable of size %d", size));
            table3 = new LinearProbingHashtable(size);
            HashtableComparison.getKeys(table3, size, random);
        }
    }

    static void addKeys(AbstractOpenAddressingHashtable table, int count, Random random) {
        HashSet<String> data = new HashSet<>();
        for(int i = 0; i < count; i++){
            data.add(RandomStringUtils.randomAlphanumeric(random.nextInt(1024)));
        }
        Stopwatch timer = new Stopwatch().start();
        for(String key : data){
            table.put(key);
        }
        System.out.println("Put key test: " + table + " " + count + " " + timer.stop());
    }

    static void deleteKeys(AbstractOpenAddressingHashtable table, int count, Random random) {
        HashSet<String> data = new HashSet<>();
        for(int i = 0; i < count; i++){
            String key = RandomStringUtils.randomAlphanumeric(random.nextInt(1024));
            data.add(key);
            table.put(key);
        }
        Stopwatch timer = new Stopwatch().start();
        for(String key: data)
            table.delete(key);
        System.out.println("Delete key test: " + table + " " + count + " " + timer.stop());
    }

    static void getKeys(AbstractOpenAddressingHashtable table, int count, Random random) {
        HashSet<String> data = new HashSet<>();
        for(int i = 0; i < count; i++){
            String key = RandomStringUtils.randomAlphanumeric(random.nextInt(1024));
            data.add(key);
            table.put(key);
        }
        List<String> data_as_list = new ArrayList<String>(data);
        Stopwatch timer = new Stopwatch().start();
        for(int j = 0; j < count; j++) {
            int index = random.nextInt(data_as_list.size());
            String key = data_as_list.get(index);
            table.get(key);
        }
        System.out.println("Get test: " + table + " " + count + " " + timer.stop());
    }
}
