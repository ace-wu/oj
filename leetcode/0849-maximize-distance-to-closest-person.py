class Solution:
    # TC: O(n)
    # SC: O(1)
    def maxDistToClosest(self, seats: List[int]) -> int:
        left, right = 0, len(seats) - 1
        while seats[left] == 0:
            left += 1
        while seats[right] == 0:
            right -= 1
        max_dist = max(left, len(seats) - 1 - right)
        while left < right:
            next_left = left + 1
            while seats[next_left] == 0:
                next_left += 1
            max_dist = max(max_dist, (next_left - left) // 2)
            left = next_left
        return max_dist
