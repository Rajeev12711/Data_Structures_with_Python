class MinStack(object):
    # def __init__(self):
    #     self.stack = []
    #     self.min_stack = []
    #
    # def push(self, val):
    #     self.stack.append(val)
    #     val= min(val, self.min_stack[-1] if self.min_stack else val)
    #     self.min_stack.append(val)
    #
    # def pop(self):
    #     self.stack.pop()
    #
    # def top(self):
    #     return self.stack[-1]
    #
    # def getmin(self):
    #     return self.min_stack[-1]

    # Without 2 Stack
    def __init__(self):
        self.stack = []
        self.min=float("inf")

    def push(self, val):
        self.stack.append(val)
        if val<self.min:
            self.min=val

    def pop(self):
        popped=self.stack.pop()
        if popped== self.min:
            self.min = min(self.stack) if self.stack else float('inf')

    def top(self):
        return self.stack[-1]

    def getmin(self):
        return self.min




