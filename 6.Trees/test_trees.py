import unittest
from binary_tree import BST
from avl_tree import AvlTree
from red_black_tree import RedBlackTree
from b_tree import BTree
from parameterized import parameterized


BUILD_DATA = [
    [None, [0], [0]],
    [None, [1, 2], [1, 2]],
    [None, [2, 1], [1, 2]],
    [None, [4, 2, 5], [2, 4, 5]],
    [None, [4, 5, 2, 0, 8, 11, 22, 9, 1], [0, 1, 2, 4, 5, 8, 9, 11, 22]],
    [None, [-1, 5, -8, 3, 10, -3, 1, 20, 32, 6, -15], [-15, -8, -3, -1, 1, 3, 5, 6, 10, 20, 32]],
]


DELETE_DATA = [
    [None, [0], 0],
    [None, [2, 1, 3], 1],
    [None, [2, 1, 3], 3],
    [None, [2, 1, 3], 1],
    [None, [4, 5, 2, 0, 8, 11, 22, 9, 1], 5],
]


DELETE_MULTIPLE_DATA = [
    [None, [5, 3, 1, 6, 4, 0], [6, 3], [0, 1, 4, 5]],
    [None, [4, 5, 2, 0, 8, 11, 22, 9, 1], [5, 1], [0, 2, 4, 8, 9, 11, 22]],
    [None, [4, 5, 2, 0, 8, 11, 22, 9, 1], [11, 0, 8, 9, 22, 4], [1, 2, 5]],
    [None, [-1, 5, -8, 3, 10, -3, 1, 20, 32, 6, -15], [-1, 20, -15, -8], [-3, 1, 3, 5, 6, 10, 32]]
]


class BinaryTreeTest(unittest.TestCase):

    @parameterized.expand(BUILD_DATA)
    def test_build_bst(self, _, input_data, expected):
        bst = BST.build_from_list(input_data)
        inorder = bst.iterative_inorder()
        assert inorder == expected

    @parameterized.expand(BUILD_DATA)
    def test_build_avl(self, _, input_data, expected):
        avl = AvlTree.build_from_list(input_data)
        inorder = avl.iterative_inorder()
        assert inorder == expected

    @parameterized.expand(BUILD_DATA)
    def test_build_red_black(self, _, input_data, expected):
        red_black = RedBlackTree.build_from_list(input_data)
        inorder = red_black.iterative_inorder()
        assert inorder == expected

    @parameterized.expand(BUILD_DATA)
    def test_build_b_tree(self, _, input_data, expected):
        b_tree = BTree.build_from_list(input_data, 2)
        inorder = b_tree.inorder_walk()
        assert inorder == expected

    @parameterized.expand(DELETE_DATA)
    def test_delete(self, _, input_data, key):
        bst = BST.build_from_list(input_data)
        bst.delete_by_key(key)
        res = set(bst.iterative_inorder())
        assert key not in res

    @parameterized.expand(DELETE_DATA)
    def test_delete_in_avl(self, _, input_data, key):
        avl = AvlTree.build_from_list(input_data)
        avl.delete_by_key(key)
        res = set(avl.iterative_inorder())
        assert key not in res

    @parameterized.expand(DELETE_DATA)
    def test_delete_in_b_tree(self, _, input_data, key):
        b_tree = BTree.build_from_list(input_data, 2)
        b_tree.delete_by_key(key)
        res = set(b_tree.inorder_walk())
        assert key not in res

    @parameterized.expand(DELETE_MULTIPLE_DATA)
    def test_delete_multiple_bst(self, _, input_data, delete_data, expected_result):
        bst = BST.build_from_list(input_data)
        for key in delete_data:
            bst.delete_by_key(key)
        res = bst.iterative_inorder()
        assert expected_result == res

    @parameterized.expand(DELETE_MULTIPLE_DATA)
    def test_delete_multiple_b_tree(self, _, input_data, delete_data, expected_result):
        b_tree = BTree.build_from_list(input_data, 2)
        for key in delete_data:
            b_tree.delete_by_key(key)
        res = b_tree.inorder_walk()
        assert expected_result == res

    @parameterized.expand(DELETE_MULTIPLE_DATA)
    def test_delete_multiple_avl(self, _, input_data, delete_data, expected_result):
        avl = AvlTree.build_from_list(input_data)
        for key in delete_data:
            avl.delete_by_key(key)
        res = avl.iterative_inorder()
        assert expected_result == res

    @parameterized.expand(DELETE_DATA)
    def test_delete_in_red_black(self, _, input_data, key):
        rb = RedBlackTree.build_from_list(input_data)
        rb.delete_by_key(key)
        res = set(rb.iterative_inorder())
        assert key not in res

    @parameterized.expand(DELETE_MULTIPLE_DATA)
    def test_delete_multiple_red_black(self, _, input_data, delete_data, expected_result):
        rb = RedBlackTree.build_from_list(input_data)
        for key in delete_data:
            rb.delete_by_key(key)
        res = rb.iterative_inorder()
        assert expected_result == res


if __name__ == '__main__':
    unittest.main()
