class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        free, hold = 0, float('-inf')
        for price in prices:
            hold = max(hold, free - price)
            free = max(free, hold + price)
        return free


## TC: O(n)
## SC: O(1)
