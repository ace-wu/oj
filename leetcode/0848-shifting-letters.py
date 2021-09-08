from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        offset = ord('a')
        accum_shift = 0
        reversed_result = []
        for c, shift in zip(reversed(s), reversed(shifts)):
            accum_shift += shift
            reversed_result.append(chr((ord(c) - offset + accum_shift) % 26 + offset))
        return ''.join(reversed(reversed_result))


## TC: O(n)
## SC: O(n) output space, O(1) extra space

s = Solution()
print(s.shiftingLetters('abc', [3,5,9]))
