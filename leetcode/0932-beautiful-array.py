from typing import List

class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        nums = [1]
        while len(nums) < n:
            nums = [i * 2 - 1 for i in nums] + [i * 2 for i in nums]
        return [i for i in nums if i <= n]

    def check(self, nums):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(i + 1, j):
                    if nums[k] * 2 == nums[i] + nums[j]:
                        print(f'{i}:{nums[i]} {j}:{nums[k]} {k}:{nums[j]}')
                        return False
        return True

s = Solution()
i = 1000
nums = s.beautifulArray(i)
print(nums)
#is_beautiful = s.check(nums)
#if not is_beautiful:
    #print(f'{i}, {is_beautiful}')
