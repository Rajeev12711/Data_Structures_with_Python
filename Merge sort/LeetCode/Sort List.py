class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def sortList(head):
    if not head or not head.next:
        return head

    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    mid = slow.next
    slow.next = None

    left = sortList(head)
    right = sortList(mid)

    dummy = ListNode(0)
    curr = dummy

    while left and right:
        if left.val < right.val:
            curr.next = left
            left = left.next
        else:
            curr.next = right
            right = right.next
        curr = curr.next
    curr.next = left or right

    return dummy.next


def printList(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    print(res)

node = ListNode(1, ListNode(5, ListNode(8, ListNode(9, ListNode(3)))))
sorted_node = sortList(node)
printList(sorted_node)


