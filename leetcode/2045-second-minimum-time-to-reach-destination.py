from collections import deque


class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        adj_list = [[] for i in range(n + 1)]
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        def find_second_shortest():
            # search the shortest k
            shortest = [float('inf')] * (n + 1)
            shortest[1] = 0
            queue = deque([1])
            while queue:
                node = queue.popleft()
                length = shortest[node]
                for neighbor in adj_list[node]:
                    if length + 1 < shortest[neighbor]:
                        queue.append(neighbor)
                        shortest[neighbor] = length + 1

            # search if there is a second shortest k+1
            queue = deque([(1, 0)])
            while queue:
                node, length = queue.popleft()
                for neighbor in adj_list[node]:
                    if length <= shortest[neighbor]:
                        if neighbor == n:
                            if length == shortest[n]:
                                return shortest[n] + 1
                        queue.append((neighbor, length + 1))
            return shortest[n] + 2

        step = find_second_shortest()

        offset = time % (change * 2)
        if offset == 0:
            return step * time
        cycle_length = change // offset + int(bool(change % offset))
        cycle_wait = ((time * cycle_length) // change + 1) * change - (time * cycle_length)
        return step * time + (step // cycle_length - int(bool(step % cycle_length == 0))) * cycle_wait


## TC: O(V + E)
## SC: O(V + E)
## where V = #vertex and E = #edges
