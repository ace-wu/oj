class Solution:
    def climbStairs(self, n: int) -> int:
        step = [1, 1]
        for i in range(2, n + 1):
            step[i&1] = step[0] + step[1]
        return step[n&1]


## TC: O(n)
## SC: O(1)
