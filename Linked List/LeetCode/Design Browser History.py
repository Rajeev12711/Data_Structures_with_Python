class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class BrowserHistory(object):

    def __init__(self, homepage):
        self.head = ListNode(homepage)

    def visit(self, url):
        self.head.next = ListNode(url, self.head)
        self.head = self.head.next

    def back(self, steps):
        while self.head.prev and steps > 0:
            self.head = self.head.prev
            steps -= 1
        return self.head.val

    def forward(self, steps):
        while self.head.next and steps > 0:
            self.head = self.head.next
            steps -= 1
        return self.head.val
