from functools import cache


class Solution:
    def maxProfit_top_down_dp(self, prices: List[int]) -> int:
        inf = float('inf')
        FREE, HOLD = 0, 1
        @cache
        def max_profit(i, status, transactions):
            if transactions < 0:
                return -inf
            if i <= 0:
                return 0 if status == FREE and transactions == 0 else -inf
            if status == FREE:
                return max(
                    max_profit(i-1, FREE, transactions),
                    max_profit(i-1, HOLD, transactions-1) + prices[i-1],
                )
            if status == HOLD:
                return max(
                    max_profit(i-1, HOLD, transactions),
                    max_profit(i-1, FREE, transactions) - prices[i-1],
                )
        n = len(prices)
        return max(max_profit(n, FREE, trans) for trans in range(3))

    def maxProfit_bottom_up_dp(self, prices: List[int]) -> int:
        inf = float('inf')
        free0, free1, free2, hold0, hold1 = 0, -inf, -inf, -inf, -inf
        for price in prices:
            free2 = max(free2, hold1 + price)
            hold1 = max(hold1, free1 - price)
            free1 = max(free1, hold0 + price)
            hold0 = max(hold0, free0 - price)
        return max(free2, free1, free0)


## TC: O(n)
## SC: O(1)
