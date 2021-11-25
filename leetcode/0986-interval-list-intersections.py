class Solution:
    def intervalIntersection(self, list1: List[List[int]], list2: List[List[int]]) -> List[List[int]]:
        answer = []
        i1, i2 = 0, 0
        while i1 < len(list1) and i2 < len(list2):
            s1, e1 = list1[i1]  # (s1 e1)
            s2, e2 = list2[i2]  # <s2 e2>
            if e1 < s2:         # ( ) < >
                i1 += 1
            elif e2 < s1:       # < > ( )
                i2 += 1
            elif s1 <= s2:
                if e1 <= e2:    # ( < ) >
                    answer.append((s2, e1))
                    i1 += 1
                else:           # ( < > )
                    answer.append((s2, e2))
                    i2 += 1
            else: # s2 < s1
                if e2 <= e1:    # < ( > )
                    answer.append((s1, e2))
                    i2 += 1
                else:           # < ( ) >
                    answer.append((s1, e1))
                    i1 += 1
        return answer

    def intervalIntersection_simplified(self, list1: List[List[int]], list2: List[List[int]]) -> List[List[int]]:
        answer = []
        i1, i2 = 0, 0
        while i1 < len(list1) and i2 < len(list2):
            s1, e1 = list1[i1]
            s2, e2 = list2[i2]
            if s1 <= e2 and s2 <= e1:
                answer.append((max(s1, s2), min(e1, e2)))
            if e1 <= e2:
                i1 += 1
            else: # e1 > e2
                i2 += 1
        return answer


## TC: O(n)
## SC: O(1)
