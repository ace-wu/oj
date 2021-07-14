# https://leetcode.com/problems/kth-largest-element-in-an-array/

def partition(nums, l, r):
    p = nums[r]
    i = l
    for j in range(l, r):
        if nums[j] >= p:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    nums[i], nums[r] = nums[r], nums[i]
    return i


def find_kth_rec(nums, k, l, r):
    if not l <= k <= r:
        return None
    p_index = partition(nums, l, r)
    if (p_index == k):
        return nums[p_index]
    elif (p_index > k):
        return find_kth_rec(nums, k, l, p_index - 1)
    else:
        return find_kth_rec(nums, k, p_index + 1, r)


def find_kth(nums, k):
    return find_kth_rec(nums, k - 1, 0, len(nums) - 1)


class Solution(object):
    def findKthLargest(self, nums, k):
        return find_kth(nums, k)


nums = [10, 4, 5, 8, 6, 11, 26, 0, 22, 17]
print(list(reversed(sorted(nums))))
print([find_kth(nums, i) for i in range(1, len(nums) + 1)])
