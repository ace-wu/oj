from typing import List

class NumArray:
    def __init__(self, nums: List[int]):
        self.sums = [0]
        if not nums:
            return
        for n in nums:
            self.sums.append(self.sums[-1] + n)

    def sumRange(self, left: int, right: int) -> int:
        return self.sums[right+1] - self.sums[left]

## TC: build: O(n), query: O(1)
## SC: O(n)

nums = NumArray([-2, 0, 3, -5, 2, -1])
print(nums.sumRange(0, 2))
print(nums.sumRange(2, 5))
print(nums.sumRange(0, 5))
