class Solution:
    def tribonacci(self, n: int) -> int:
        t = [0, 1, 1]
        while n > 2:
            t[0], t[1], t[2] = t[1], t[2], t[0] + t[1] + t[2]
            n -= 1
        return t[n]

## TC: O(n)
## SC: O(1)
