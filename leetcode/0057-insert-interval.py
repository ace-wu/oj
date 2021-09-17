class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_l, new_r = newInterval
        lhs, rhs = [], []
        for l, r in intervals:
            if r < new_l:
                lhs.append([l, r])
            elif new_r < l:
                rhs.append([l, r])
            else:
                new_l = min(new_l, l)
                new_r = max(new_r, r)
        return lhs + [[new_l, new_r]] + rhs


## TC: O(n)
## SC: O(n)
