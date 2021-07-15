class Solution(object):
    def licenseKeyFormatting(self, s, k):
        s = s.replace('-', '').upper()
        return '-'.join(s[max(i, 0):i+k] for i in range(len(s) % k - k, len(s), k)).strip('-')


s = Solution()
print('5F3Z-2e-9-w')
print(s.licenseKeyFormatting('5F3Z-2e-9-w', 5))
print(s.licenseKeyFormatting('5F3Z-2e-9-w', 4))
print(s.licenseKeyFormatting('5F3Z-2e-9-w', 3))
print(s.licenseKeyFormatting('5F3Z-2e-9-w', 2))
print(s.licenseKeyFormatting('5F3Z-2e-9-w', 1))

print('2-5g-3-J')
print(s.licenseKeyFormatting('2-5g-3-J', 5))
print(s.licenseKeyFormatting('2-5g-3-J', 4))
print(s.licenseKeyFormatting('2-5g-3-J', 3))
print(s.licenseKeyFormatting('2-5g-3-J', 2))
print(s.licenseKeyFormatting('2-5g-3-J', 1))
