class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        # adds elements to the buffer
        # 1. add item
        # 2. if full in capacity, replace oldest element
        self.storage[self.current] = item
        self.current += 1
        if self.current == self.capacity:
            self.current = 0

    def get(self):
        # method returns all of the elements in the buffer in a list in their given order. It should not return any `None` values in the list even if they are present in the ring buffer
        # 1.go through list
        # 2.if there's a "none", take that none out
        # 3.return list
        for i in range(len(self.storage)):
            if self.storage[i] == None:
                return self.storage[:i]
        return self.storage
