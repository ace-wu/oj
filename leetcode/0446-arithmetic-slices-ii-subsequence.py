from typing import List
from collections import defaultdict


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        diff_table = defaultdict(int)
        total = 0
        for curr in range(1, len(nums)):
            for prev in range(curr):
                diff = nums[curr] - nums[prev]
                count = diff_table[(prev, diff)] if (prev, diff) in diff_table else 0
                diff_table[(curr, diff)] += count + 1
                total += count
        return total


## TC: O(n^2)
## SC: O(n^2)

s = Solution()
print(s.numberOfArithmeticSlices([2,4,6,8,10]))
print(s.numberOfArithmeticSlices([7,7,7,7,7]))
