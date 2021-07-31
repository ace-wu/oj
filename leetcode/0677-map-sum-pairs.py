from typing import List

class Node:
    def __init__(self):
        self.value = 0
        self.children = None

    def insert(self, index_list: List[int], value: int):
        cursor = self
        for i in index_list:
            if cursor.children is None:
                cursor.children = [None] * 26
            if cursor.children[i] is None:
                cursor.children[i] = Node()
            cursor = cursor.children[i]
        cursor.value = value

    def sum(self, index_list: List[int]):
        cursor = self
        for i in index_list:
            if cursor.children is None:
                return 0
            if cursor.children[i] is None:
                return 0
            cursor = cursor.children[i]
        total = 0
        if cursor:
            stack = [cursor]
        while stack:
            cursor = stack.pop()
            total += cursor.value
            if cursor.children:
                stack.extend(child for child in cursor.children if child)
        return total


class MapSum:
    def __init__(self):
        self.ord_a = ord('a')
        self.trie = Node()
        pass

    def insert(self, key: str, val: int) -> None:
        self.trie.insert(self.str_to_index_list(key), val)

    def sum(self, prefix: str) -> int:
        return self.trie.sum(self.str_to_index_list(prefix))

    def str_to_index_list(self, text):
        return [ord(c) - self.ord_a for c in text]


s = MapSum()
s.insert('apple', 3)
print(s.sum('ap'))
s.insert('app', 2)
print(s.sum('ap'))
