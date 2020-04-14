class SuffixNode(object):

    def __init__(self):
        self.children = dict()
        self.is_word = False
        self.word_id = None
        self.parent = None
        self.parent_key = None
        self.suffix_link = None
        self.end_word_link = None


class SuffixTrie(object):

    def __init__(self):
        self.trie = [SuffixNode()]  # init with an empty root
        self.word_lengths = {}
        self.size = 1

    def add_pattern(self, pattern: str, word_id: int) -> None:
        vertex_ptr = 0
        for c in pattern:
            if c not in self.trie[vertex_ptr]:
                self.trie.append(SuffixNode())
                self.trie[self.size].parent = vertex_ptr
                self.trie[self.size].parent_key = c
                self.trie[vertex_ptr].children[c] = self.size
                self.size += 1
            vertex_ptr = self.trie[vertex_ptr].children[c]
        self.trie[vertex_ptr].is_word = True
        self.trie[vertex_ptr].word_id = word_id
        self.word_lengths[word_id] = len(pattern)

    def calculate_suffix_links(self, vertex_pointer: int):
        if vertex_pointer == 0:
            self.trie[vertex_pointer].suffix_link = 0
            self.trie[vertex_pointer].end_word_link = 0
            return

        # case for 1-character words
        if self.trie[vertex_pointer].parent == 0:
            self.trie[vertex_pointer].suffix_link = 0
            if self.trie[vertex_pointer].is_word:
                self.trie[vertex_pointer].end_word_link = vertex_pointer
            else:
                self.trie[vertex_pointer].end_word_link = self.trie[self.trie[vertex_pointer].suffix_link].end_word_link
            return

        current_suff_link = self.trie[self.trie[vertex_pointer].parent].suffix_link
        # char that led to the current vertex
        parent_char = self.trie[vertex_pointer].parent_key

        while True:
            if parent_char in self.trie[current_suff_link].children:
                # suffix link with matching character is found in some branch of the tree
                self.trie[vertex_pointer].suffix_link = self.trie[current_suff_link].children[parent_char]
                break

            if current_suff_link == 0:
                self.trie[vertex_pointer].suffix_link = 0
                break

            current_suff_link = self.trie[current_suff_link].suffix_link

        if self.trie[vertex_pointer].is_word:
            self.trie[vertex_pointer].end_word_link = vertex_pointer
        else:
            self.trie[vertex_pointer].end_word_link = self.trie[self.trie[vertex_pointer].suffix_link].end_word_link
