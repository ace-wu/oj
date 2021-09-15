from typing import List


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        odd_len, even_len, max_len = 1, 1, 1
        for i in range(1, len(arr)):
            prev, curr = arr[i], arr[i - 1]
            is_even = i % 2 == 0
            is_even_turb = (is_even and prev < curr) or (not is_even and prev > curr)
            is_odd_turb = (not is_even and prev < curr) or (is_even and prev > curr)
            even_len = even_len + 1 if is_even_turb else 1
            odd_len = odd_len + 1 if is_odd_turb else 1
            max_len = max(max_len, even_len, odd_len)
        return max_len


## TC: O(n)
## TC: O(1)

s = Solution()
print(s.maxTurbulenceSize([9,4,2,10,7,8,8,1,9]))
