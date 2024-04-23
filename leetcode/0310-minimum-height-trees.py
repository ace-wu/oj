from collections import deque, defaultdict


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        ## TC: O(n)
        ## SC: O(n)
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
        return [
            node for node, length in iter_path(end, start, prev) if length in mid_length
        ]

    def findMinHeightTrees_20240423(self, n: int, edges: List[List[int]]) -> List[int]:
        ## TC: O(n)
        ## SC: O(n)
        if n == 1:
            return [0]

        adj_list = defaultdict(set)
        for u, v in edges:
            adj_list[u].add(v)
            adj_list[v].add(u)

        leaves = set()
        for v, edges in adj_list.items():
            if len(edges) == 1:
                leaves.add(v)

        # remove leaves level by level
        while len(adj_list) > 2:
            next_level_leaves = set()
            for leaf in leaves:
                for v in adj_list[leaf]:
                    adj_list[v].remove(leaf)
                    if len(adj_list[v]) == 1:
                        next_level_leaves.add(v)
                del adj_list[leaf]
            leaves = next_level_leaves

        return leaves
