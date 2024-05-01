class Solution:
    # TC: O(len(nums) + log(k))
    # SC: O(1)
    def minOperations(self, nums: list[int], k: int) -> int:
        p = k
        for n in nums:
            p ^= n
        ops = 0
        while p > 0:
            ops += p & 1
            p >>= 1
        return ops
