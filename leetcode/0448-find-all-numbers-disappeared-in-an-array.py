class Solution:

    def findDisappearedNumbers_swap_to_pos(self, nums: List[int]) -> List[int]:
        length = len(nums)
        for i in range(1, length+1):
            k, nums[i-1] = nums[i-1], None
            while not (k is None or nums[k-1] == k):
                t = k
                k = nums[t-1]
                nums[t-1] = t
        return [i for i in range(1, length+1) if nums[i-1] != i]

    def findDisappearedNumbers_negative(self, nums: List[int]) -> List[int]:
        length = len(nums)
        for n in nums:
            n = n if n >= 0 else -n
            if nums[n-1] >= 0:
                nums[n-1] = -nums[n-1]
        return [i+1 for i in range(length) if nums[i] > 0]


## TC: O(n)
## SC: O(1) for extra usage, O(n) for output array
