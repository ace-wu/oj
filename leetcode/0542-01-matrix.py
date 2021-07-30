from typing import List
from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat:
            return [[]]
        m = len(mat)
        n = len(mat[0])
        result = [[None for i in range(n)] for j in range(m)]

        queue = deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.appendleft((i, j, 0))
        while queue:
            i, j, distance = queue.pop()
            if not (0 <= i < m) or not (0 <= j < n) or result[i][j] is not None:
                continue
            result[i][j] = distance
            queue.appendleft((i - 1, j, distance + 1))
            queue.appendleft((i + 1, j, distance + 1))
            queue.appendleft((i, j - 1, distance + 1))
            queue.appendleft((i, j + 1, distance + 1))
        return result

s = Solution()
input = [
    [1, 0, 1, 1],
    [0, 1, 1, 1],
    [0, 0, 1, 1],
]
print(input)
print(s.updateMatrix(input))
