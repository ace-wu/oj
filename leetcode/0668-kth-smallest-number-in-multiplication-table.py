import heapq


class Solution:
    def findKthNumber_heapq(self, m: int, n: int, k: int) -> int:
        pq = [(1, 1, 1)]
        seen = set([(0, 0)])
        while pq:
            value, i, j = heapq.heappop(pq)
            k -= 1
            if k == 0:
                return value
            if i+1 <= m and (i+1, j) not in seen:
                heapq.heappush(pq, ((i+1)*j, i+1, j))
                seen.add((i+1, j))
            if j+1 <= n and (i, j+1) not in seen:
                heapq.heappush(pq, (i*(j+1), i, j+1))
                seen.add((i, j+1))
        return Noneclass Solution:

    def findKthNumber_bisect(self, m: int, n: int, k: int) -> int:
        if m > n:
            m, n = n, m
        def get_rank(v):
            return sum(min(n, v // i) for i in range(1, m + 1))
        low, mid, high, answer = 0, 0, m*n+1, 0
        while low <= high:
            mid = (low + high) // 2
            if get_rank(mid) < k:
                low = mid + 1
            else:
                high = mid - 1
                answer = mid
        return answer


## heapq solution:
##  TC: O(k*log(m+n))
##  SC: O(m+n)

## bisect solution:
##  TC: O(min(m,n)*log(m*n))
##  SC: O(2)
