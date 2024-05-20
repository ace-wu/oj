# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    ## TC: O(n)
    ## SC: O(n)
    def distributeCoins(self, root: TreeNode | None) -> int:
        def count_moves(
            node: TreeNode | None,
        ) -> tuple[int, int]:  # diff, moves
            if node is None:
                return 0, 0
            l_diff, l_moves = count_moves(node.left)
            r_diff, r_moves = count_moves(node.right)
            diff = node.val - 1 + l_diff + r_diff
            moves = l_moves + r_moves + abs(diff)
            return diff, moves

        return count_moves(root)[1]
