from typing import List
from collections import Counter

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        counter = list(Counter(nums).items())
        return [comb for comb in self.iter_subsets(counter)]

    def iter_subsets(self, counter, curr = 0) -> List[int]:
        if curr >= len(counter):
            yield []
            return
        num, count = counter[curr]
        for comb in self.iter_subsets(counter, curr + 1):
            for i in range(count + 1):
                yield [num] * i + comb

s = Solution()
print(s.subsetsWithDup([1,2,2]))
print(s.subsetsWithDup([0]))
print(s.subsetsWithDup([]))
print(s.subsetsWithDup([1,1,1,2,2,3,3,3,3,4,4]))
