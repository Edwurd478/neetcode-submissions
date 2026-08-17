class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.size = 0
        self.head = None
        self.tail = None

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        if self.isEmpty():
            self.head = Node(value)
            self.tail = self.head
            self.tail.next = self.head
        else:
            self.tail.next = Node(value)
            self.tail.next.next = self.head
            self.tail = self.tail.next
            
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
        
        self.size -= 1
        return True

    def Front(self) -> int:
        return self.head.val if not self.isEmpty() else -1

    def Rear(self) -> int:
        return self.tail.val if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        return False if self.head else True

    def isFull(self) -> bool:
        return self.size >= self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()