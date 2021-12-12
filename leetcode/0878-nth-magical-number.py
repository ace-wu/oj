class Solution:
    def nthMagicalNumber_bisect(self, n: int, a: int, b: int) -> int:
        if a > b:
            a, b = b, a
        def gcd(a, b):
            while b > 0:
                a, b = b, a % b
            return a
        lcm = a * b // gcd(a, b)
        low, mid, high = 1, 1, a * n
        while low < high:
            mid = (low + high) // 2
            if mid // a + mid // b - mid // lcm < n:
                low = mid + 1
            else:
                high = mid
        return low % (10**9 + 7)

    def nthMagicalNumber_search_back(self, n: int, a: int, b: int) -> int:
        if a > b:
            a, b = b, a
        def gcd(a, b):
            while b > 0:
                a, b = b, a % b
            return a
        lcm = a * b // gcd(a, b)
        lcm_size = (lcm // a) + (lcm // b) - 1
        lcm_count = n // lcm_size
        rest = n % lcm_size

        a_count, b_count = rest, a * rest // b
        while a_count + b_count > rest:
            if a * a_count < b * b_count:
                b_count -= 1
            else:
                a_count -= 1
        return (lcm * lcm_count + max(a * a_count, b * b_count)) % (10**9 + 7)



## TC: O(log(n) + log(min(a, b)))
## SC: O(1)
