from typing import List
import collections


class Solution:
    ## TC: O(n)
    ## SC: O(n)
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        adj_list = collections.defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        size = [0] * n  # rooted

        def create_size(parent, v):
            size[v] = 1 + sum(create_size(v, w) for w in adj_list[v] if w != parent)
            return size[v]

        def get_dist(parent, v):
            return sum(size[w] + get_dist(v, w) for w in adj_list[v] if w != parent)

        udist = [0] * n  # unrooted

        def create_udist(parent, v):
            for w in adj_list[v]:
                if w != parent:
                    udist[w] = udist[v] - size[w] + (n - size[w])
                    create_udist(v, w)

        create_size(-1, 0)
        udist[0] = get_dist(-1, 0)
        create_udist(-1, 0)

        return udist


s = Solution()
print(s.sumOfDistancesInTree(6, [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]))
print(s.sumOfDistancesInTree(1, []))
print(s.sumOfDistancesInTree(2, [[1, 0]]))
print(s.sumOfDistancesInTree(30000, [[0, i] for i in range(1, 30000)]))
