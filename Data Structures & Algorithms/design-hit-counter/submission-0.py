from collections import deque
class HitCounter:

    def __init__(self):
        self.active = deque()

    def hit(self, timestamp: int) -> None:
        self.active.append(timestamp)
        while self.active and self.active[0] <= timestamp - 300:
            self.active.popleft()

    def getHits(self, timestamp: int) -> int:
        while self.active and self.active[0] <= timestamp - 300:
            self.active.popleft()
        return len(self.active)
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
