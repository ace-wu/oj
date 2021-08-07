from typing import List
from collections import deque

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        result = []
        if not root:
            return result
        queue = deque([(0, root)])
        while queue:
            depth, cursor = queue.pop()
            if depth >= len(result):
                result.append([])
            result[depth].append(cursor.val)
            for child in cursor.children:
                queue.appendleft((depth + 1, child))
        return result


