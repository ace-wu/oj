class Solution:
    def numTilings(self, n: int) -> int:
        t00, t01, t10, t11 = 1, 0, 0, 1
        for i in range(1, n):
            t00, t01, t10, t11 = t11 + t01 + t10 + t00, t11 + t10, t11 + t01, t00
        return t00 % (10**9 + 7)


## TC: O(n)
## SC: O(1)
