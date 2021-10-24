class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]
        l, r = 0, len(nums) - 1
        while l < r - 1:
            m = (l + r) // 2
            if nums[m] < nums[r]:
                r = m
            elif nums[l] < nums[m]:
                l = m
            elif nums[m] == nums[r]:
                r -= 1
            else: # nums[l] == nums[m]
                l += 1
        return nums[r]


## TC: O(n)
## SC: O(1)
