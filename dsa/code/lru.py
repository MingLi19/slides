from collections import deque


class LRUCache:
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._memory = dict()
        self._queue = deque()

    def get(self, key: int) -> str:
        if key not in self._memory:
            return -1
        self._queue.remove(key)
        self._queue.append(key)
        return self._memory[key]

    def put(self, key: int, value: str):
        if key in self._memory:
            self._queue.remove(key)
        elif len(self._memory) == self._capacity:
            oldest = self._queue.popleft()
            self._memory.pop(oldest)
        self._memory[key] = value
        self._queue.append(key)

    def __repr__(self):
        return str(self._memory) + ' : ' + str(self._queue)


cache = LRUCache(3)
cache.put(1, 'A')
cache.put(2, 'B')
cache.put(3, 'C')
print('缓存', cache)
print('----')

cache.put(4, 'D')
print('缓存', cache)
print('查找 id(1): ', cache.get(1))
print('----')

print('缓存', cache)
print('查找 id(2): ', cache.get(2))
