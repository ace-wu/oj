from typing import List
from collections import deque


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m = len(grid)
        n = len(grid[0])
        seen = set()
        queue = deque([(0, 0, 0, 0)])
        while queue:
            dist, remove_count, x, y = queue.popleft()
            if (x, y, remove_count) in seen:
                continue
            seen.add((x, y, remove_count))
            if x == m-1 and y == n-1:
                return dist
            for dx, dy in d:
                if not (0 <= x+dx < m and 0 <= y+dy < n) or (x+dx, y+dy, remove_count) in seen:
                    continue
                elif grid[x+dx][y+dy] == 0:
                    queue.append((dist+1, remove_count, x+dx, y+dy))
                elif remove_count < k:
                    queue.append((dist+1, remove_count+1, x+dx, y+dy))
        return -1


## TC: O(m*n*k)
## SC: O(m*n*k)
