class Node:
    def __init__(self, key, value=None, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

    def insert_next(self, node):
        if self.next == node:
            return
        if self.next is not None:
            self.next.prev = node
        node.next = self.next
        node.prev = self
        self.next = node

    def remove(self):
        if self.next is not None:
            self.next.prev = self.prev
        if self.prev is not None:
            self.prev.next = self.next

    def __str__(self):
        if self.next is None:
            return f'{self.value}'
        return f'{self.value} -> {self.next}'


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        self.head = Node(-1, 'head')
        self.tail = Node(-1, 'tail', prev=self.head)
        self.head.next = self.tail

    def touch(self, node):
        node.remove()
        self.head.insert_next(node)

    def trim_tail(self):
        while len(self.hashmap) > self.capacity:
            del self.hashmap[self.tail.prev.key]
            self.tail.prev.remove()

    def get(self, key: int) -> int:
        node = self.hashmap.get(key)
        if not node:
            return -1
        self.touch(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            node = self.hashmap[key]
            node.value = value
            self.touch(node)
        else:
            node = Node(key, value)
            self.hashmap[key] = node
            self.head.insert_next(node)
            self.trim_tail()
        return self

    def __str__(self):
        mapping = {k: node.value for k, node in self.hashmap.items()}
        return f'{self.head} {mapping}'


## TC: get: O(1), put: O(1)
## SC: O(capacity)

cache = LRUCache(2)
print(cache)

print(cache.put(1, 1))
print(cache.put(2, 2))
print(cache.get(1))
print(cache.put(3, 3))
print(cache.get(2))
print(cache.put(4, 4))
print(cache.get(1))
print(cache.get(3))
print(cache.get(4))
print()

cache = LRUCache(2)
print(cache)

print(cache.put(1, 0))
print(cache.put(2, 2))
print(cache.get(1))
print(cache.put(3, 3))
print(cache.get(2))
print(cache.put(4, 4))
print(cache.get(1))
print(cache.get(3))
print(cache.get(4))
print()


cache = LRUCache(2)
print(cache)

print(cache.put(2, 1))
print(cache.put(2, 2))
print(cache.get(2))
print(cache.put(1, 1))
print(cache.put(4, 1))
print(cache.get(2))
