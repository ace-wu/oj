class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        subsets = [[n] for n in nums]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(subsets[i]) < len(subsets[j]) + 1:
                    subsets[i] = subsets[j] + [nums[i]]
        return max(subsets, key=len)