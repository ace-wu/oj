class Solution:
    ## TC: O(n)
    ## SC: O(n)
    def reversePrefix(self, word: str, ch: str) -> str:
        for i, c in enumerate(word):
            if c != ch:
                continue
            return word[i::-1] + word[i + 1 :]
        return word
