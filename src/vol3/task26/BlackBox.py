import heapq


class BlackBox:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []
        self.i = 0

    def add(self, x):
        if len(self.max_heap) < self.i:
            heapq.heappush(self.max_heap, -x)
        else:
            heapq.heappush(self.min_heap, x)
        self._balance()

    def get(self):
        self.i += 1
        self._balance()
        return -self.max_heap[0]

    def _balance(self):
        while len(self.max_heap) < self.i and self.min_heap:
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -val)
        while len(self.max_heap) > self.i:
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)