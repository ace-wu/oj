class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        in_mapping = {v: i for i, v in enumerate(inorder)}
        post_stack = postorder[:]
        def build_tree(start, end):
            if start >= end or not post_stack:
                return None
            value = post_stack.pop()
            in_i = in_mapping[value]
            node = TreeNode(value)
            node.right = build_tree(in_i + 1, end)
            node.left = build_tree(start, in_i)
            return node
        return build_tree(0, len(inorder))



## TC: O(n)
## SC: O(n)
