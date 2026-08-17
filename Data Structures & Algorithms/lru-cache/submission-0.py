class Node:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

        self.cap = capacity
        self.size = 0
        self.cache = {}

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        self.cache[key].prev.next = self.cache[key].next
        self.cache[key].next.prev = self.cache[key].prev
        
        self.cache[key].prev = self.head
        self.cache[key].next = self.head.next
        
        self.head.next.prev = self.cache[key]
        self.head.next = self.cache[key]

        return self.cache[key].val



    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            
            self.cache[key].prev.next = self.cache[key].next
            self.cache[key].next.prev = self.cache[key].prev
            self.cache[key].prev = self.head
            self.cache[key].next = self.head.next
            self.head.next.prev = self.cache[key]
            self.head.next = self.cache[key]
        else:
            if self.size >= self.cap:
                delete = self.tail.prev.key
                self.cache.pop(delete)
                self.tail.prev.prev.next = self.tail
                self.tail.prev = self.tail.prev.prev
            else:
                self.size += 1

            self.cache[key] = Node(key, value)
            self.cache[key].prev = self.head
            self.cache[key].next = self.head.next
            self.head.next.prev = self.cache[key]
            self.head.next = self.cache[key]
