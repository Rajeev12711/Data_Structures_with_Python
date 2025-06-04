class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class MyLinkedList(object):

    def __init__(self):
        self.head = ListNode('start')


    def get(self, index):
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                return curr.val
            curr = curr.next
            i += 1
        return -1


    def addAtHead(self, val):
        new_node = ListNode(val)
        if self.head.next:
            new_node.next = self.head.next
            self.head.next.prev = new_node
        new_node.prev = self.head
        self.head.next = new_node


    def addAtTail(self, val):
        curr = self.head
        while curr.next:
            curr = curr.next
        new_node = ListNode(val, prev=curr)
        curr.next = new_node


    def addAtIndex(self, index, val):
        curr = self.head
        i = 0
        while i < index and curr.next:
            curr = curr.next
            i += 1

        if i == index:
            new_node = ListNode(val)
            new_node.next = curr.next
            new_node.prev = curr
            if curr.next:
                curr.next.prev = new_node
            curr.next = new_node


    def deleteAtIndex(self, index):
        curr = self.head
        i = 0
        while i < index and curr.next:
            curr = curr.next
            i += 1

        if i == index and curr.next:
            node_to_delete = curr.next
            curr.next = node_to_delete.next
            if node_to_delete.next:
                node_to_delete.next.prev = curr
            node_to_delete.prev = None
            node_to_delete.next = None