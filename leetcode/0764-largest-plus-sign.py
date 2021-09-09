from typing import List
from itertools import chain


class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        nearest_mine = [[n] * n for i in range(n)]
        for x, y in mines:
            nearest_mine[x][y] = 0

        for i in range(n):
            # left
            nearest = 0
            for j in range(n):
                nearest = 0 if nearest_mine[i][j] == 0 else nearest + 1
                nearest_mine[i][j] = min(nearest_mine[i][j], nearest)
            # right
            nearest = 0
            for j in range(n-1, -1, -1):
                nearest = 0 if nearest_mine[i][j] == 0 else nearest + 1
                nearest_mine[i][j] = min(nearest_mine[i][j], nearest)
        for j in range(n):
            # up
            nearest = 0
            for i in range(n):
                nearest = 0 if nearest_mine[i][j] == 0 else nearest + 1
                nearest_mine[i][j] = min(nearest_mine[i][j], nearest)
            # down
            nearest = 0
            for i in range(n-1, -1, -1):
                nearest = 0 if nearest_mine[i][j] == 0 else nearest + 1
                nearest_mine[i][j] = min(nearest_mine[i][j], nearest)

        return max(chain(*nearest_mine))


s = Solution()
print(s.orderOfLargestPlusSign(5, [[4,2]]))
print(s.orderOfLargestPlusSign(5, [[0,1]]))
print(s.orderOfLargestPlusSign(1, [[0,0]]))
print(s.orderOfLargestPlusSign(1, []))
