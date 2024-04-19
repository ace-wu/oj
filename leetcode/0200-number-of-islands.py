class Solution:
    DIR = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    ## TC: O(m*n)
    ## SC: O(1) using input grid
    def numIslands(self, grid: list[list[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def mark_island(grid, i, j):
            stack = [(i, j)]
            while stack:
                k, l = stack.pop()
                grid[k][l] = '2'
                for dk, dl in self.DIR:
                    if (
                        0 <= k + dk < m
                        and 0 <= l + dl < n
                        and grid[k + dk][l + dl] == '1'
                    ):
                        stack.append((k + dk, l + dl))

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != '1':
                    continue
                count += 1
                mark_island(grid, i, j)
        return count
