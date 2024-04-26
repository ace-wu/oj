class Solution:
    ## TC: O(N^2)
    ## SC: O(1)
    def minFallingPathSum(self, grid: list[list[int]]) -> int:
        if len(grid) == 1:
            return grid[0][0]
        inf = float('inf')

        min_idx = -1
        min_val = 0
        snd_min_val = 0

        for row in grid:
            next_min_idx = -1
            next_min_val = inf
            next_snd_min_val = inf

            for i in range(len(row)):
                val = row[i] + (min_val if i != min_idx else snd_min_val)
                if val < next_min_val:
                    next_snd_min_val = next_min_val
                    next_min_val = val
                    next_min_idx = i
                elif val < next_snd_min_val:
                    next_snd_min_val = val

            min_idx = next_min_idx
            min_val = next_min_val
            snd_min_val = next_snd_min_val

        return min_val
