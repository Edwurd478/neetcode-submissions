class MyHashMap:

    def __init__(self):
        self.keys = []
        self.vals = []

    def put(self, key: int, value: int) -> None:
        for i in range(len(self.keys)):
            if self.keys[i] == key:
                self.vals[i] = value
                return
        self.keys.append(key)
        self.vals.append(value)

    def get(self, key: int) -> int:
        for i in range(len(self.keys)):
            if self.keys[i] == key:
                return self.vals[i]
        return -1
        

    def remove(self, key: int) -> None:
        for i in range(len(self.keys)):
            if self.keys[i] == key:
                self.keys.pop(i)
                self.vals.pop(i)
                return
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)