class Solution:
    def maxLength_set(self, word_list: List[str]) -> int:
        set_list = [set()]
        for word in word_list:
            word_set = set(word)
            if len(word_set) != len(word):
                continue
            for total_word_set in set_list:
                if total_word_set & word_set:
                    continue
                set_list.append(total_word_set | word_set)
        return max(len(word_set) for word_set in set_list)

    def maxLength_mask(self, word_list: List[str]) -> int:
        def iter_masks(word_list):
            for word in word_list:
                mask = 0
                for c in word:
                    c_mask = (1 << (ord(c) - ord('a')))
                    if mask & c_mask:
                        break
                    mask |= c_mask
                else:
                    yield mask, len(word)
        mask_list = list(iter_masks(word_list))

        @cache
        def get_max_length(total_mask, total_length, i):
            if i >= len(mask_list):
                return total_length
            mask, length = mask_list[i]
            max_length = get_max_length(total_mask, total_length, i + 1)
            if total_mask & mask == 0:
                max_length = max(max_length, get_max_length(total_mask | mask, total_length + length, i + 1))
            return max_length
        return get_max_length(0, 0, 0)
