import unittest
from binary_tree import BST
from parameterized import parameterized


class BinaryTreeTest(unittest.TestCase):

    @parameterized.expand(
        [
            [None, [0], [0]],
            [None, [1, 2], [1, 2]],
            [None, [2, 1], [1, 2]],
            [None, [4, 2, 5], [2, 4, 5]],
            [None, [4, 5, 2, 0, 8, 11, 22, 9, 1], [0, 1, 2, 4, 5, 8, 9, 11, 22]],
        ]
    )
    def test_build_bst(self, _, input_data, expected):
        bst = BST.build_from_list(input_data)
        inorder = bst.iterative_inorder()
        assert inorder == expected

    @parameterized.expand(
        [
            [None, [0], 0],
            [None, [2, 1, 3], 1],
            [None, [2, 1, 3], 3],
            [None, [2, 1, 3], 1],
            [None, [4, 5, 2, 0, 8, 11, 22, 9, 1], 5],
        ]
    )
    def test_delete(self, _, input_data, key):
        bst = BST.build_from_list(input_data)
        bst.delete_by_key(key)
        res = set(bst.iterative_inorder())
        assert key not in res


if __name__ == '__main__':
    unittest.main()
