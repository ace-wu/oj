class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        answer = []
        a1, a2 = intervals[0]
        for b1, b2 in intervals:
            if b1 <= a2:
                a2 = max(a2, b2)
            else:
                answer.append([a1, a2])
                a1, a2 = b1, b2
        answer.append([a1, a2])
        return answer


## TC: O(n*log(n))
## SC: O(n) for output space, O(1) for extra space
