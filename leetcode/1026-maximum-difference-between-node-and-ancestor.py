from math import inf


class Solution:
    ## TC: O(n)
    ## SC: O(n)
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def max_diff_dfs(node, min_val=inf, max_val=-inf):
            if node is None:
                return -inf
            return max(
                node.val - min_val,
                max_val - node.val,
                max_diff_dfs(node.left, min(node.val, min_val), max(node.val, max_val)),
                max_diff_dfs(node.right, min(node.val, min_val), max(node.val, max_val)),
            )
        return max_diff_dfs(root)
