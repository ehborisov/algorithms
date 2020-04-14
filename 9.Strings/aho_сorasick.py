"""
Implentation is based on the article https://www.toptal.com/algorithms/aho-corasick-algorithm
"""
import queue

from suffix_trie import SuffixTrie
from typing import List, Iterable


class AhoCorasickPatternMatcher(object):

    def __init__(self, patterns: Iterable[str]):
        self.suffix_trie = SuffixTrie()
        self.patterns_map = {}
        for i, p in enumerate(patterns):
            self.patterns_map[i] = p
            self.suffix_trie.add_pattern(p, i)
        q = queue.Queue()
        q.put(0)
        # just a bfs traversal
        while q:
            v_index = q.get()
            self.suffix_trie.calculate_suffix_links(v_index)
            for key in self.suffix_trie.trie[v_index].children:
                q.put(self.suffix_trie.trie[v_index].children[key])

    def search(self, text: str) -> List[int]:
        vertex_pointer = 0
        matches = []

        for j in range(len(text)):
            while True:
                if text[j] in self.suffix_trie.trie[vertex_pointer].children:
                    vertex_pointer = self.suffix_trie.trie[vertex_pointer].children[text[j]]
                    break

                if vertex_pointer == 0:
                    break

                vertex_pointer = self.suffix_trie.trie[vertex_pointer].suffix_link

            while True:
                vertex_pointer = self.suffix_trie.trie[vertex_pointer].end_word_link

                if vertex_pointer == 0:
                    break

                matches.append(j + 1 - self.suffix_trie.word_lengths[self.suffix_trie.trie[vertex_pointer].word_id])

                vertex_pointer = self.suffix_trie.trie[vertex_pointer].suffix_link

        return matches
