class Solution:
    ## TC: O(2^n)
    ## SC: O(n)
    def subsetXORSum_recursion(self, nums: list[int]) -> int:
        def iter_subset_xor_numbers(xor_num=0, pos=0):
            if pos >= len(nums):
                yield xor_num
            else:
                yield from iter_subset_xor_numbers(xor_num, pos + 1)
                yield from iter_subset_xor_numbers(xor_num ^ nums[pos], pos + 1)

        return sum(iter_subset_xor_numbers())

    ## TC: O(n)
    ## SC: O(1)
    def subsetXORSum(self, nums: list[int]) -> int:
        result = 0
        for i in nums:
            result |= i
        return result << (len(nums) - 1)
