class Solution:
    ## TC: O(n)
    ## SC: O(n)
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def sum_numbers(node, num):
            if node is None:
                return 0
            num = num * 2 + node.val
            if node.left or node.right:
                return sum_numbers(node.left, num) + sum_numbers(node.right, num)
            return num
        return sum_numbers(root, 0)
