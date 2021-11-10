from functools import cache


class Solution:
    def numTrees(self, n: int) -> int:
        @cache
        def catalan(n):
            return 1 if (n <= 1) else sum(catalan(i) * catalan(n-i-1) for i in range(n))
        return catalan(n)


## TC: O(n^2)
## SC: O(n)
