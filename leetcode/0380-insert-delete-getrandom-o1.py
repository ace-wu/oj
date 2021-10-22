from random import choice


class RandomizedSet:

    def __init__(self):
        self._map = {}
        self._list = []

    def insert(self, val: int) -> bool:
        if val in self._map:
            return False
        self._map[val] = len(self._list)
        self._list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self._map:
            return False
        index = self._map.pop(val)
        if val != self._list[-1]:
            self._map[self._list[-1]] = index
        self._list[index] = self._list[-1]
        self._list.pop()
        return True

    def getRandom(self) -> int:
        return choice(self._list)


## TC: O(1)
## SC: O(n)
