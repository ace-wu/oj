class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        max_square = 0
        local = [[0] * n, [0] * n]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    local[i&1][j] = int(matrix[i][j] == '1')
                elif matrix[i][j] == '1':
                    local[i&1][j] = 1 + min(local[(i-1)&1][j-1], local[(i-1)&1][j], local[i&1][j-1])
                else:
                    local[i&1][j] = 0
            max_square = max(max_square, max(local[i&1]))
        return max_square**2


## TC: O(m*n)
## SC: O(n)
