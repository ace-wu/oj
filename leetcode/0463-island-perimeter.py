class Solution:
    ## TC: O(h*w)
    ## SC: O(1)
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        h = len(grid)
        w = len(grid[0])

        perimeter = 0
        for i in range(h):
            perimeter += grid[i][0] + grid[i][-1]
            for j in range(1, w):
                perimeter += int(grid[i][j] != grid[i][j - 1])
        for j in range(w):
            perimeter += grid[0][j] + grid[-1][j]
            for i in range(1, h):
                perimeter += int(grid[i][j] != grid[i - 1][j])
        return perimeter
