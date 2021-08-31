from typing import List
from collections import defaultdict


class UnionFind:
    def __init__(self):
        self.parent = defaultdict(lambda: None)
        self.degree = defaultdict(int)

    def find(self, v):
        if self.parent[v] is None:
            return v
        self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, u, v):
        u = self.find(u)
        v = self.find(v)
        if u == v:
            return
        if self.degree[u] > self.degree[v]:
            u, v = v, u
        self.parent[u] = v
        self.degree[v] += self.degree[u]

    def get_groups(self):
        groups = defaultdict(set)
        for i in self.parent:
            groups[self.find(i)].add(i)
        return groups


class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])

        point_groups = defaultdict(list)
        for i in range(m):
            for j in range(n):
                point_groups[matrix[i][j]].append((i, j))

        output = [[0] * n for _ in range(m)]
        rank_list = [0] * (m + n)

        for value in sorted(point_groups):
            points = point_groups[value]
            uf = UnionFind()

            for i, j in points:
                uf.union(i, j + m)

            for group in uf.get_groups().values():
                rank = max(rank_list[i] for i in group) + 1
                for i in group:
                    rank_list[i] = rank

            for i, j in points:
                output[i][j] = rank_list[i]

        return output


## TC: O(mn*lg(mn))
## SC: O(mn)

s = Solution()
print(s.matrixRankTransform([
    [7,3,6],
    [1,4,5],
    [9,8,2],
]))
print(s.matrixRankTransform([
    [ 20,-21,14],
    [-19,  4,19],
    [ 22,-47,24],
    [-19,  4,19],
]))
print(s.matrixRankTransform([
    [-37,-50, -3, 44],
    [-37, 46, 13,-32],
    [ 47,-42, -3,-40],
    [-17,-22,-39, 24],
]))
print(s.matrixRankTransform([
    [7,7],
    [7,7],
]))
