class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # parity check & find start point & find total length
        parity_count = [0, 0]
        parity_start = None
        parity_end = None
        start_pos = None
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    parity_count[(i^j) & 1] += 1
                elif grid[i][j] == 1:
                    parity_start = (i^j) & 1
                    start_pos = i, j
                elif grid[i][j] == 2:
                    parity_end = (i^j) & 1
        if parity_start is None or parity_end is None:
            return 0
        if parity_count[0] == parity_count[1]:
            if parity_start == parity_end:
                return 0
        elif parity_count[0] == parity_count[1] + 1:
            if parity_start != 1 or parity_end != 1:
                return 0
        elif parity_count[0] + 1 == parity_count[1]:
            if parity_start != 0 or parity_end != 0:
                return 0
        else:
            return 0

        total_length = sum(parity_count)

        # backtracking
        def unique_path(x, y, length=0):
            path_count = 0
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if 0 <= x+dx < m and 0 <= y+dy < n:
                    if grid[x+dx][y+dy] == 0:
                        grid[x][y] = -1
                        path_count += unique_path(x+dx, y+dy, length+1)
                        grid[x][y] = 0
                    elif grid[x+dx][y+dy] == 2 and length == total_length:
                        path_count =+ 1
            return path_count

        return unique_path(*start_pos)


## TC: O(3*(m*n))
## SC: O(m*n)
