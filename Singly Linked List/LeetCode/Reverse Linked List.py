class Node:
    def __init__(self, val):
        self.val = val
        self.next = None



node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5


first = node1


def reverser_linkedlist(head):
    prev = None
    while head:
        nextNode = head.next
        head.next = prev
        prev = head
        head = nextNode
    return prev

def print_linked_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


reversed_head = reverser_linkedlist(first)
print_linked_list(reversed_head)




