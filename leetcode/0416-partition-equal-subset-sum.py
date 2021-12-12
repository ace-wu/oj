class Solution:
    def canPartition_0_1_knapsack(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        half = total // 2
        max_w = [0] * (half + 1)
        for i, n in enumerate(nums):
            for capacity in range(half, n-1, -1):
                max_w[capacity] = max(max_w[capacity], max_w[capacity - n] + n)
        return max_w[half] == half

    def canPartition_bool(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        half = total // 2
        max_w = [True] + [False] * half
        for i, n in enumerate(nums):
            for capacity in range(half, n-1, -1):
                if max_w[capacity - n]:
                    max_w[capacity] = max_w[capacity - n]
        return max_w[half]


## TC: O(len(nums) * sum(nums)
## SC: O(sum(nums))
