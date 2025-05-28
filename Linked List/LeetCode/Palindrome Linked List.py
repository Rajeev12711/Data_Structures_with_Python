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

def palindrome(head):
    dummy1 = ListNode("start")
    tail1 = dummy1

    curr = head
    while curr:
        tail1.next = ListNode(curr.val)
        tail1 = tail1.next
        curr = curr.next

    dummy1 = dummy1.next
    prev = None
    while dummy1:
        next_node = dummy1.next
        dummy1.next = prev
        prev = dummy1
        dummy1 = next_node

    while prev and head:
        if prev.val != head.val:
            return False
        prev = prev.next
        head = head.next

    return True

print(palindrome(List))