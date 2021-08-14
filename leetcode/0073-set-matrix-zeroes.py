from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        zero_rows = set()
        zero_cols = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)
        for i in zero_rows:
            for j in range(n):
                matrix[i][j] = 0
        for j in zero_cols:
            for i in range(m):
                matrix[i][j] = 0


s = Solution()
s.setZeroes([
    [0,1,2,0],
    [3,4,5,2],
    [1,3,1,5],
])

s.setZeroes([
    [1,1,2,1],
    [3,4,5,2],
    [1,3,1,5],
])

s.setZeroes([
    [1,1,2,1],
    [3,0,0,2],
    [1,3,0,5],
])

s.setZeroes([
    [1],
])
