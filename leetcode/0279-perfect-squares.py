from math import isqrt


class Solution:
    def numSquares(self, n: int) -> int:
        answer = [0, 1]
        for i in range(2, n + 1):
            answer.append(1 + min(answer[-k*k] for k in range(1, isqrt(i) + 1)))
        return answer[-1]


## TC: O(n^1.5)
## SC: O(n)
