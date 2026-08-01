class ListNode:
    def __init__(self, val=""):
        self.val = val
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = ListNode(homepage)
        self.curr = self.history

    def visit(self, url: str) -> None:
        self.curr.next = ListNode(url)
        self.curr.next.prev = self.curr
        self.curr = self.curr.next

    def back(self, steps: int) -> str:
        for s in range(steps):
            if self.curr.prev == None:
                break
            self.curr = self.curr.prev
        return self.curr.val

    def forward(self, steps: int) -> str:
        for s in range(steps):
            if self.curr.next == None:
                break
            self.curr = self.curr.next
        return self.curr.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)