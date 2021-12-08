class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        def get_sum_and_tilt(root):
            if root is None:
                return 0, 0
            left_sum, left_tilt = get_sum_and_tilt(root.left)
            right_sum, right_tilt = get_sum_and_tilt(root.right)
            total_sum = root.val + left_sum + right_sum
            total_tilt = abs(left_sum - right_sum) + left_tilt + right_tilt
            return total_sum, total_tilt
        _, tilt = get_sum_and_tilt(root)
        return tilt


## TC: O(n)
## SC: O(n)
