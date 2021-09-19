from functools import lru_cache


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)
        if m < n:
            return 0
        if m == n:
            return 1 if s == t else 0
        seq_count = [1] + [0] * n
        for si in range(1, m+1):
            for ti in range(min(n, si), 0, -1):
                seq_count[ti] += seq_count[ti-1] if s[si - 1] == t[ti - 1] else 0
        return seq_count[-1]

    def numDistinct_top_down(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)
        if m < n:
            return 0
        if m == n:
            return 1 if s == t else 0

        @lru_cache(None)
        def seq_count(si, ti):
            if si == ti == 0:
                return 1
            if si < 0 or ti < 0 or si < ti:
                return 0
            result = seq_count(si - 1, ti)
            if s[si - 1] == t[ti - 1]:
                result += seq_count(si - 1, ti - 1)
            return result

        return seq_count(m, n)


## TC: O(m*n)
## SC: O(n)

s = Solution()
print(s.numDistinct('rabbbit', 'rabbit'))
print(s.numDistinct('babgbag', 'bag'))
