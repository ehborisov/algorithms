import timeit
import csv
import sys
from binary_tree import BST
from avl_tree import AvlTree
from multiprocessing import Pool

SETUP = '''
import random
import copy

n = %d
data = list(range(n))
'''

SHUFFLED_SETUP = SETUP + '''
random.shuffle(data)
'''


def compare_performance(n):
    shuffled_setup = SHUFFLED_SETUP % (n,)
    ordered_setup = SETUP % (n,)

    setups = {'_ordered': ordered_setup, '_shuffled': shuffled_setup}

    results = {'N': n}

    # Simple Binary search tree built from ordered and randomized data
    results.update({'BST_search' + suffix: min(timeit.Timer(
'''
a = data[:]
set_of_data = set(data)
bst = BST.build_from_list(a)
for _ in range(n//10):
    rnd = random.sample(set_of_data, 1)[0]
    bst.search(rnd)
''',
        globals=globals(),
        setup=setup).repeat(4, 10)) for suffix, setup in setups.items()})

    results.update({'BST_delete' + suffix: min(timeit.Timer(
'''
a = data[:]
set_of_data = set(data)
bst = BST.build_from_list(a)
for _ in range(n//10):
    rnd = random.sample(set_of_data, 1)[0]
    bst.delete_by_key(rnd)
    set_of_data.remove(rnd)
''',
        globals=globals(),
        setup=setup).repeat(4, 10)) for suffix, setup in setups.items()})

    # AVL tree built from ordered and randomized data
    results.update({'AVL_search' + suffix: min(timeit.Timer(
'''
a = data[:]
set_of_data = set(data)
avl = AvlTree.build_from_list(a)
for _ in range(n//10):
    rnd = random.sample(set_of_data, 1)[0]
    avl.search(rnd)
''',
        globals=globals(),
        setup=setup).repeat(4, 10)) for suffix, setup in setups.items()})

    results.update({'AVL_delete' + suffix: min(timeit.Timer(
'''
a = data[:]
set_of_data = set(data)
avl = AvlTree.build_from_list(a)
for _ in range(n//10):
    rnd = random.sample(set_of_data, 1)[0]
    avl.delete_by_key(rnd)
    set_of_data.remove(rnd)
''',
        globals=globals(),
        setup=setup).repeat(4, 10)) for suffix, setup in setups.items()})
    return results


if __name__ == '__main__':
    n = [20 * (2**k) for k in range(7)]
    pool = Pool(4)
    output = pool.map(compare_performance, n)
    with open('simple_bst_comparison.csv', 'w', newline='') as csvfile:
        fieldnames = ['N',
                      'BST_search_ordered', 'BST_search_shuffled',
                      'BST_delete_ordered', 'BST_delete_shuffled',
                      'AVL_search_ordered', 'AVL_search_shuffled',
                      'AVL_delete_ordered', 'AVL_delete_shuffled']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for res_for_n in output:
            writer.writerow(res_for_n)
