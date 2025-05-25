class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

first = node1


list_node1 = ListNode(1)
list_node2 = ListNode(2)
list_node3 = ListNode(3)
list_node4 = ListNode(4)
list_node5 = ListNode(5)

list_node1.next = list_node2
list_node2.next = list_node3
list_node3.next = list_node4
list_node4.next = list_node5

second = list_node1

def merge_list(list1, list2):
    dummy = ListNode(-1)
    tail = dummy

    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            tail = tail.next
            list1 = list1.next
        else:
            tail.next = list2
            tail = tail.next
            list2 = list2.next
    if list1:
        tail.next = list1
    if list2:
        tail.next = list2

    return dummy.next

def print_linked_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

final = merge_list(first, second)
print_linked_list(final)
