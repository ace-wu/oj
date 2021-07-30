from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        answer_set = set()
        nums = sorted(nums)
        length = len(nums)
        for a in range(length):
            for b in range(a + 1, length):
                c = b + 1
                d = length - 1
                while c < d:
                    diff = nums[a] + nums[b] + nums[c] + nums[d] - target
                    if diff == 0:
                        answer_set.add((nums[a], nums[b], nums[c], nums[d]))
                        c += 1
                        d -= 1
                    elif diff < 0:
                        c += 1
                    else:
                        d -= 1
        return answer_set


s = Solution()
print(s.fourSum([1,0,-1,0,-2,2], 0))
print(s.fourSum([2,2,2,2,2], 8))
