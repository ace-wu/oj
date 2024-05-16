class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # TC: O(n), SC: O(height of the tree)
    def evaluateTree(self, root: TreeNode) -> bool:
        def eval_tree(node) -> bool:
            if node.val == 0:
                return False
            elif node.val == 1:
                return True
            elif node.val == 2:
                return eval_tree(node.left) or eval_tree(node.right)
            else:  # node.val == 3
                return eval_tree(node.left) and eval_tree(node.right)

        return eval_tree(root)
