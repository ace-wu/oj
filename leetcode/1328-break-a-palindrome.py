class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        length = len(palindrome)
        if length <= 1:
            return ''
        for i in range(length // 2):
            if palindrome[i] != 'a':
                return palindrome[:i] + 'a' + palindrome[i+1:]
        return palindrome[:-1] + 'b'


## TC: O(n)
## SC: O(n) output space, O(1) extra space
