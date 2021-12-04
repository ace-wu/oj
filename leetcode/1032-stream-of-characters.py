from collections import defaultdict


class Trie:
    def __init__(self, words=[]):
        self.children = defaultdict(Trie)
        self.hit_word = None
        for word in words:
            self.insert(word)

    def insert(self, word):
        cursor = self
        for c in word:
            cursor = cursor.children[c]
        cursor.hit_word = word


class StreamChecker:
    def __init__(self, words: List[str]):
        self.trie = Trie(words)
        self.cursors = []

    def query(self, letter: str) -> bool:
        self.cursors.append(self.trie)
        self.cursors = [cursor.children[letter] for cursor in self.cursors if letter in cursor.children]
        return any(cursor.hit_word is not None for cursor in self.cursors)



## TC: O(max(w)) for each query
## SC: O(sum(w))
## where max(w) is the maximum length of all words
##       sum(w) is the total length of all words
## can be further improved by the Aho-Corasick algorithm
