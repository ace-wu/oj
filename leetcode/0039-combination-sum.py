from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        length = len(candidates)
        candidates = sorted(candidates)

        def iter_combinations(pos, remaining):
            if remaining == 0:
                yield []
                return
            if remaining < 0 or pos >= length:
                return
            value = candidates[pos]
            if value > remaining:
                return
            for comb in iter_combinations(pos, remaining - value):
                comb.append(value)
                yield comb
            yield from (comb for comb in iter_combinations(pos + 1, remaining))

        return [comb for comb in iter_combinations(0, target)]


## TC: O(t * 2^t)
## SC: O(n) extra space
##  where t = target, n = len(candidates)

s = Solution()
print(s.combinationSum([2,3,6,7], 7))
print(s.combinationSum([2,3,5], 8))
print(s.combinationSum([2], 1))
print(s.combinationSum([1], 1))
print(s.combinationSum([1], 2))
