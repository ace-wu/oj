class Solution:
    def countNodes_recursive(self, root: Optional[TreeNode]) -> int:
        def depth(root):
            depth = 0
            while root:
                root = root.left
                depth += 1
            return depth

        def count_nodes(root, root_depth):
            if not root:
                return 0
            left_depth = root_depth - 1
            right_depth = depth(root.right)
            if left_depth == right_depth:
                return 2**left_depth + count_nodes(root.right, right_depth)
            return count_nodes(root.left, left_depth) + 2**right_depth

        return count_nodes(root, depth(root))

    def countNodes_constructive(self, root: Optional[TreeNode]) -> int:
        def depth(root):
            depth = 0
            while root:
                root = root.left
                depth += 1
            return depth

        total_nodes = 0
        root_depth = depth(root)
        while root:
            left_depth = root_depth - 1
            right_depth = depth(root.right)
            if left_depth == right_depth:
                total_nodes += 2**left_depth
                root = root.right
                root_depth = right_depth
            else:
                total_nodes += 2**right_depth
                root = root.left
                root_depth = left_depth

        return total_nodes


## TC: O(log(n)^2)
## SC: O(1)
