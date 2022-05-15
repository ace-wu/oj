class Solution:
    ## TC: O(n)
    ## SC: O(n)
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        tree = [root]
        i = 0
        while tree[i]:
            tree.append(tree[i].left)
            tree.append(tree[i].right)
            i += 1
        return not any(tree[i:])
