class Solution:
    ## TC: O(n*log(n))
    ## SC: O(n)
    def minIncrementForUnique_sort(self, nums: list[int]) -> int:
        inc_count = 0
        next_value = 0
        for k in sorted(nums):
            if k < next_value:
                inc_count += next_value - k
                next_value += 1
            else:
                next_value = k + 1
        return inc_count
