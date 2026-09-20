import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def get_distance(coord):
            return coord[0]**2 + coord[1]**2
        
        heap = []
        for point in points:
            heapq.heappush(heap, (get_distance(point), point))
        
        result = []
        for i in range(k):
            if not heap:
                break
            result.append(heapq.heappop(heap)[1])
        return result