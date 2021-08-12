
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        length = len(s)
        flip_from_0 = sum([1 for c in s if c == '0'])
        flip_from_1 = 0
        min_flip = flip_from_0
        for c in s:
            if c == '1':
                flip_from_1 += 1
            else: # c == '0':
                flip_from_0 -= 1
            min_flip = min(min_flip, flip_from_0 + flip_from_1)
        return min_flip

s = Solution()
print(s.minFlipsMonoIncr('00110'))
print(s.minFlipsMonoIncr('010110'))
print(s.minFlipsMonoIncr('00011000'))
print(s.minFlipsMonoIncr('00011110'))
print(s.minFlipsMonoIncr('10011110'))
print(s.minFlipsMonoIncr('01111111'))
