class Solution:
    def searchInsert_bisect(self, nums: List[int], target: int) -> int:
        from bisect import bisect_left
        return bisect_left(nums, target)

    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)
        while low < high:
            mid = (low + high) // 2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid
            else:
                return mid
        return low


## TC: O(log(n))
## SC: O(1)
