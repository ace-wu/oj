from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        if not length:
            return 0
        pairs = sorted([(h, i) for i, h in enumerate(height) if h > 0])
        if not pairs:
            return 0
        lh, li = pairs.pop()
        rh, ri = lh, li
        total = lh
        while pairs:
            h, i = pairs.pop()
            if i < li:
                total += h * (li - i)
                lh, li = h, i
            elif i > ri:
                total += h * (i - ri)
                rh, ri = h, i
            if li == 0 and ri == length - 1:
                break
        return total - sum(height)

s = Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(s.trap([4,2,0,3,2,5]))
