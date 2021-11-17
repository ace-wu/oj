from functools import cache


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        answer = 1
        for i in range(m + n - 2, max(m, n) - 1, -1):
            answer *= i
        for i in range(1, min(m, n)):
            answer //= i
        return answerclass Solution:

    def uniquePaths_dp(self, m: int, n: int) -> int:
        @cache
        def combination(cm, cn):
            if cm < 0 or cm < cn:
                return 0
            if cm < cn * 2:
                cn = cm - cn
            if cn == 0:
                return 1
            if cn == 1:
                return cm
            return combination(cm - 1, cn - 1) + combination(cm - 1, cn)
        return combination(m + n - 2, m - 1)


## TC: O(m*n)
## SC: O(m*n)
