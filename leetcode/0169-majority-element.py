# https://leetcode.com/problems/majority-element/

class Solution(object):
    def majorityElement(self, nums):
        mode = None
        count = 0
        for n in nums:
            if count == 0:
                count += 1
                mode = n
            elif n == mode:
                count += 1
            else:
                count -= 1
        return mode
