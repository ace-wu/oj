class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        parse_complex_number = lambda num_str: map(int, num_str.rstrip('i').split('+'))
        real1, imag1 = parse_complex_number(num1)
        real2, imag2 = parse_complex_number(num2)
        return f'{real1*real2-imag1*imag2}+{real1*imag2+real2*imag1}i'


## TC: O(len(num1+num2))
## SC: O(len(num1+num2)) for the output, O(1) for others

s = Solution()
print(s.complexNumberMultiply('1+1i', '1+1i'))
print(s.complexNumberMultiply('1+-1i', '1+-1i'))
