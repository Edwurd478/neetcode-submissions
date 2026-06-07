class MyHashSet:

    def __init__(self):
        self.arr = []
        

    def add(self, key: int) -> None:
        for a in self.arr:
            if a == key:
                return
        self.arr.append(key)

    def remove(self, key: int) -> None:
        for i in range(len(self.arr)):
            if key == self.arr[i]:
                self.arr.pop(i)
                return
        

    def contains(self, key: int) -> bool:
        for n in self.arr:
            if n == key:
                return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)