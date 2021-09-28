class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i_even, i_odd = 0, 1
        while i_even < n and i_odd < n:
            while i_even < n and nums[i_even] & 1 == 0:
                i_even += 2
            while i_odd < n and nums[i_odd] & 1 == 1:
                i_odd += 2
            if not (i_even < n and i_odd < n):
                break
            nums[i_even], nums[i_odd] = nums[i_odd], nums[i_even]
        return nums


## TC: O(n)
## SC: O(1) extra space, inplace
