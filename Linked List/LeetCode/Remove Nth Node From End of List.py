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

def remove_n(head, n=2):
    curr = head
    count = 0
    while curr:
        count += 1
        curr = curr.next
    pos = count - n

    dummy = Node(-1)
    dummy.next = head
    curr = dummy
    for i in range(pos):
        curr = curr.next

    curr.next = curr.next.next
    return dummy.next

def print_linked_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

print_linked_list(remove_n(first))