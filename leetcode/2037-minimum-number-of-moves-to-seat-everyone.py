class Solution:
    ## TC: O(n)
    ## SC: O(n)
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        MAX_VALUE = 100

        def iter_sorted(nums):  # counting sort
            counts = [0] * (MAX_VALUE + 1)
            for k in nums:
                counts[k] += 1
            for k, c in enumerate(counts):
                for _ in range(c):
                    yield k

        return sum(
            abs(seat_pos - student_pos)
            for seat_pos, student_pos in zip(iter_sorted(seats), iter_sorted(students))
        )
