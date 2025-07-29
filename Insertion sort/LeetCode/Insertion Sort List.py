class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

node1 = Node(1)
node2 = Node(5)
node3 = Node(2)
node4 = Node(4)
node5 = Node(3)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

head = node1

def insertionSortList(heads):
    dummy = Node(0)
    dummy.next = heads

    prev, cur = heads, heads.next

    while cur:

        if cur.val >= prev.val:
            prev = cur
            cur = cur.next
            continue

        tmp = dummy
        while tmp.next.val < cur.val:
            tmp = tmp.next

        prev.next = cur.next

        cur.next = tmp.next
        tmp.next = cur

        cur = prev.next

    return dummy.next



def print_linked_list(heads):
    while heads:
        print(heads.val, end=" -> ")
        heads = heads.next
    print("None")

print_linked_list(insertionSortList(head))