from collections import defaultdict


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        in_degree = defaultdict(int)
        for u, v in prerequisites:
            adj_list[v].append(u)
            in_degree[u] += 1
        answer = []
        stack = []
        for i in range(numCourses):
            if in_degree[i] == 0:
                stack.append(i)
        while stack:
            course = stack.pop()
            answer.append(course)
            for next_course in adj_list[course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    stack.append(next_course)
        return answer if len(answer) == numCourses else []


## TC: O(n)
## SC: O(n)
