class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = [False] * len(arr)
        stack = [start]
        visited[start] = True
        while stack:
            pos = stack.pop()
            if arr[pos] == 0:
                return True
            left, right = pos - arr[pos], pos + arr[pos]
            if left >= 0 and not visited[left]:
                visited[left] = True
                stack.append(left)
            if right < len(arr) and not visited[right]:
                visited[right] = True
                stack.append(right)
        return False


## TC: O(n)
## SC: O(n)
