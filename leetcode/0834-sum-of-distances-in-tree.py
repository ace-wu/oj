from typing import List
from collections import defaultdict
from functools import lru_cache


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        adjacency_map = defaultdict(list)
        for u, v in edges:
            adjacency_map[u].append(v)
            adjacency_map[v].append(u)

        @lru_cache(None)
        def get_size(u, v):
            return 1 + sum(get_size(v, child) for child in adjacency_map[v] if child != u)

        @lru_cache(None)
        def get_dist_sum(u, v):
            return 1 + sum(get_dist_sum(v, child) + get_size(v, child) for child in adjacency_map[v] if child != u)

        return [sum(get_dist_sum(v, child) for child in adjacency_map[v]) for v in range(n)]


## TC: O(n)
## SC: O(n)

s = Solution()
print(s.sumOfDistancesInTree(6, [[0,1],[0,2],[2,3],[2,4],[2,5]]))
print(s.sumOfDistancesInTree(1, []))
print(s.sumOfDistancesInTree(2, [[1,0]]))
