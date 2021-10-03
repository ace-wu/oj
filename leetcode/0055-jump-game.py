from typing import List
from functools import lru_cache


class Solution:
    def canJump_top_down(self, nums: List[int]) -> bool:
        n = len(nums)
        @lru_cache(None)
        def can_jump(i):
            if i < 0 or i >= n:
                return False
            if i + nums[i] >= n - 1:
                return True
            return any(can_jump(k) for k in range(i + nums[i], i, -1))
        return can_jump(0)

    def canJump_greedy(self, nums: List[int]) -> bool:
        n = len(nums)
        max_jump = 0
        for i in range(n):
            if max_jump < i:
                return False
            max_jump = max(max_jump, i + nums[i])
            if max_jump >= n - 1:
                return True
        return max_jump >= n - 1


## TC: O(n)
## SC: O(1)

s = Solution()
print(s.canJump([0]))
print(s.canJump([3,2,1,0,4]))
