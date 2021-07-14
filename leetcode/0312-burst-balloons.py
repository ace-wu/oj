# https://leetcode.com/problems/burst-balloons/

def max_coins(nums):
    if not nums:
        return 0
    nums = [1] + nums + [1]
    size = len(nums)
    table = [[0] * size for i in range(size)]

    for w in range(2, size):
        for i in range(size - w):
            j = i + w
            prod_ij = nums[i] * nums[j]
            table[i][j] = max([nums[k] * prod_ij + table[i][k] + table[k][j] for k in range(i + 1, j)])

    return table[0][size-1]


class Solution(object):
    def maxCoins(self, nums):
        return max_coins(nums)


#print(max_coins([2]))
#print(max_coins([2, 1, 2]))
print(max_coins([3, 1, 5, 8]))


