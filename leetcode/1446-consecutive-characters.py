class Solution:
    def maxPower(self, s: str) -> int:
        def iter_powers(s):
            start_i = 0
            for i, c in enumerate(s):
                if c != s[start_i]:
                    yield i - start_i
                    start_i = i
            yield len(s) - start_i
        return max(iter_powers(s))


## TC: O(n)
## SC: O(1)
