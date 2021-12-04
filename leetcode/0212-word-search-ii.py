from typing import List
from collections import defaultdict


class Trie:
    def __init__(self, words=[]):
        self.children = defaultdict(Trie)
        self.hit_word = None
        for word in words:
            self.insert(word)

    def insert(self, word: str) -> None:
        cursor = self
        for c in word:
            cursor = cursor.children[c]
        cursor.hit_word = word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m = len(board)
        n = len(board[0])

        def iter_result(trie, x, y):
            c = board[x][y]
            if c not in trie.children:
                return
            child = trie.children[c]
            if child.hit_word:
                yield child.hit_word
            board[x][y] = '#'
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if 0 <= x+dx < m and 0 <= y+dy < n:
                    yield from iter_result(child, x+dx, y+dy)
            board[x][y] = c

        result = set()
        trie = Trie(words)
        for x in range(m):
            for y in range(n):
                result.update(iter_result(trie, x, y))
        return result


## TC: O(m*n*l^3) where l is the length of the longest word
## SC: O(L) where L is the total length of the words
