from typing import Optional
from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()
        stack = [root]
        while stack:
            cursor = stack.pop()
            if k - cursor.val in seen:
                return True
            seen.add(cursor.val)
            if cursor.left is not None:
                stack.append(cursor.left)
            if cursor.right is not None:
                stack.append(cursor.right)
        return False

## TC: O(n)
## SC: O(n)
