class MapSum:
    def __init__(self):
        self.map = {}

    def insert(self, key: str, val: int) -> None:
        self.map[key] = val

    def sum(self, prefix: str) -> int:
        return sum([self.map[key] for key in self.map if key.startswith(prefix)])

s = MapSum()
s.insert('apple', 3)
print(s.sum('ap'))
s.insert('app', 2)
print(s.sum('ap'))
s.insert('app', 4)
print(s.sum('ap'))
