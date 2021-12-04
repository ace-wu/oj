class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_p, min_p, answer = 1, 1, float('-inf')
        for n in nums:
            candidates = (n, max_p * n, min_p * n)
            max_p = max(candidates)
            min_p = min(candidates)
            answer = max(answer, max_p)
        return answer


# TC: O(n)
# SC: O(1)
