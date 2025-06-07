class ListNode:
    def __init__(self, val, next=None):
        self.val=val
        self.next=next

class Queues:
    def __init__(self):
        self.head = ListNode('start')
        self.tail = self.head

    def enqueue(self, val):
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def dequeue(self):
        if self.empty():
            return 'Empty'
        val = self.head.next.val
        self.head.next =self.head.next.next
        if self.head.next is None:
            self.tail = self.head
        return val

    def peek(self):
        if self.empty():
            return 'Empty'
        return self.head.next.val


    def empty(self):
        return self.head.next is None

    def size(self):
        curr = self.head.next
        count =0
        while curr:
            curr = curr.next
            count +=1
        return count