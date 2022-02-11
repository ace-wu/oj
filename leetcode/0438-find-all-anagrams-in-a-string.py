from collections import Counter


class Solution:
    ## TC: O(len(s) + len(p))
    ## SC: O(A) where A is the size of alphabet
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_s, len_p = len(s), len(p)
        if len_s < len_p:
            return []

        char_counter = Counter(p)
        mismatch_count = len(char_counter)
        answer = []

        for i in range(len_s):
            char_counter[s[i]] -= 1
            if char_counter[s[i]] == 0:
                mismatch_count -= 1
            if i >= len_p:
                char_counter[s[i - len_p]] += 1
                if char_counter[s[i - len_p]] == 1:
                    mismatch_count += 1
            if mismatch_count == 0:
                answer.append(i - len_p + 1)

        return answer
