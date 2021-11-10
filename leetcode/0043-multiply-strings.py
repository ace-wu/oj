class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ord_0 = ord('0')
        num1 = num1[::-1]
        num2 = num2[::-1]
        m = len(num1)
        n = len(num2)
        answer = []
        digit_sum = 0
        for k in range(m + n - 1):
            for i in range(m):
                if 0 <= k-i < n:
                    digit_sum += (ord(num1[i]) - ord_0) * (ord(num2[k-i]) - ord_0)
            answer.append(chr(digit_sum % 10 + ord_0))
            digit_sum //= 10
        while digit_sum:
            answer.append(chr(digit_sum % 10 + ord_0))
            digit_sum //= 10
        while len(answer) > 1 and answer[-1] == '0':
            answer.pop()
        return ''.join(answer[::-1])


## TC: O(m*n)
## SC: O(m+n)
