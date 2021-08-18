class Solution:
    def numDecodings(self, s: str) -> int:
        codes = set(str(i) for i in range(1, 27))
        if s[0] not in codes:
            return 0
        c2, c1, c = 1, 1, 0
        for i in range(1, len(s)):
            if s[i:i+1] in codes:
                c += c1
            if s[i-1:i+1] in codes:
                c += c2
            c2, c1, c = c1, c, 0
        return c1


## TC: O(n)
## SC: O(1)

s = Solution()
print(s.numDecodings('12'))
print(s.numDecodings('27'))
print(s.numDecodings('226'))
print(s.numDecodings('22222'))
print(s.numDecodings('0123'))

