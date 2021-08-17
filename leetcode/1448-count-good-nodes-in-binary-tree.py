class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        counter = 0
        stack = [(root, root.val)]
        while stack:
            cursor, max_value = stack.pop()
            if cursor.val >= max_value:
                counter += 1
                max_value = cursor.val
            if cursor.left:
                stack.append((cursor.left, max_value))
            if cursor.right:
                stack.append((cursor.right, max_value))
        return counter


## TC: O(n)
## SC: O(n)

tree = (
    TreeNode(3,
        TreeNode(1,
            TreeNode(3),
        ),
        TreeNode(4,
            TreeNode(1),
            TreeNode(5),
        ),
    )
)
s = Solution()
print(s.goodNodes(tree))
