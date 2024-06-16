import heapq


class Solution:
    ## TC: O(n*log(n))
    ## SC: O(n)
    def findMaximizedCapital(
        self, k: int, cap: int, profits: list[int], capital: list[int]
    ) -> int:
        min_cap_pq = list(zip(capital, profits))
        heapq.heapify(min_cap_pq)
        max_pro_pq = []
        for _ in range(k):
            while min_cap_pq:
                c, p = min_cap_pq[0]
                if c > cap:
                    break
                heapq.heappush(max_pro_pq, -p)
                heapq.heappop(min_cap_pq)
            if not max_pro_pq:
                break
            cap -= heapq.heappop(max_pro_pq)
        return cap
