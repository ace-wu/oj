from typing import List


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        length = len(num)
        def iter_solutions(start=0, expr='', value=0, term_value=None):
            if start == length and value == target:
                yield expr
                return
            for end in range(start + 1, length + 1): # [start ...] [end ...]
                if end - start >= 2 and num[start] == '0': # prevent '0##'
                    break
                curr_expr = num[start:end]
                curr_value = int(curr_expr)
                if term_value is None:
                    yield from iter_solutions(end, curr_expr, curr_value, curr_value)
                else:
                    yield from iter_solutions(end, f'{expr}+{curr_expr}', value + curr_value, curr_value)
                    yield from iter_solutions(end, f'{expr}-{curr_expr}', value - curr_value, -curr_value)
                    yield from iter_solutions(end, f'{expr}*{curr_expr}', value - term_value + term_value * curr_value, term_value * curr_value)
        return list(iter_solutions())

    def addOperators_sums_of_prods(self, num: str, target: int) -> List[str]:
        def iter_prods(num, target):
            for i in range(1, len(num)):
                lhs = int(num[:i])
                if str(lhs) != num[:i]:
                    continue
                if target is None:
                    rhs_target = None
                elif lhs == 0:
                    if target == 0:
                        rhs_target = None
                    else:
                        continue
                elif target % lhs != 0:
                    continue
                else:
                    rhs_target = target // lhs
                for rhs, rhs_expr in iter_prods(num[i:], rhs_target):
                    yield lhs * rhs, f'{num[:i]}*{rhs_expr}'
            if target is None or num == str(target):
                if num == str(int(num)):
                    yield int(num), num

        def iter_sums_of_prods(num, target, is_pos=True):
            for i in range(1, len(num)):
                for lhs, lhs_expr in iter_prods(num[:i], None):
                    op = '+' if is_pos else '-'
                    for rhs, rhs_expr in iter_sums_of_prods(num[i:], target - lhs, is_pos):
                        yield lhs + rhs, f'{lhs_expr}{op}{rhs_expr}'
                    op = '-' if is_pos else '+'
                    for rhs, rhs_expr in iter_sums_of_prods(num[i:], lhs - target, not is_pos):
                        yield lhs - rhs, f'{lhs_expr}{op}{rhs_expr}'
            yield from iter_prods(num, target)

        return [expr for _, expr in iter_sums_of_prods(num, target)]


s = Solution()
print(s.addOperators('123', 6))
print(s.addOperators('105', 5))
print(s.addOperators('000', 0))
print(s.addOperators('3456237490', 9191))
print(s.addOperators('123456789', 45))
