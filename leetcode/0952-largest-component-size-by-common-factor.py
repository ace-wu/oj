from collections import defaultdict, Counter


class UnionFind:
    def __init__(self):
        self.parent = defaultdict(lambda: None)
        self.size = defaultdict(lambda: 1)

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.size[x] > self.size[y]:
            x, y = y, x
        self.parent[x] = y
        self.size[y] += self.size[x]
        self.size[x] = 0

    def find(self, x):
        if self.parent[x] is None:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]


class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        uf = UnionFind()
        for n in nums:
            factor = 2
            comp = n
            while comp >= factor * factor:
                if comp % factor == 0:
                    uf.union(n, factor)
                    while comp % factor == 0:
                        comp //= factor
                factor += 2 if factor != 2 else 1
            if comp > 1:
                uf.union(n, comp)
        return max(Counter(uf.find(n) for n in nums).values())


## TC: O(n*sqrt(m))
## SC: O(n+log(m))
## where n = len(nums), m = max(nums)
