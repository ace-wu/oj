from typing import List

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        max_length = 1
        for i in range(len(nums)):
            length = 0
            while nums[i] != i:
                next_i = nums[i]
                nums[i] = i
                i = next_i
                length += 1
            max_length = max(max_length, length)
        return max_length


## TC: O(n)
## SC: O(1)

s = Solution()
print(s.arrayNesting([5,4,0,3,1,6,2]))
print(s.arrayNesting([0,1,2,3,4,5,6]))
print(s.arrayNesting([1,2,3,4,5,6,0]))
print(s.arrayNesting([]))
