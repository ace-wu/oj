class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def get_depth_diameter(node):
            if node is None:
                return -1, 0
            l_depth, l_diameter = get_depth_diameter(node.left)
            r_depth, r_diameter = get_depth_diameter(node.right)
            depth = max(l_depth, r_depth) + 1
            diameter = max(l_diameter, r_diameter, l_depth + r_depth + 2)
            return depth, diameter
        return get_depth_diameter(root)[1]


## TC: O(n)
## SC: O(n)
