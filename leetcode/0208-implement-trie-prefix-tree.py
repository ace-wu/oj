from collections import defaultdict


class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.is_ending = False

    def insert(self, word: str, index=0) -> None:
        cursor = self
        for c in word:
            cursor = cursor.children[c]
        cursor.is_ending = True

    def search(self, word: str, index=0) -> bool:
        cursor = self
        for c in word:
            if c not in cursor.children:
                return False
            cursor = cursor.children[c]
        return cursor.is_ending

    def startsWith(self, prefix: str, index=0) -> bool:
        cursor = self
        for c in prefix:
            if c not in cursor.children:
                return False
            cursor = cursor.children[c]
        return True


## TC: O(n) where n is the length of the query word/prefix
## SC: O(N) where N is the total length of inserted words
