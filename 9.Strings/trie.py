from typing import Tuple, Optional
import string

ALPHABET = tuple(string.printable)


class TrieNode(object):

    def __init__(self, key: str, alphabet: Tuple[str] = ALPHABET):
        self.key = key
        self.alphabet = alphabet
        self.children = dict.fromkeys(self.alphabet)
        self.word = False


class Trie(object):

    def __init__(self):
        self.root = TrieNode('')

    def add(self, word: Optional[str] = None) -> None:
        node_pointer = self.root
        for k in word:
            if not node_pointer.children[k]:
                node_pointer.children[k] = TrieNode(k)
            node_pointer = node_pointer.children[k]
        node_pointer.word = True

    def search(self, word: str) -> bool:
        node_pointer = self.root
        for k in word:
            if not node_pointer.children[k]:
                return False
            node_pointer = node_pointer.children[k]
        return True

    def delete(self, word: str):
        nodes_traversed = [self.root]
        for k in word:
            if not nodes_traversed[-1].children[k]:
                raise KeyError(f"No such word in the Trie: {word}")
            nodes_traversed.append(nodes_traversed[-1].children[k])
        nodes_traversed[-1].word = False
        prev = nodes_traversed[-2]
        while prev != self.root:
            node = nodes_traversed.pop()
            if not any(node.children.values()):
                prev.children[node.key] = None
                prev = nodes_traversed[-2]
            else:
                break
