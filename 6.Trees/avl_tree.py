from __future__ import annotations

from binary_tree import BST, Node
from typing import Any, List


class AvlNode(Node):
    def __init__(self, key, parent=None):
        super().__init__(key, parent)
        self.height = 1

    @property
    def balance(self) -> int:
        return getattr(self.right, 'height', 0) - getattr(self.left, 'height', 0)

    def fix_height(self):
        left_height = getattr(self.left, 'height', 0)
        right_height = getattr(self.right, 'height', 0)
        self.height = (left_height if left_height > right_height else right_height) + 1


class AvlTree(BST):

    def __init__(self):
        super().__init__()

    @staticmethod
    def _small_left_rotation(node: AvlNode) -> AvlNode:
        y = node.right
        if y:
            node.right = y.left
            if y.left:
                y.left.parent = node
            y.left = node
            node.parent = y
        node.fix_height()
        y.fix_height()
        return y

    @staticmethod
    def _small_right_rotation(node: AvlNode) -> AvlNode:
        x = node.left
        if x:
            node.left = x.right
            if node.left:
                node.left.parent = node
            x.right = node
            node.parent = x
        node.fix_height()
        x.fix_height()
        return x

    @staticmethod
    def _balance(node: AvlNode):
        node.fix_height()
        if node.balance == 2:
            if node.right.balance < 0:
                node.right = AvlTree._small_right_rotation(node.right)
                node.right.parent = node
            return AvlTree._small_left_rotation(node)
        if node.balance == -2:
            if node.left.balance > 0:
                node.left = AvlTree._small_left_rotation(node.left)
                node.left.parent = node
            return AvlTree._small_right_rotation(node)
        return node

    @classmethod
    def build_from_list(cls, input_list: List) -> AvlTree:
        avl = AvlTree()
        for e in input_list:
            avl.insert(e)
        return avl

    def insert(self, key: Any):
        p1 = None
        p2 = self.root
        node = AvlNode(key, None)
        while p2 is not None:
            p1 = p2
            if node.key < p2.key:
                p2 = p2.left
            else:
                p2 = p2.right
        node.parent = p1
        if p1 is None:
            self.root = node
        elif p1.key > node.key:
            p1.left = node
        else:
            p1.right = node
        # node is inserted, adjusting heights and rebalancing
        while node.parent:
            p = node.parent.parent
            is_left = p and (p.left == node.parent)
            node = AvlTree._balance(node.parent)
            node.parent = p
            if p and is_left:
                p.left = node
            elif p:
                p.right = node

        self.root = node

    def delete(self, node: AvlNode):
        p = node.parent
        if node.left is None:
            self._transplant(node, node.right)
            if node.right:
                node.right.fix_height()
        elif node.right is None:
            self._transplant(node, node.left)
            if node.left:
                node.left.fix_height()
        else:
            p = self.minimum(node.right)
            if p.parent != node:
                self._transplant(p, p.right)
                p.right = node.right
                p.right.parent = p
                p.right.fix_height()
            self._transplant(node, p)
            p.left = node.left
            p.left.parent = p
            p.left.fix_height()
            p.fix_height()
        if not p:
            if self.root:
                self.root = AvlTree._balance(self.root)
            return
        while p.parent:
            tmp = p.parent
            is_left = tmp.left == p
            p = AvlTree._balance(p)
            p.parent = tmp
            if is_left:
                tmp.left = p
            else:
                tmp.right = p
            p = p.parent
        self.root = p
