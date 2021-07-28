class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest = sum(nums[:3]) - target
        nums = sorted(nums)
        length = len(nums)
        for i in range(length):
            j = i + 1
            k = length - 1
            while j < k:
                diff = nums[i] + nums[j] + nums[k] - target
                if abs(diff) < abs(closest):
                    closest = diff
                    if closest == 0:
                        return target
                if diff < 0:
                    j += 1
                else:
                    k -= 1
        return target + closest
