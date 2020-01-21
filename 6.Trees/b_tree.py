from __future__ import annotations
from typing import List, Any, Optional, Tuple


class BNode(object):

    def __init__(self, keys: Optional[List[Any]] = None):
        self.keys = keys or []
        self.children = []

    @property
    def is_leaf(self):
        return not self.children

    @property
    def size(self):
        return len(self.keys)


class BTree(object):

    def __init__(self, min_degree: int):
        self.degree = min_degree
        self.root = None

    def _search(self, node: BNode, key: Any) -> Optional[Tuple[Any, int]]:
        if not node:
            return None
        i = 0
        while i < node.size and key > node.keys[i]:
            i += 1
        if i < node.size and key == node.keys[i]:
            return node, i
        elif node.is_leaf:
            return None
        else:
            return self._search(node.children[i], key)

    def search(self, key) -> Optional[Any]:
        result = self._search(self.root, key)
        if result:
            node, i = result
            return node[i]

    def _split_child(self, node: BNode, i: int) -> None:
        z = BNode()
        # i-th child is a full node and has 2t - 1 keys and 2t children
        y = node.children[i]
        z.keys = y.keys[self.degree: 2 * self.degree]  # y has 2t - 1 keys
        z.children = y.children[self.degree: 2 * self.degree + 1]  # y has 2t children
        node.keys.insert(i, y.keys[self.degree])
        node.children.insert(i + 1, z)
        # adjust the split node in size
        y.keys = y.keys[0: self.degree]
        y.children = y.children[0: self.degree + 1]

    def insert(self, key: Any) -> None:
        r = self.root
        if r.size == 2 * self.degree - 1:
            node = BNode()
            self.root = node
            node.children.append(r)
            self._split_child(node, 0)
            self._insert_nonfull(node, key)
        else:
            self._insert_nonfull(r, key)

    def _insert_nonfull(self, node: BNode, key: Any) -> None:
        i = node.size - 1
        while i > 0 and key < node.keys[i]:
            i -= 1
        if node.is_leaf:
            node.keys.insert(i + 1, key)
        else:
            i += 1
            if node.children[i].size == 2 * self.degree - 1:
                self._split_child(node, i)
                if key > node.keys[i]:
                    i += 1
            self._insert_nonfull(node.children[i], key)

    def delete_by_key(self, key: Any):
        self._delete(self.root, key)

    def _delete(self, node: BNode, key: Any) -> None:
        try:
            i = node.keys.index(key)
        except ValueError:
            i = None
        if i is not None and node.is_leaf:
            node.keys.remove(key)
            return  # end of recursive delete call ending with removal of some node from the leaf
        elif i is None and node.is_leaf:
            raise KeyError(f"No such key to delete {key}.")  # Recursion end for the case when key is not in the tree
            # and we searched all the way down to the leaf.
        elif i is not None:
            pred_node = node.children[i]
            following_node = node.children[i + 1]
            if pred_node.size >= self.degree:
                pred_key = pred_node.keys[-1]
                node.keys.insert(i, pred_key)
                self._delete(pred_node, pred_key)
            elif pred_node.size < self.degree <= following_node.size:
                following_key = following_node.keys[0]
                node.keys.insert(i, following_key)
                self._delete(following_node, following_key)
            else:
                # two t - 1 sized nodes as predecessor and following nodes exist for the key being deleted
                # moving everything into predecessor, deleting the following, proceeding to delete the same key
                # in the new 2t - 1 - sized predecessor node.
                pred_node.keys.append(key)
                pred_node.keys.extend(following_node.keys)
                pred_node.children.extend(following_node.children)
                node.keys.remove(key)
                node.children.remove(following_node)
                self._delete(pred_node, key)
        else:
            child_index = None
            if key < node.keys[0]:
                child_index = 0
            elif key > node.keys[-1]:
                child_index = node.size
            for i in range(node.size - 1):
                if node.keys[i] < key < node.keys[i + 1]:
                    child_index = i
                    break
            if (node.children[child_index].size == self.degree - 1 and child_index < node.size
                    and node.children[child_index + 1].size >= self.degree):
                key_to_move_down_from_node = node.keys.pop(child_index)
                node.children[child_index].keys.append(key_to_move_down_from_node)
                sibling_key_to_move_up = node.children[child_index + 1].keys.pop(0)
                sibling_child_to_move_up = node.children[child_index + 1].children.pop(0)
                node.keys.append(sibling_key_to_move_up)
                node.children.append(sibling_child_to_move_up)
            elif (node.children[child_index].size == self.degree - 1 and child_index > 0
                    and node.children[child_index - 1].size >= self.degree):
                key_to_move_down_from_node = node.keys.pop(child_index)
                node.children[child_index].keys.append(key_to_move_down_from_node)
                sibling_key_to_move_up = node.children[child_index - 1].keys.pop(0)
                sibling_child_to_move_up = node.children[child_index - 1].children.pop(0)
                node.keys.insert(0, sibling_key_to_move_up)
                node.children.insert(0, sibling_child_to_move_up)
            else:
                # merge node at child_index with one of the siblings
                sibling_index = child_index - 1 if child_index > 0 else child_index + 1
                sibling_to_merge = node.children.pop(sibling_index)
                median_key_to_move_down = node.keys.pop(child_index)
                node.children[child_index].keys.append(median_key_to_move_down)
                node.children[child_index].keys.extend(sibling_to_merge.keys)
                node.children[child_index].children.extend(sibling_to_merge.children)
            self._delete(node.children[child_index], key)
