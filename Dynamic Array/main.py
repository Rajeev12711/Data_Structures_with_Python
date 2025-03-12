class DynamicArray:

    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.arr = [0] * capacity

    def get(self, i):
        return self.arr[i]

    def set(self, i, n):
        self.arr[i] = n

    def pushback(self, n):
        if self.size == self.capacity:
            self.resize()
        self.arr[self.size] = n
        self.size += 1

    def pop_back(self):
        if self.size > 0:
            self.size -= 1
        return self.arr[self.size]

    def resize(self):
        self.capacity = 2 * self.capacity
        new_arr = [0] * self.capacity

        for i in range(self.size):
            new_arr[i] = self.arr[i]
        self.arr = new_arr

    def getsize(self):
        return self.size

    def get_capacity(self):
        return self.capacity

