from typing import List

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        length = len(profit)
        end_events = [(0, 0, 0)] + list(sorted(zip(startTime, endTime, profit), key=lambda x: x[1]))
        start_index = {}
        i = 0
        for start_time in sorted(startTime):
            while i+1 < length and start_time >= end_events[i+1][1]:
                i += 1
            start_index[start_time] = i

        max_profit = [0] * (length + 1)
        for i in range(1, length+1):
            start_time, end_time, p = end_events[i]
            max_profit[i] = max(
                max_profit[i - 1],
                p + max_profit[start_index[start_time]],
            )
        return max_profit[-1]


## TC: O(n*log(n))
## SC: O(n)

s = Solution()
s.jobScheduling(
    [1,2,3,4,6],
    [3,5,10,6,9],
    [20,20,100,70,60],
)
