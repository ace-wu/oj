from collections import Counter


class Solution:
    ## TC: O(len(s) + len(t))
    ## SC: O(A) where A is size of the alphabet
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
