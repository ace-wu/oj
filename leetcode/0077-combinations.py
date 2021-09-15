class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def iter_combinations(n, k):
            if k == 0:
                yield []
                return
            if n < k:
                return
            if n == k:
                yield list(range(1, n + 1))
                return
            # skip #n
            yield from iter_combinations(n - 1, k)
            # choose #n
            for subset in iter_combinations(n - 1, k - 1):
                subset.append(n)
                yield subset
        return list(iter_combinations(n, k))


## TC: O(n*C(n, k))
## TC: O(n*C(n, k))
