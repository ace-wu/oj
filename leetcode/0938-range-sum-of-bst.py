class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def iter_values(root):
            if root:
                yield root.val
                yield from iter_values(root.left)
                yield from iter_values(root.right)
        return sum(v for v in iter_values(root) if low <= v <= high)


## TC: O(n)
## SC: O(n)
