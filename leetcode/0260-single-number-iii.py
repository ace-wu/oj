from operator import xor
from functools import reduce


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        a_xor_b = reduce(xor, nums)
        diff_bit = a_xor_b & (a_xor_b - 1) ^ a_xor_b
        a = reduce(xor, (n for n in nums if n & diff_bit))
        b = a ^ a_xor_b
        return a, b


## TC: O(n)
## SC: O(1)
