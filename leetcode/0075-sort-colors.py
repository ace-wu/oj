class Solution:
    ## TC: O(n)
    ## SC: in-place
    def sortColors_swap(self, nums: list[int]) -> None:
        i, left, right = 0, 0, len(nums) - 1
        while i <= right:
            if nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
                i += 1
            elif nums[i] == 2:
                nums[right], nums[i] = nums[i], nums[right]
                right -= 1
            else:
                i += 1

    ## TC: O(n)
    ## SC: in-place
    def sortColors_counting(self, nums: list[int]) -> None:
        zeros, ones, n = 0, 0, len(nums)
        for i in nums:
            if i == 0:
                zeros += 1
            elif i == 1:
                ones += 1
        for i in range(zeros):
            nums[i] = 0
        for i in range(zeros, zeros + ones):
            nums[i] = 1
        for i in range(zeros + ones, n):
            nums[i] = 2
