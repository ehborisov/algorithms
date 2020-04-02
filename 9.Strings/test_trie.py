import unittest

from typing import Tuple
from trie import Trie
from parameterized import parameterized


def construct_trie_from_words(words: Tuple[str]) -> Trie:
    t = Trie()
    for word in words:
        t.add(word)
    return t


class TrieTest(unittest.TestCase):

    @parameterized.expand([
        [None, ('abc', 'abcde', 'acbed', 'abcdeb'), 'abc', True],
        [None, ('abc', 'abcde', 'acbed', 'abcdeb'), 'abcde', True],
        [None, ('abc', 'abcde', 'acbed', 'abcdeb'), 'abcg', False],
        [None, ('abc', 'abcde', 'acbed', 'abcdeb'), 'abcdg', False],
        [None, ('abc', 'abcde', 'acbed', 'abcdeb'), 'abcdeb', True],
    ])
    def test_search_word(self, _, words, query, is_found):
        t = construct_trie_from_words(words)
        result = t.search(query)
        assert result == is_found

    @parameterized.expand([
        [None, ('abc', 'abcde', 'acbed', 'abcdeb'), ('abcdeb', 'acbed'), 'abcdeb', False],
        [None, ('abc', 'abcde', 'acbed', 'abcdeb'), ('abc',), 'abc', True],
        [None, ('abc', 'abcde', 'acbed', 'abcdeb'), ('abc', 'abcde'), 'abc', True],
        [None, ('abc', 'abcde', 'acbed', 'adcdeb'), ('abc', 'abcde'), 'abc', False],
    ])
    def test_delete_word(self, _, words, words_to_delete, query, is_found):
        t = construct_trie_from_words(words)
        for w in words_to_delete:
            t.delete(w)
        result = t.search(query)
        assert result == is_found
