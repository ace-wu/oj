class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        def iter_path(path_):
            node = path_[-1]
            if node == n - 1:
                yield path_[:]
                return
            for neighbor in graph[node]:
                path_.append(neighbor)
                yield from iter_path(path_)
                path_.pop()
        return list(iter_path([0]))


## TC: O((n-1)!)
## SC: O(n!) output space, O(n) extra space
