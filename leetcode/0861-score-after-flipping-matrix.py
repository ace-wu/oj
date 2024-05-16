class Solution:
    ## TC: O(m * n)
    ## SC: O(1), modifying input grid
    def matrixScore(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        for row in grid:
            if row[0] == 0:
                for j in range(n):
                    row[j] = 0 if row[j] else 1
        pow2 = 1 << (n - 1)
        total = 0
        for j in range(n):
            bits = sum(grid[i][j] for i in range(m))
            bits = max(bits, m - bits)
            total += bits * pow2
            pow2 >>= 1
        return total
