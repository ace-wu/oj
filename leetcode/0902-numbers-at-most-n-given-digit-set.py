class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        def count_numbers(digits, n_str, k, count_zero=False):
            if k >= len(n_str):
                return 1
            count = 0
            if count_zero:
                for i in range(1, len(n_str)):
                    count += len(digits) ** i
            for d in digits:
                if d < n_str[k]:
                    count += len(digits) ** (len(n_str) - k - 1)
                elif d == n_str[k]:
                    count += count_numbers(digits, n_str, k + 1)
                else:
                    break
            return count
        return count_numbers(digits, str(n), 0, True)


## TC: O(log(n))
## SC: O(log(n))
