from collections import deque, defaultdict


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        def bfs(node, length=0):
            prev = [None] * n
            prev[node] = -1
            queue = deque([(node, length)])
            while queue:
                node, length = queue.popleft()
                for neighbor in adj_list[node]:
                    if prev[neighbor] is None:
                        prev[neighbor] = node
                        queue.append((neighbor, length + 1))
            return node, length, prev

        def iter_path(start, end, prev):
            length = 0
            while start != -1:
                yield start, length
                start = prev[start]
                length += 1

        start, length, prev = bfs(0)
        end, length, prev = bfs(start)
        mid_length = set([length // 2, (length + 1) // 2])
        return [node for node, length in iter_path(end, start, prev) if length in mid_length]


## TC: O(n)
## SC: O(n)
