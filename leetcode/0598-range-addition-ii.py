from typing import List

class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        return min(op[0] for op in ops) * min(op[1] for op in ops) if ops else m * n


## TC: O(m+n)
## SC: O(1)

s = Solution()
print(s.maxCount(3, 3, [[2,2],[3,3]]))
print(s.maxCount(3, 3, [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]))
print(s.maxCount(3, 3, []))
