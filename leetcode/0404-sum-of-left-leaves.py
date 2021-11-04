class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        total = 0
        stack = [(root, False)]
        while stack:
            node, is_left = stack.pop()
            if node.left is None and node.right is None and is_left:
                total += node.val
            if node.left:
                stack.append((node.left, True))
            if node.right:
                stack.append((node.right, False))
        return total


## TC: O(n)
## SC: O(n)
