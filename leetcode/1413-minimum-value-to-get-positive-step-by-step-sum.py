class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        accum, min_start = 0, 1
        for n in nums:
            accum += n
            min_start = max(min_start, -accum+1)
        return min_start


## TC: O(n)
## SC: O(1)
