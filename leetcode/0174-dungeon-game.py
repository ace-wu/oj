from typing import List
from functools import lru_cache


class Solution:
    def calculateMinimumHP_inplace_dp(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m-1:
                    if j == n-1:
                        prev_min = 1
                    else:
                        prev_min = dungeon[i][j+1]
                else:
                    if j == n-1:
                        prev_min = dungeon[i+1][j]
                    else:
                        prev_min = min(dungeon[i][j+1], dungeon[i+1][j])
                dungeon[i][j] = max(1, prev_min - dungeon[i][j])
        return dungeon[0][0]

    def calculateMinimumHP_top_down(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])
        inf = float('inf')

        @lru_cache(None)
        def min_hp(i, j):
            if i + j  == m + n - 1:
                return 1
            if i == m or j == n:
                return inf
            return max(1, min(min_hp(i+1, j), min_hp(i, j+1)) - dungeon[i][j])

        return min_hp(0, 0)


## TC: O(m*n)
## SC: O(m*n) can be reduce to O(min(m, n)) or inplace

s = Solution()
print(s.calculateMinimumHP([[0,0]]))
print(s.calculateMinimumHP([[100]]))
print(s.calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]]))
