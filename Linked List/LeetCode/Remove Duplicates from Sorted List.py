class ListNode:
    def __init__(self, val):
        self.val= val
        self.next = None

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(2)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

curr = node1

def remove_from_list(head):
    if not head:
        return None
    list2 = ListNode(head.val)
    tail = list2
    head = head.next
    while head:
        if tail.val != head.val:
            tail.next = ListNode(head.val)
            tail = tail.next
        head = head.next
    return list2

def print_linked_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

values =remove_from_list(curr)
print_linked_list(values)