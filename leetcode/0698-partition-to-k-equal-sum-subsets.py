class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        if k > len(nums):
            return False
        nums = sorted(nums, reverse=True)
        capacity = total // k
        def is_fit_k_subset(i, cap_list):
            if i >= len(nums):
                return True
            value = nums[i]
            for j in range(len(cap_list)):
                if value <= cap_list[j]:
                    cap_list[j] -= value
                    if is_fit_k_subset(i + 1, cap_list):
                        return True
                    cap_list[j] += value
                    if cap_list[j] == capacity:
                        return False
            return False
        return is_fit_k_subset(0, [capacity] * k)


## TC: O(k^n)
## SC: O(n)
