from functools import cache


class Solution:
    def maxProfit_top_down_dp(self, prices: List[int]) -> int:
        FREE, HOLD, CD = 1, 2, 3
        @cache
        def max_profit(i, status):
            if i <= 0:
                return 0 if status == FREE else float('-inf')
            if status == FREE:
                return max(max_profit(i-1, FREE), max_profit(i-1, CD))
            if status == HOLD:
                return max(max_profit(i-1, HOLD), max_profit(i-1, FREE) - prices[i-1])
            if status == CD:
                return max_profit(i-1, HOLD) + prices[i-1]
        n = len(prices)
        return max_profit(n+1, FREE)

    def maxProfit_bottom_up_dp(self, prices: List[int]) -> int:
        inf = float('inf')
        free, hold, cd = 0, -inf, -inf
        for price in prices:
            free, hold, cd = max(free, cd), max(hold, free - price), hold + price
        return max(free, cd)


## TC: O(n)
## SC: O(1)
