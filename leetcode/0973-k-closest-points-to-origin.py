import heapq


class Solution:
    # heapify and pop first k elements
    ## TC: O(n + k*log(n))
    ## SC: O(n)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = [(x**2 + y**2, x, y) for x, y in points]
        heapq.heapify(pq)
        answer = []
        for i in range(k):
            dist, x, y = heapq.heappop(pq)
            answer.append([x, y])
        return answer

    # keep only k elements in heap
    ## TC: O(n*log(k))
    ## SC: O(k)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        for x, y in points:
            dist = -(x**2 + y**2)
            if len(pq) < k:
                heapq.heappush(pq, (dist, x, y))
            else:
                heapq.heappushpop(pq, (dist, x, y))
        return [[x, y] for dist, x, y in pq]
