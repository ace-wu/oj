from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter = Counter(nums1)
        result = []
        for num in nums2:
            if counter.get(num, 0) > 0:
                result.append(num)
                counter[num] -= 1
        return result


## TC: O(len(num1) + len(num2))
## SC: O(1)
