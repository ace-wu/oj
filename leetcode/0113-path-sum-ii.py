class Solution:
    def iter_path(self, root, remaining, path_):
        if not root:
            return
        remaining -= root.val
        path_.append(root.val)
        if root.left or root.right:
            yield from self.iter_path(root.left, remaining, path_)
            yield from self.iter_path(root.right, remaining, path_)
        elif remaining == 0:
            yield path_.copy()
        path_.pop()

    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        return [path_ for path_ in self.iter_path(root, targetSum, [])]
