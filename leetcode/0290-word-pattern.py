class Solution:
    ## TC: O(m+n)
    ## SC: O(m+n)
    ## where m = len(pattern) and n = len(s)
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        word_to_letter = {}
        letter_to_word = {}
        for letter, word in zip(pattern, words):
            if word in word_to_letter or letter in letter_to_word:
                if word_to_letter.get(word) != letter or letter_to_word.get(letter) != word:
                    return False
            else:
                word_to_letter[word] = letter
                letter_to_word[letter] = word
        return True
