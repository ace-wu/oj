class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            mid -= mid & 1
            if nums[mid] == nums[mid+1]:
                low = mid + 2
            elif nums[mid] == nums[mid-1]:
                high = mid - 2
            else:
                return nums[mid]
        return nums[high]


## TC: O(log(n))
## SC: O(1)
