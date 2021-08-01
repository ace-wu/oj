from typing import List

class Solution:
    neighbor = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def find_size_and_bridges(self, grid, island_id, x, y, n):
        stack = [(x, y)]
        bridge_set = set()
        size = 0
        while stack:
            i, j = stack.pop()
            if not (0 <= i < n) or not (0 <= j < n):
                continue
            elif grid[i][j] == 1:
                size += 1
                grid[i][j] = island_id
                for di, dj in self.neighbor:
                    stack.append((i+di, j+dj))
            elif grid[i][j] == 0:
                opps_set = set()
                for di, dj in self.neighbor:
                    if not (0 <= i+di < n) or not (0 <= j+dj < n):
                        continue
                    opps_id = grid[i+di][j+dj]
                    if opps_id > 1 and opps_id < island_id:
                        opps_set.add(opps_id)
                if opps_set:
                    opps_set.add(island_id)
                    bridge_set.add(tuple(sorted(opps_set)))
        return size, bridge_set

    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        bridge_set = set()
        size_map = {}
        island_id = 2
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    size_map[island_id], bridges = self.find_size_and_bridges(grid, island_id, i, j, n)
                    bridge_set.update(bridges)
                    island_id += 1
        if bridge_set:
            return max(sum(size_map[id] for id in id_set) for id_set in bridge_set) + 1
        elif size_map:
            return min(max(size_map.values()) + 1, n * n)
        else:
            return 1


s = Solution()
print(s.largestIsland([[1,0],[0,1]]))
print(s.largestIsland([[1,1],[1,0]]))
print(s.largestIsland([[1,1],[1,1]]))
print(s.largestIsland([[0,0],[0,0]]))
print(s.largestIsland([
    [0,0,0,0,0,0,0],
    [0,1,1,1,1,0,0],
    [0,1,0,0,1,0,0],
    [1,0,1,0,1,0,0],
    [0,1,0,0,1,0,0],
    [0,1,0,0,1,0,0],
    [0,1,1,1,1,0,0],
]))
