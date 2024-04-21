import collections


class Solution:
    ## TC: O(V + E)
    ## SC: O(V + E)
    def validPath(
        self, n: int, edges: list[list[int]], source: int, destination: int
    ) -> bool:
        adj_list = collections.defaultdict(set)
        for u, v in edges:
            adj_list[u].add(v)
            adj_list[v].add(u)
        seen = set([source])
        stack = [source]
        while stack:
            v = stack.pop()
            if v == destination:
                return True
            for u in adj_list[v]:
                if u not in seen:
                    stack.append(u)
                    seen.add(u)
        return False
