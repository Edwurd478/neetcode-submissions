class Solution:
    def simulateEating(self, k: int) -> int:    # number of hours required to finish all bananas
        tot = 0
        for p in self.piles:
            tot += p // k
            if p % k != 0:
                tot += 1
        return tot
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        self.piles = piles
        lo, hi = 1, max(piles)
        ans = float('inf')
        
        while lo <= hi:
            mid = (hi + lo) // 2
            time = self.simulateEating(mid)
            if time <= h:
                hi = mid - 1
                ans = min(ans, mid)
            else:
                lo = mid + 1

        return ans