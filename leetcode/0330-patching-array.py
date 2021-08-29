from typing import List

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patch_count = 0
        current_n = 0

        for num in nums:
            while current_n + 1 < num:
                if current_n >= n:
                    return patch_count
                patch_count += 1
                current_n += current_n + 1
            current_n += num

        while current_n < n:
            patch_count += 1
            current_n += current_n + 1

        return patch_count

## TC: O(len(nums) + log(n))
## SC: O(1)

s = Solution()
print(s.minPatches([1,3], 6))
print(s.minPatches([1,5,10], 20))
print(s.minPatches([1,2,2], 5))
print(s.minPatches([], 1000000))
print(s.minPatches([1,2,2,6,34,38,41,44,47,47,56,59,62,73,77,83,87,89,94], 20))
