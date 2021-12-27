class Solution:

    ## TC: O(log(n))
    ## SC: O(1)
    def findComplement(self, num: int) -> int:
        answer, bit = 0, 1
        while num:
            if num & 1 == 0:
                answer |= bit
            num >>= 1
            bit <<= 1
        return answer

    ## TC: O(log(n))
    ## SC: O(1)
    def findComplement(self, num: int) -> int:
        bit = 1
        while bit <= num:
            bit <<= 1
        return (bit - 1) ^ num
