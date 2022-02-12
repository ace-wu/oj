from collections import Counter


class Solution:
    ## TC: O(len(s1) + len(s2))
    ## SC: O(A) where A is the size of alphabet
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1, len_s2 = len(s1), len(s2)
        if len_s1 > len_s2:
            return False

        char_counter = Counter(s1)
        mismatch_count = len(char_counter)

        for i in range(len_s2):
            char_counter[s2[i]] -= 1
            if char_counter[s2[i]] == 0:
                mismatch_count -= 1
            if i >= len_s1:
                char_counter[s2[i - len_s1]] += 1
                if char_counter[s2[i - len_s1]] == 1:
                    mismatch_count += 1
            if mismatch_count == 0:
                return True
        return False
