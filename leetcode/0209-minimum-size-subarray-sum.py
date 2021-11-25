class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start, end = 0, 0
        total = 0
        while end < len(nums):
            if total >= target:
                break
            total += nums[end]
            end += 1
        if total < target:
            return 0
        min_size = end - start
        while end <= len(nums):
            if total >= target:
                min_size = min(min_size, end - start)
                total -= nums[start]
                start += 1
            elif end < len(nums):
                total += nums[end]
                end += 1
            else:
                break
        return min_size


## TC: O(n)
## SC: O(1)
