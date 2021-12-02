class Solution:
    def rob(self, nums: List[int]) -> int:
        h2, h1, h0 = 0, 0, 0
        for n in nums:
            h2, h1, h0 = h1, h0, n + max(h1, h2)
        return max(h1, h2)


## TC: O(n)
## SC: O(1)
