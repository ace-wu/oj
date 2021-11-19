class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        answer = 0
        x_xor_y = x ^ y
        while x_xor_y:
            answer += x_xor_y & 1
            x_xor_y >>= 1
        return answer


## TC: O(log(max(x, y)))
## SC: O(1)
