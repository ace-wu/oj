class Solution:
    ## TC: O(log(num)^2)
    ## SC: O(1)
    def addDigits(self, num: int) -> int:
        while num >= 10:
            next_num = 0
            while num:
                next_num += (num % 10)
                num //= 10
            num = next_num
        return num

    ## TC: O(1)
    ## TC: O(1)
    def addDigits(self, num: int) -> int:
        return num % 9 or 9 if num else 0
