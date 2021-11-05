from math import isqrt


class Solution:
    def arrangeCoins(self, n: int) -> int:
        k = isqrt(n * 2) - 1
        n -= k * (k + 1) // 2
        while n >= k + 1:
            k += 1
            n -= k
        return k