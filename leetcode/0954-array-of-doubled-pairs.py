from typing import List
from collections import defaultdict

class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        return self.canReorderDoubledAux([n for n in arr if n >= 0]) and self.canReorderDoubledAux([-n for n in arr if n < 0])

    def canReorderDoubledAux(self, arr):
        counter = defaultdict(int)
        for n in sorted(arr):
            if counter.get(n/2, 0):
                counter[n/2] -= 1
            else:
                counter[n] += 1
        return all(v == 0 for v in counter.values())


s = Solution()
print(s.canReorderDoubled([1,2,2,4,4]))
print(s.canReorderDoubled([2,2,4,4]))
print(s.canReorderDoubled([2,-2,-4,4]))
print(s.canReorderDoubled([1,2,2,4,4,8]))
print(s.canReorderDoubled([]))
