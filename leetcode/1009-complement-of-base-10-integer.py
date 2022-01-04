class Solution:
    ## TC: O(log(n))
    ## SC: O(1)
    def bitwiseComplement(self, n: int) -> int:
        bit = 1
        while bit <= n:
            bit <<= 1
        return n ^ (bit - 1)
