class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total = 0
        stack = [(root, 0)]
        while stack:
            node, value = stack.pop()
            value = value * 10 + node.val
            if node.left is None and node.right is None:
                total += value
                continue
            if node.left:
                stack.append((node.left, value))
            if node.right:
                stack.append((node.right, value))
        return total


## TC: O(n)
## SC: O(n)
