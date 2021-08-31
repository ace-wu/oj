from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]
        l = 0
        r = len(nums) - 1
        while l < r - 1:
            m = (l + r) // 2
            if nums[m] < nums[r]:
                r = m
            else: # nums[m] > nums[l]:
                l = m
        return nums[r]


## TC: O(log(n))
## SC: O(1)

s = Solution()
print(s.findMin([4]))
print(s.findMin([0,1,2,3]))
print(s.findMin([4,5,6,7,0,1,2]))
