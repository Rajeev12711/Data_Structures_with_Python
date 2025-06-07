from collections import deque


class Queues:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, val):
        self.queue.append(val)

    def dequeue(self):
        if self.empty():
            return 'Empty'
        return self.queue.popleft()

    def peek(self):
        if self.empty():
            return 'Empty'
        return self.queue[0]


    def empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)