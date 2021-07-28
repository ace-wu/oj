# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.create_bst(nums, 0, len(nums))

    def create_bst(self, nums: List[int], left: int, right: int) -> TreeNode:
        if left >= right:
            return None
        mid = left + (right - left) // 2
        return TreeNode(
            nums[mid],
            self.create_bst(nums, left, mid),
            self.create_bst(nums, mid + 1, right),
        )
