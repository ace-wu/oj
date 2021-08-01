from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        if not length:
            return 0
        lh, rh = [0] * length, [0] * length
        lh[0] = height[0]
        rh[-1] = height[-1]
        for i in range(1, length):
            lh[i] = max(lh[i-1], height[i])
            rh[length-i-1] = max(rh[length-i], height[length-i-1])
        return sum(min(lh[i], rh[i]) for i in range(length)) - sum(height)


s = Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(s.trap([4,2,0,3,2,5]))
