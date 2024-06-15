import collections

class UnionFind:
    def __init__(self):
        self.parent = collections.defaultdict(lambda: None)
        self.rank = collections.defaultdict(int)
        self.largest = collections.defaultdict(lambda: None)
    
    def find(self, x: int) -> int:
        if self.parent[x] is None:
            return x
        # pass compression
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> int:
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return x
        # union by rank
        if self.rank[x] < self.rank[y]:
            x, y = y, x
        self.largest[x] = max(self.find_largest(x), self.find_largest(y))
        self.parent[y] = x
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1
        return x

    def find_largest(self, x: int) -> int:
        x = self.find(x)
        if self.largest[x] is None:
            self.largest[x] = x
        return self.largest[x]


class Solution:
    ## TC: O(n * alpha(n))
    ## SC: O(n)
    def minIncrementForUnique_unionfind(self, nums: list[int]) -> int:
        uf = UnionFind()
        total_inc = 0
        seen = set()
        for k in nums:
            if k in seen:
                next_unseen = uf.find_largest(k) + 1
                total_inc += next_unseen - k
                k = next_unseen
            seen.add(k)
            if k - 1 in seen:
                uf.union(k, k - 1)
            if k + 1 in seen:
                uf.union(k, k + 1)
        return total_inc

    ## TC: O(n*log(n))
    ## SC: O(n)
    def minIncrementForUnique_sort(self, nums: list[int]) -> int:
        inc_count = 0
        next_value = 0
        for k in sorted(nums):
            if k < next_value:
                inc_count += next_value - k
                next_value += 1
            else:
                next_value = k + 1
        return inc_count
