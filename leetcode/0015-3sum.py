from collections import Counter


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def iter_triple():
            counter = Counter(nums)
            # (x, x, x)
            if counter.get(0, 0) >= 3:
                yield 0, 0, 0
            # (x, x, y) where x != y
            for x, count in counter.items():
                if x and count >= 2 and -2 * x in counter:
                    yield x, x, -2 * x
            # (x, y, z) where x < y < z
            for x in counter:
                for y in counter:
                    z = -(x + y)
                    if x < y < z and z in counter:
                        yield x, y, z
        return list(iter_triple())


# TC: O(n^2)
# SC: O(n)
