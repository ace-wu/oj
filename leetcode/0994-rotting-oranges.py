from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        queue = deque()
        fresh_count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.appendleft((i, j, 0))
                elif grid[i][j] == 1:
                    fresh_count += 1
        rotten_mins = 0
        while queue:
            i, j, mins = queue.pop()
            rotten_mins = max(rotten_mins, mins)
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if 0 <= i + di < m and 0 <= j + dj < n and grid[i + di][j + dj] == 1:
                    queue.appendleft((i + di, j + dj, mins + 1))
                    grid[i + di][j + dj] = 2
                    fresh_count -= 1
        if fresh_count:
            return -1
        return rotten_mins


## TC: O(n)
## SC: O(n)
