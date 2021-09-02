from pprint import pprint
from typing import List, Optional
from functools import lru_cache


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        result = f'{self.val}'
        if self.left:
            result = f'{self.left}/{result}'
        if self.right:
            result = f'{result}\{self.right}'
        if self.left or self.right:
            result = f'({result})'
        return result


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        @lru_cache(None)
        def trees(start, end):
            if start > end:
                return [None]
            return [
                TreeNode(i, lhs, rhs)
                    for i in range(start, end + 1)
                    for lhs in trees(start, i - 1)
                    for rhs in trees(i + 1, end)
            ]
        return trees(1, n)


## TC: O(n!)
## SC: O(n!)

s = Solution()
print(len(s.generateTrees(1)))
print(len(s.generateTrees(2)))
print(len(s.generateTrees(3)))
print(len(s.generateTrees(4)))
print(len(s.generateTrees(5)))

pprint(s.generateTrees(3))
pprint(s.generateTrees(4))

