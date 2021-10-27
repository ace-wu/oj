class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i, left, right = 0, 0, len(nums) - 1
        while i <= right:
            if nums[i] == 0 :
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
                i += 1
            elif nums[i] == 2:
                nums[right], nums[i] = nums[i], nums[right]
                right -= 1
            else:
                i += 1


## TC: O(n)
## SC: O(1)
