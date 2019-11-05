import timeit
import csv
from shell.shell import shell_sort
from insertion.insertion import insertion_sort
import random
from multiprocessing import Pool

SHUFFLE_SETUP = '''
import random
import copy
from math import floor

random.seed('some')

def swap(i, j, arr):
    arr[i] += arr[j]
    arr[j] = arr[i] - arr[j]
    arr[i] -= arr[j]

def shuffle_in_place(arr, num_shuffles):
    for i in range(num_shuffles):
        p = q = 0
        while p == q:
            # initialize p and q to be not equal
            p = random.randint(0, len(arr) - 1)
            q = random.randint(0, len(arr) - 1)
        swap(p, q, arr)

'''

SHUFFLED_SETUP = '''
n = %d
shuffled = list(range(n))
random.shuffle(shuffled)

'''

SHUFFLED_10_PERCENT = '''
n = %d
shuffled = list(range(n))
n_10 = n // 10
shuffle_in_place(shuffled, n_10)

'''

SHUFFLED_5_SETUP = '''
n = %d
shuffled = list(range(n))
shuffle_in_place(shuffled, 5)

'''

SHELL_SEQUENCE_SETUP = '''
seq = [1]
i = n // 2
k = 1
while i >= 1:
    seq.append(floor(i))
    k += 1
    i = i // 2

'''

A168604_SEQ_SETUP = '''
seq = [1]
i = (2 ** 1) - 1
k = 1
while i <= n:
    seq.append(floor(i))
    k += 1
    i = (2 ** k) - 1
seq.reverse()

'''

A003642_SEQ_SETUP = '''
seq = [1]
i = (3 ** 1 - 1)/2
k = 1
while i <= n:
    seq.append(floor(i))
    k += 1
    i = (3 ** k - 1)/2
seq.reverse()

'''

A033622_SEQ_SETUP = '''
seq = [1]
i = 8 * (2 ** 1) - 6 * (2 ** 1) + 1
k = 1
while i <= n:
    seq.append(floor(i))
    k += 1
    if k % 2 == 0:
        i = 9 * ((2 ** k) - (2 ** (k//2))) + 1
    else:
        i = 8 * (2 ** k) - 6 * (2 ** ((k+1)//2)) + 1
seq.reverse()
'''


def compare_performance(n):
    shuffled_all_setup = SHUFFLE_SETUP + SHUFFLED_SETUP % (n,)

    shuffled_10_percent_setup = SHUFFLE_SETUP + SHUFFLED_10_PERCENT % (n,)

    shuffled_5_setup = SHUFFLE_SETUP + SHUFFLED_5_SETUP % (n,)

    setups = {'_shuffled': shuffled_all_setup, '_10%': shuffled_10_percent_setup, '_5': shuffled_5_setup}

    results = {'N': n}
    # test Insertion
    results.update({'Insertion' + suffix: min(timeit.Timer("import insertion; a = shuffled[:]; insertion_sort(a)",
                                                           globals=globals(), setup=setup).repeat(4, 10))
                    for suffix, setup in setups.items()}),
    # test Shell original sequence
    results.update({'Shell' + suffix: min(timeit.Timer("import shell; a = shuffled[:]; shell_sort(a, seq)",
                                                       globals=globals(), setup=setup + SHELL_SEQUENCE_SETUP).repeat(4,
                                                                                                                     10))
                    for suffix, setup in setups.items()}),
    # test A168604 sequence (2^k -1)
    results.update({'ShellA168604' + suffix: min(timeit.Timer("import shell; a = shuffled[:]; shell_sort(a, seq)",
                                                              globals=globals(),
                                                              setup=setup + A168604_SEQ_SETUP).repeat(4, 10))
                    for suffix, setup in setups.items()}),
    # test A003462 sequence (3^k - 1)/2
    results.update({'ShellA003462' + suffix: min(timeit.Timer("import shell; a = shuffled[:]; shell_sort(a, seq)",
                                                              globals=globals(),
                                                              setup=setup + A003642_SEQ_SETUP).repeat(4, 10))
                    for suffix, setup in setups.items()}),
    # test A033622 sequence (Sedgewick)
    results.update({'ShellA033622' + suffix: min(timeit.Timer("import shell; a = shuffled[:]; shell_sort(a, seq)",
                                                              globals=globals(),
                                                              setup=setup + A033622_SEQ_SETUP).repeat(4, 10))
                    for suffix, setup in setups.items()})
    return results


if __name__ == '__main__':
    n = [20 * (2**k) for k in range(10)]
    pool = Pool(4)
    output = pool.map(compare_performance, n)
    with open('sort_comparison.csv', 'w', newline='') as csvfile:
        fieldnames = ['N',
                      'Insertion_shuffled', 'Insertion_10%', 'Insertion_5',
                      'Shell_shuffled', 'Shell_10%', 'Shell_5',
                      'ShellA168604_shuffled', 'ShellA168604_10%', 'ShellA168604_5',
                      'ShellA003462_shuffled', 'ShellA003462_10%', 'ShellA003462_5',
                      'ShellA033622_shuffled', 'ShellA033622_10%', 'ShellA033622_5']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for res_for_n in output:
            writer.writerow(res_for_n)
