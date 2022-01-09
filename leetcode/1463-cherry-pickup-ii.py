from math import inf


class Solution:
    # top-down, search from the last row
    ## TC: O(rows*cols^2)
    ## SC: O(rows*cols^2)
    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        @cache
        def cherry_pickup(c1, c2, r):
            cherries = grid[r][c1] + grid[r][c2] if c1 != c2 else grid[r][c1]
            if r == 0:
                return cherries if c1 == 0 and c2 == cols - 1 else -inf
            return cherries + max(cherry_pickup(prev_c1, prev_c2, r - 1)
                for prev_c1 in range(max(c1 - 1, 0), min(c1 + 2, cols))
                for prev_c2 in range(max(c2 - 1, 0), min(c2 + 2, cols))
            )
        return max(cherry_pickup(c1, c2, rows - 1) for c1 in range(cols) for c2 in range(cols))

    # top-down, search from the first row
    ## TC: O(rows*cols^2)
    ## SC: O(rows*cols^2)
    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        @cache
        def cherry_pickup(c1, c2, r):
            if r >= rows:
                return 0
            cherries = grid[r][c1] + grid[r][c2] if c1 != c2 else grid[r][c1]
            return cherries + max(cherry_pickup(next_c1, next_c2, r + 1)
                for next_c1 in range(max(c1 - 1, 0), min(c1 + 2, cols))
                for next_c2 in range(max(c2 - 1, 0), min(c2 + 2, cols))
            )
        return cherry_pickup(0, cols - 1, 0)
