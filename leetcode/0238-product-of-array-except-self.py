class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        def product(start, end):
            result = 1
            for i in range(start, end):
                result *= nums[i]
            return result
        if 0 in nums:
            i = nums.index(0)
            answer = [0] * len(nums)
            answer[i] = product(0, i) * product(i + 1, len(nums))
            return answer
        prod = product(0, len(nums))
        return [prod // n for n in nums]


## TC: O(n)
## SC: O(1)
