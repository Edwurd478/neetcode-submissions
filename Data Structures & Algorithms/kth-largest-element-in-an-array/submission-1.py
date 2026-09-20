import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)
        result = -1
        for i in range(k):
            if not max_heap:
                break
            result = -heapq.heappop(max_heap)
        return result
