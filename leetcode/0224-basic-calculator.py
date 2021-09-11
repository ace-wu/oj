class Solution:
    def calculate(self, s: str) -> int:
        is_digit = lambda c: '0' <= c <= '9'
        global_sign = [1]
        my_sign = 1
        total = 0
        i = 0
        while i < len(s):
            c = s[i]
            if is_digit(c):
                begin = i
                while i < len(s) and is_digit(s[i]):
                    i += 1
                total += global_sign[-1] * my_sign * int(s[begin:i])
                continue
            elif c == '(':
                global_sign.append(global_sign[-1] * my_sign)
            elif c == ')':
                global_sign.pop()
            if c != ' ':
                my_sign = -1 if c == '-' else 1
            i += 1
        return total


## TC: O(n)
## SC: O(n)

s = Solution()
print(s.calculate(' ( 1  +(4+5+2)-3)+(6+8)'))
print(s.calculate('- (3 + (4 + 5))'))
