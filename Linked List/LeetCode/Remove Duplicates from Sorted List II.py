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

List = node1

def remove_all_duplicates(head):
    new = ListNode('start')
    tail1 = new

    delete = ListNode('start')
    tail2 = delete

    while head:
        if head.next and head.val == head.next.val or tail2 and head.val == tail2.val:
            tail2.next = head
            tail2 = head
        else:
            tail1.next = head
            tail1 = tail1.next
        head = head.next

    tail1.next = None
    tail2.next = None
    return new.next

def print_linked_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

print_linked_list(remove_all_duplicates(List))
