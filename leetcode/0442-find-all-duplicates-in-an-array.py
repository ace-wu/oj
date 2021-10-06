class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dups = []
        for i in range(len(nums)):
            k, nums[i] = nums[i], 0
            while k:
                if nums[k-1] == k:
                    dups.append(k)
                    break
                nums[k-1], k = k, nums[k-1]
        return dups


## TC: O(n)
## SC: O(1)
