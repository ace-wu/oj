from functools import cache


class Solution:
    # top-down DP (TLE)
    ## TC: O(n^2)
    ## SC: O(n^2)
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        @cache
        def max_coins(left, right):
            if left + 1 >= right:
                return 0
            left_right_prod = nums[left] * nums[right]
            return max(nums[mid] * left_right_prod + max_coins(left, mid) + max_coins(mid, right) for mid in range(left + 1, right))
        return max_coins(0, len(nums) - 1)

    # bottom-up DP
    ## TC: O(n^2)
    ## SC: O(n^2)
    def maxCoins(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = [1] + nums + [1]
        size = len(nums)
        table = [[0] * size for i in range(size)]

        for width in range(2, size):
            for left in range(size - width):
                right = left + width
                left_right_prod = nums[left] * nums[right]
                table[left][right] = max([nums[mid] * left_right_prod + table[left][mid] + table[mid][right] for mid in range(left + 1, right)])

        return table[0][size-1]
