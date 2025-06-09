class MyQueue(object):

    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        rever = self.stack[::-1]
        data = rever.pop()
        self.stack = rever[::-1]
        return data

    def peek(self):
        return self.stack[0]

    def empty(self):
        return len(self.stack) == 0