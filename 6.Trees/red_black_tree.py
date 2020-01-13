from __future__ import annotations

from enum import Enum
from binary_tree import Node
from typing import Any, List, Union, Optional


class Color(Enum):
    RED = True
    BLACK = False


class RedBlackNode(Node):

    def __init__(self, key, parent=None):
        super().__init__(key, parent)
        self.color = Color.RED
        self.left = NilNode()
        self.right = NilNode()


class NilNode(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, NilNode):
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.color = Color.BLACK


class RedBlackTree(object):

    @classmethod
    def build_from_list(cls, input_list: List) -> RedBlackTree:
        red_black = RedBlackTree()
        for e in input_list:
            red_black.insert(e)
        return red_black

    @staticmethod
    def _left_rotation(node: RedBlackNode) -> RedBlackNode:
        y = node.right
        if y != NilNode():
            node.right = y.left
            if y.left != NilNode():
                y.left.parent = node
            y.left = node
            node.parent = y
        return y

    @staticmethod
    def _right_rotation(node: RedBlackNode) -> RedBlackNode:
        x = node.left
        if x != NilNode():
            node.left = x.right
            if node.left != NilNode():
                node.left.parent = node
            x.right = node
            node.parent = x
        return x

    def __init__(self):
        self.nil = NilNode()
        self.root = self.nil

    def search(self, x: Any) -> Optional[Any]:
        if self.root == self.nil:
            return None
        p = self.root
        while True:
            if p.key == x:
                return p
            elif p.key > x and p.left != self.nil:
                p = p.left
            elif p.key < x and p.right != self.nil:
                p = p.right
            else:
                return None

    def insert(self, key: Any) -> None:
        p1 = self.nil
        p2 = self.root
        while p2 != self.nil:
            p1 = p2
            if key < p2.key:
                p2 = p2.left
            else:
                p2 = p2.right
        node = RedBlackNode(key, p1)
        if p1 == self.nil:
            self.root = node
        elif key > p1.key:
            p1.right = node
        else:
            p1.left = node
        self._rb_insert_fixup(node)

    def _rb_insert_fixup(self, node: RedBlackNode) -> None:
        while node.parent.color == Color.RED:
            if node.parent.parent.left == node.parent:
                y = node.parent.parent.right  # Uncle
                if y.color == Color.RED:
                    # case 1: repaint Uncle and Parent black, Grandparent red
                    node.parent.color = Color.BLACK
                    y.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    node = node.parent.parent
                else:
                    if node.parent.right == node:
                        # case 2: do left rotation at node parent first
                        node = node.parent
                        tmp = node.parent
                        is_left = (tmp != self.nil) and (tmp.left == node)
                        node = RedBlackTree._left_rotation(node)
                        self._fix_parent_child_links(node, tmp, is_left)
                        # move the node pointer into case 3 position
                        node = node.left
                    # cases 2,3: repaint Parent black, Grandparent red
                    node.parent.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    tmp = node.parent.parent.parent
                    is_left = (tmp != self.nil) and (tmp.left == node.parent.parent)
                    node = RedBlackTree._right_rotation(node.parent.parent)
                    self._fix_parent_child_links(node, tmp, is_left)
            else:
                # symmetric to cases 1-3
                y = node.parent.parent.left  # Uncle
                if y.color == Color.RED:
                    node.parent.color = Color.BLACK
                    y.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    node = node.parent.parent
                else:
                    if node.parent.left == node:
                        node = node.parent
                        tmp = node.parent
                        is_left = (tmp != self.nil) and (tmp.left == node)
                        node = RedBlackTree._right_rotation(node)
                        self._fix_parent_child_links(node, tmp, is_left)
                        node = node.right
                    node.parent.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    tmp = node.parent.parent.parent
                    is_left = (tmp != self.nil) and (tmp.left == node.parent.parent)
                    node = RedBlackTree._left_rotation(node.parent.parent)
                    self._fix_parent_child_links(node, tmp, is_left)
        self.root.color = Color.BLACK

    def _fix_parent_child_links(self, node: RedBlackNode, parent: RedBlackNode, is_left: bool) -> None:
        node.parent = parent
        if parent != self.nil and is_left:
            parent.left = node
        else:
            parent.right = node
        if parent == self.nil:
            self.root = node

    def _transplant(self, node_from: RedBlackNode, node: Union[RedBlackNode, NilNode]) -> None:
        if node_from.parent == self.nil:
            self.root = node
        else:
            if node_from.parent.left == node_from:
                node_from.parent.left = node
            else:
                node_from.parent.right = node
        node.parent = node_from.parent

    def delete_by_key(self, key: Any):
        node = self.search(key)
        if not node:
            raise Exception(f"No such node with key {key}")
        self.delete(node)

    def delete(self, node: RedBlackNode) -> None:
        y = node
        y_color = y.color
        if node.left == self.nil:
            x = node.right
            self._transplant(node, node.right)
        elif node.right == self.nil:
            x = node.left
            self._transplant(node, node.left)
        else:
            y = self.minimum(node.right)
            y_color = y.color
            x = y.right
            if y.parent != node:
                self._transplant(y, y.right)
                y.right = node.right
                y.right.parent = y
            else:
                x.parent = y
            self._transplant(node, y)
            y.left = node.left
            y.left.parent = y
            y.color = node.color
        if y_color == Color.BLACK:
            self._rb_delete_fixup(x)

    def _rb_delete_fixup(self, node: Union[RedBlackNode, NilNode]) -> None:
        while node != self.root and node.color == Color.BLACK:
            if node == node.parent.left:
                s = node.parent.right  # sibling
                if s.color == Color.RED:  # case 1
                    s.color = Color.BLACK
                    node.parent.color = Color.RED
                    tmp = node.parent.parent
                    is_left = (tmp != self.nil) and (tmp.left == node.parent)
                    new_node_parent = RedBlackTree._left_rotation(node.parent)
                    self._fix_parent_child_links(new_node_parent, tmp, is_left)
                    s = new_node_parent.right
                if s.left.color == Color.BLACK and s.right.color == Color.BLACK:  # case 2, s is already black
                    s.color = Color.RED
                    node = node.parent
                else:
                    if s.right.color == Color.BLACK:
                        s.left.color = Color.BLACK
                        s.color = Color.RED
                        tmp = s.parent
                        is_left = (tmp != self.nil) and (tmp.left == s)
                        s = self._right_rotation(s)
                        self._fix_parent_child_links(s, tmp, is_left)
                        s = node.parent.right
                    s.color = node.parent.color
                    node.parent.color = Color.BLACK
                    s.right.color = Color.BLACK
                    tmp = node.parent.parent
                    is_left = (tmp != self.nil) and (tmp.left == node.parent)
                    new_node_parent = RedBlackTree._left_rotation(node.parent)
                    self._fix_parent_child_links(new_node_parent, tmp, is_left)
                    node = self.root
            else:
                s = node.parent.left
                if s.color == Color.RED:
                    s.color = Color.BLACK
                    node.parent.color = Color.RED
                    tmp = node.parent.parent
                    is_left = (tmp != self.nil) and (tmp.left == node.parent)
                    new_node_parent = RedBlackTree._right_rotation(node.parent)
                    self._fix_parent_child_links(new_node_parent, tmp, is_left)
                    s = new_node_parent.left
                if s.right.color == Color.BLACK and s.right.color == Color.BLACK:
                    s.color = Color.RED
                    node = node.parent
                else:
                    if s.left.color == Color.BLACK:
                        s.right.color = Color.BLACK
                        s.color = Color.RED
                        tmp = s.parent
                        is_left = (tmp != self.nil) and (tmp.left == s)
                        s = self._left_rotation(s)
                        self._fix_parent_child_links(s, tmp, is_left)
                        s = node.parent.left
                    s.color = node.parent.color
                    node.parent.color = Color.BLACK
                    s.left.color = Color.BLACK
                    tmp = node.parent.parent
                    is_left = (tmp != self.nil) and (tmp.left == node.parent)
                    new_node_parent = RedBlackTree._right_rotation(node.parent)
                    self._fix_parent_child_links(new_node_parent, tmp, is_left)
                    node = self.root
        node.color = Color.BLACK

    def minimum(self, node: Union[RedBlackNode, NilNode]) -> RedBlackNode:
        while (node != self.nil) and (node.left != self.nil):
            node = node.left
        if node == self.nil:
            raise ValueError('Couldn\'t find minimum, the tree is empty.')
        return node

    def iterative_inorder(self) -> List[Any]:
        values = []
        if self.root == self.nil:
            return values
        p = self.root
        while True:
            while (p != self.nil) and (p.left != self.nil):
                p = p.left
            values.append(p.key)
            if (p != self.nil) and (p.right != self.nil):
                p = p.right
            elif p.parent == self.nil and p.left == self.nil and p.right == self.nil:
                return values
            else:
                while p.parent.right == p or p.parent.right == self.nil:
                    p = p.parent
                    if p.right == self.nil:
                        values.append(p.key)
                    if p.parent == self.nil:
                        return values
                values.append(p.parent.key)
                p = p.parent.right
