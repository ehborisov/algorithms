from __future__ import annotations
from typing import List, Any, Optional


class Node(object):

    def __init__(self, key: Any, parent=None):
        self.key = key
        self.parent = parent
        self.left = None
        self.right = None


class BST(object):

    def __init__(self):
        self.root = None

    @classmethod
    def build_from_list(cls, input_list: List) -> BST:
        bst = BST()
        for e in input_list:
            bst.insert(e)
        return bst

    def insert(self, key: Any) -> None:
        p1 = None
        p2 = self.root
        node = Node(key, None)
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

    def search(self, x: Any) -> Optional[Any]:
        if not self.root:
            return None
        p = self.root
        while True:
            if p.key == x:
                return p
            elif p.key < x and p.left:
                p = p.left
            elif p.key > x and p.right:
                p = p.right
            else:
                return None

    def search_recursive(self, x: Any) -> Optional[Any]:
        def _search(node, x):
            if x is None or node.key == x:
                return node
            return _search(node.left if node.key < x else node.right, x)
        return _search(self.root, x)

    def minimum(self, node):
        while node and node.left:
            node = node.left
        if not node:
            raise ValueError('Couldn\'t find minimum, the tree is empty.')
        return node

    def maximum(self, node):
        while node and node.right:
            node = node.right
        if not node:
            raise ValueError('Couldn\'t find maximum, the tree is empty.')
        return node

    def successor(self, node):
        if node.right:
            return self.minimum(node.right)
        y = node.parent
        while y is not None and node == y.right:
            node = y
            y = y.parent
        return y

    def predecessor(self, node):
        if node.left:
            return self.maximum(node.left)
        y = node.parent
        while y is not None and node == y.left:
            node = y
            y = y.parent
        return y

    def inorder_recursive_walk(self):
        def walk(x):
            if x is not None:
                walk(x.left)
                print(x.key)
                walk(x.right)
        return walk(self.root)

    def iterative_inorder(self) -> List[Any]:
        values = []
        if not self.root:
            return values
        p = self.root
        while True:
            while p and p.left:
                p = p.left
            values.append(p.key)
            if p and p.right:
                p = p.right
            else:
                while p.parent.right == p or not p.parent.right:
                    p = p.parent
                    if not p.right:
                        values.append(p.key)
                    if not p.parent:
                        print(f'returning {values}')
                        return values
                values.append(p.parent.key)
                p = p.parent.right

    def _transplant(self, node_from: Node, node: Node) -> None:
        if node_from.parent is None:
            self.root = node
        elif node_from.parent.left == node_from:
            node_from.parent.left = node
        else:
            node_from.parent.right = node
        if node_from.parent and node:
            node.parent = node_from.parent

    def delete_by_key(self, key: Any):
        node = self.search(key)
        if not node:
            raise Exception(f"No such node with key {key}")
        self.delete(node)

    def delete(self, node: Node) -> None:
        if node.left is None:
            self._transplant(node, node.right)
        elif node.right is None:
            self._transplant(node, node.left)
        else:
            p = self.minimum(node.right)
            if p.parent != node:
                self._transplant(p, p.right)
                p.right = node.right
                node.right.parent = p
                p.left = node.left
            else:
                self._transplant(node, node.right)
