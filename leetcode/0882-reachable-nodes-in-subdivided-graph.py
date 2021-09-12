from typing import List
from collections import defaultdict
import heapq


class Solution:
    def reachableNodes(self, edges: List[List[int]], max_moves: int, n: int) -> int:
        adjacency_map = defaultdict(list)
        for u, v, moves in edges:
            adjacency_map[u].append((v, moves))
            adjacency_map[v].append((u, moves))

        visited = {}
        pq = [(-max_moves, 0)]
        while pq:
            remain_moves, u = heapq.heappop(pq)
            remain_moves = -remain_moves
            if u not in visited:
                visited[u] = remain_moves
                for v, moves in adjacency_map[u]:
                    if v not in visited and remain_moves >= moves + 1:
                        heapq.heappush(pq, (-(remain_moves - moves - 1), v))

        total = len(visited)
        for u, v, moves in edges:
            total += min(moves, visited.get(u, 0) + visited.get(v, 0))
        return total


## TC: O((V+E)*log(E)) -> O(E*log(E))
## SC: O(V+E) -> O(E)
## note that #visited_node <= #edges

s = Solution()
print(s.reachableNodes([[0,1,10],[0,2,1],[1,2,2]], 6, 3))
print(s.reachableNodes([[0,1,4],[1,2,6],[0,2,8],[1,3,1]], 10, 4))
print(s.reachableNodes([[1,2,4],[1,4,5],[1,3,1],[2,3,4],[3,4,5]], 17, 5))
print(s.reachableNodes([[0,3,4],[3,4,0],[1,3,0],[2,4,4],[2,3,0]], 5, 5))
