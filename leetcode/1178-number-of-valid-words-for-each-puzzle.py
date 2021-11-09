from operator import or_
from collections import Counter

class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        ord_a = ord('a')
        def to_mask(word):
            return reduce(or_, (1 << (ord(c) - ord_a) for c in word))
        def contains(mask1, mask2):
            return (mask1 | mask2) == mask1
        def iter_submasks(mask):
            submask = mask
            while submask:
                yield submask
                submask = (submask - 1) & mask

        word_counter = Counter((to_mask(word) for word in words))

        answer = []
        for puzzle in puzzles:
            first_char_mask = to_mask(puzzle[0])
            puzzle_mask = to_mask(puzzle)
            count = 0
            for submask in iter_submasks(puzzle_mask):
                if contains(submask, first_char_mask):
                    count += word_counter[submask]
            answer.append(count)
        return answer


## TC: O(m + n * 3^l)
## SC: O(m)
## where m == len(words), n == len(puzzles), l == len(puzzles[0]) == 7
