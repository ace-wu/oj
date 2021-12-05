class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def max_money(root):
            if root is None:
                return (0, 0)
            rob_left, skip_left = max_money(root.left)
            rob_right, skip_right = max_money(root.right)
            return (root.val + skip_left + skip_right, max(rob_left, skip_left) + max(rob_right, skip_right))
        return max(*max_money(root))


## TC: O(n)
## SC: O(n)
