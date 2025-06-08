class MyStack(object):

    def __init__(self):
        self.p = deque()

    def push(self, x):

        self.p.append(x)

    def pop(self):

        item = self.p.pop()
        return item

    def top(self):

        if self.empty():
            return None
        return self.p[-1]

    def empty(self):

        return len(self.p) == 0
