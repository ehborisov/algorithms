import timeit
import csv
import sys
from shell_and_insertion_comparison import SHUFFLE_SETUP, SHUFFLED_SETUP, SHUFFLED_5_SETUP, SHUFFLED_10_PERCENT
from quicksort.quicksort import quicksort
from quicksort.quicksort import quicksort_with_insertion
from quicksort.quicksort import random_partition
from multiprocessing import Pool


def compare_performance(n):
    shuffled_all_setup = SHUFFLE_SETUP + SHUFFLED_SETUP % (n,)

    shuffled_10_percent_setup = SHUFFLE_SETUP + SHUFFLED_10_PERCENT % (n,)

    shuffled_5_setup = SHUFFLE_SETUP + SHUFFLED_5_SETUP % (n,)

    setups = {'_shuffled': shuffled_all_setup, '_10%': shuffled_10_percent_setup, '_5': shuffled_5_setup}

    results = {'N': n}

    # Quicksort with rightmost pivot element
    results.update({'Quicksort' + suffix: min(timeit.Timer(
        "a = shuffled[:]; quicksort(a)", globals=globals(), setup=setup).repeat(4, 10))
                    for suffix, setup in setups.items()})
    # Quicksort with random pivot
    results.update({'Quicksort_random' + suffix: min(timeit.Timer(
        "a = shuffled[:]; quicksort(a, partition_strategy=random_partition)",
        globals=globals(), setup=setup).repeat(4, 10)) for suffix, setup in setups.items()})
    # Quicksort with random pivot and insertion sort fallback
    results.update({'Quicksort_with_insertion' + suffix: min(timeit.Timer(
        "a = shuffled[:]; quicksort(a, partition_strategy=random_partition)",
        globals=globals(), setup=setup).repeat(4, 10)) for suffix, setup in setups.items()})
    return results


if __name__ == '__main__':
    sys.setrecursionlimit(10**6)
    n = [20 * (2**k) for k in range(10)]
    pool = Pool(4)
    output = pool.map(compare_performance, n)
    with open('quicksort_comparison.csv', 'w', newline='') as csvfile:
        fieldnames = ['N',
                      'Quicksort_shuffled', 'Quicksort_10%', 'Quicksort_5',
                      'Quicksort_random_shuffled', 'Quicksort_random_10%', 'Quicksort_random_5',
                      'Quicksort_with_insertion_shuffled', 'Quicksort_with_insertion_10%', 'Quicksort_with_insertion_5']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for res_for_n in output:
            writer.writerow(res_for_n)