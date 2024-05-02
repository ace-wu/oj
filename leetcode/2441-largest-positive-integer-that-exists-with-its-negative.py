class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        largest = -1
        seen = set()
        for n in nums:
            if abs(n) <= largest:
                continue
            seen.add(n)
            if -n in seen:
                largest = abs(n)
        return largest
