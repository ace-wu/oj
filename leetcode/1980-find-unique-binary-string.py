from typing import List

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        return ''.join('1' if num[i] == '0' else '0' for i, num in enumerate(nums))


## TC: O(n)
## SC: O(n) for return string + O(1) for others

s = Solution()
print(s.findDifferentBinaryString(['01','10']))
print(s.findDifferentBinaryString(['00','01']))
print(s.findDifferentBinaryString(['111','011','001']))
