class ListNode:
    def __init__(self, val= None, next=None):
        self.val = val
        self.next = next


def reverse(node):

    if node.next is None:
        return node.val

    new =  reverse(node.next)

    node.next.next= node
    node.next = None
    return node


head = ListNode(10, ListNode(20, ListNode(30, ListNode(40, ListNode(50, None)))))
print(reverse(head))