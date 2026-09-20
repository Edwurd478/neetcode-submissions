import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.top_k = nums
        self.k = k
        heapq.heapify(self.top_k)
        while len(self.top_k) > k:
            heapq.heappop(self.top_k)

    def add(self, val: int) -> int:
        if not self.top_k or val >= self.top_k[0]:
            if len(self.top_k) == self.k:
                heapq.heappop(self.top_k)
            heapq.heappush(self.top_k, val)
        return self.top_k[0]
