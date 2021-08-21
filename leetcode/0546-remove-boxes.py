from typing import List
from functools import lru_cache

class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        @lru_cache(None)
        def max_score(left, right, selected_size):
            if left > right:
                return 0
            selected_value = boxes[left]
            selected_size += 1
            left += 1
            while left < right and boxes[left] == selected_value:
                left += 1
                selected_size += 1
            score = selected_size**2 + max_score(left, right, 0)
            for i in range(left, right+1):
                if boxes[i] == selected_value:
                    score = max(score, max_score(left, i-1, 0) + max_score(i, right, selected_size))
            return score

        return max_score(0, len(boxes)-1, 0)



## TC: O(n^4)
## SC: O(n^3)

s = Solution()
print(s.removeBoxes([1]))
print(s.removeBoxes([1,1,1]))
print(s.removeBoxes([1,3,2,2,2,3,4,3,1]))
print(s.removeBoxes([8,1,2,10,8,5,1,10,8,4]))
print(s.removeBoxes([1,2,2,1,1,1,2,1,1,2,1,2,1,1,2,2,1,1,2,2,1,1,1,2,2,2,2,1,2,1,1,2,2,1,2,1,2,2,2,2,2,1,2,1,2,2,1,1,1,2,2,1,2,1,2,2,1,2,1,1,1,2,2,2,2,2,1,2,2,2,2,2,1,1,1,1,1,2,2,2,2,2,1,1,1,1,2,2,1,1,1,1,1,1,1,2,1,2,2,1]))

