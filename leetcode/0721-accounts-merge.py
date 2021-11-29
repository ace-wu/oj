from collections import defaultdict


class UnionFind:
    def __init__(self):
        self.parent = defaultdict(lambda: None)
        self.order = defaultdict(int)

    def find(self, x):
        if self.parent[x] is None:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.order[x] < self.order[y]:
            x, y = y, x
        self.parent[y] = x
        self.order[x] += 1


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind()
        email_to_name = {}
        email_to_index = {}
        for name, *emails in accounts:
            for email in emails:
                email_to_name[email] = name
                if email not in email_to_index:
                    email_to_index[email] = len(email_to_index)
                email_i = email_to_index[email]
            if len(emails) >= 2:
                for i in range(len(emails) - 1):
                    uf.union(email_to_index[emails[i]], email_to_index[emails[i + 1]])
        answer = defaultdict(list)
        for email in email_to_index:
            answer[uf.find(email_to_index[email])].append(email)
        return [[email_to_name[emails[0]]] + sorted(emails) for emails in answer.values()]
