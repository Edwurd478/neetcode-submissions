"""
[1, 2, 3, 4, 5] -> [3, 4, 5]

[1, 2, 3, 4, 5, 6] -> [3, 4, 5, 6]

keep top n // 2 + 1

[3, 5, 7] -> [5, 7]
"""
import heapq
class MedianFinder:

    def __init__(self):
        self.top_half = []
        self.bottom_half = []
        self.n = 0

    def addNum(self, num: int) -> None:
        self.n += 1
        if not self.top_half or num > self.top_half[0]:
            heapq.heappush(self.top_half, num)
        else:
            heapq.heappush(self.bottom_half, -num)
        
        while len(self.top_half) > self.n//2 + 1:
            heapq.heappush(self.bottom_half, -heapq.heappop(self.top_half))
        while len(self.top_half) < self.n//2 + 1:
            heapq.heappush(self.top_half, -heapq.heappop(self.bottom_half))

        """
        if len(self.top_half) < self.n//2 + 1:
            heapq.heappush(self.top_half, num)
        elif len(self.top_half) == self.n//2 + 1 and num > self.top_half[0]:
            heapq.heappop(self.top_half)
            heapq.heappush(self.top_half, num)
        """
        

    def findMedian(self) -> float:
        if self.n % 2 == 1:
            return self.top_half[0]
        else:
            elt = heapq.heappop(self.top_half)
            result = (elt + self.top_half[0]) / 2
            heapq.heappush(self.top_half, elt)
            return result
        
        