class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def delete(node, key):
            if node is None:
                return None
            elif key < node.val:
                node.left = delete(node.left, key)
            elif key > node.val:
                node.right = delete(node.right, key)
            else:
                if node.left is None:
                    return node.right
                if node.right is None:
                    return node.left
                right_min = node.right
                while right_min.left:
                    right_min = right_min.left
                node.val = right_min.val
                node.right = delete(node.right, right_min.val)
            return node

        return delete(root, key)


## TC: O(n)
## SC: O(1)
