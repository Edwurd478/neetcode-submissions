class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currProf = 0
        ans = 0
        for i in range(1, len(prices)):
            if currProf < 0:
                currProf = 0
            
            currProf += prices[i] - prices[i-1]
            ans = max(ans, currProf)
        
        return ans
