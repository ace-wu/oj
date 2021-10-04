class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        perimeter = 0

        for i in range(m):
            prev = 0
            for j in range(n):
                if prev == 0 and grid[i][j] == 1:
                    perimeter += 2
                prev = grid[i][j]

        for j in range(n):
            prev = 0
            for i in range(m):
                curr = grid[i][j]
                if prev == 0 and grid[i][j] == 1:
                    perimeter += 2
                prev = grid[i][j]

        return perimeter


## TC: O(m*n)
## SC: O(1)
