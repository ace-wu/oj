class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def iter_permutations(nums, k):
            if k >= len(nums):
                yield []
            for i in range(k, len(nums)):
                nums[k], nums[i] = nums[i], nums[k]
                for p in iter_permutations(nums, k + 1):
                    p.append(nums[k])
                    yield p
                nums[k], nums[i] = nums[i], nums[k]
        return list(iter_permutations(nums, 0))


## TC: O(n*n!)
## SC: O(n*n!)
