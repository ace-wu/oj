class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nge_map = {}
        stack = []
        for value in nums2:
            while stack and value > stack[-1]:
                nge_map[stack.pop()] = value
            stack.append(value)
        return [nge_map.get(value, -1) for value in nums1]


## TC: O(len(nums1) + len(nums2))
## SC: O(len(nums1)) for output space, O(len(nums2)) for additional space
