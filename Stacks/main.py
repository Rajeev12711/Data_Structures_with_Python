from sys import getsizeof

class Stack:
    def __init__(self):
        self.arr=[]

    def push(self, num):
        self.arr.append(num)

    def pop(self):
        return self.arr.pop()

    def peek(self):
        return self.arr[-1]