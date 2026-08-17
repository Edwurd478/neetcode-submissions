import heapq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        closestK = []
        for a in arr:
            diff = -abs(x - a)
            if len(closestK) < k:
                heapq.heappush(closestK, (diff, a))
            else:
                if -diff < -closestK[0][0]:
                    heapq.heappop(closestK)
                    heapq.heappush(closestK, (diff, a))
        
        ans = []
        for i in range(k):
            ans.append(closestK[i][1])
        return sorted(ans)